import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional
import validators

class PropertyStatus(Enum):
    AVAILABLE = "Доступна"
    RENTED = "Сдана"
    SOLD = "Продана"
    MORTGAGE = "В ипотеке"

class Owner:
    tax_rate = 0.13
    
    def __init__(self, full_name: str, phone: str, email: str):
        self._full_name = validators.validate_string(full_name, "ФИО", min_len=5)
        self._phone = validators.validate_phone(phone)
        self._email = validators.validate_email(email)
        self._owner_id = str(uuid.uuid4())[:8]
        self._properties = []
        self._is_active = True
    
    @property
    def full_name(self): return self._full_name
    @property
    def phone(self): return self._phone
    @property
    def email(self): return self._email
    @property
    def owner_id(self): return self._owner_id
    @property
    def properties(self): return self._properties.copy()
    @property
    def is_active(self): return self._is_active
    
    @phone.setter
    def phone(self, new_phone: str):
        self._phone = validators.validate_phone(new_phone)
    
    def add_property(self, p):
        if not self._is_active:
            raise RuntimeError("Нельзя добавить недвижимость к неактивному владельцу")
        if p not in self._properties:
            self._properties.append(p)
    
    def remove_property(self, p):
        if p in self._properties:
            self._properties.remove(p)
    
    def deactivate(self):
        if self._properties:
            raise RuntimeError("Нельзя деактивировать владельца с недвижимостью")
        self._is_active = False
    
    def activate(self):
        self._is_active = True
    
    def __str__(self):
        status = "Активен" if self._is_active else "Неактивен"
        return f"Владелец: {self._full_name} | Тел: {self._phone} | Объектов: {len(self._properties)} | {status}"
    
    def __repr__(self): return f"Owner(full_name={self._full_name!r})"
    def __eq__(self, other): return isinstance(other, Owner) and self._owner_id == other._owner_id


class Apartment:
    currency = "RUB"
    
    def __init__(self, address: str, area: float, price: float, owner: Owner, 
                 floor: int, mortgage_rate: float = 0.0):
        self._address = validators.validate_string(address, "Адрес", min_len=5)
        self._area = validators.validate_positive_float(area, "Площадь")
        self._price = validators.validate_positive_float(price, "Цена")
        
        if not isinstance(owner, Owner):
            raise TypeError("owner должен быть экземпляром Owner")
        self._owner = owner
        owner.add_property(self)
        
        self._floor = validators.validate_positive_int(floor, "Этаж")
        if floor > 100:
            raise ValueError("Этаж не может быть больше 100")
        
        self._mortgage_rate = validators.validate_positive_float(mortgage_rate, "Ставка", allow_zero=True)
        if mortgage_rate > 30:
            raise ValueError("Ставка не может быть больше 30%")
        
        self._apartment_id = str(uuid.uuid4())[:8]
        self._status = PropertyStatus.AVAILABLE
        self._utilities_debt = 0.0
        self._mortgage_debt = 0.0
    
    @property
    def address(self): return self._address
    @property
    def area(self): return self._area
    @property
    def price(self): return self._price
    @property
    def owner(self): return self._owner
    @property
    def floor(self): return self._floor
    @property
    def status(self): return self._status
    @property
    def utilities_debt(self): return self._utilities_debt
    @property
    def mortgage_rate(self): return self._mortgage_rate
    @property
    def mortgage_debt(self): return self._mortgage_debt
    
    @price.setter
    def price(self, new_price: float):
        if self._status in (PropertyStatus.SOLD, PropertyStatus.RENTED, PropertyStatus.MORTGAGE):
            raise RuntimeError(f"Нельзя изменить цену в статусе {self._status.value}")
        self._price = validators.validate_positive_float(new_price, "Цена")
    
    @owner.setter
    def owner(self, new_owner: Owner):
        if self._status == PropertyStatus.SOLD:
            raise RuntimeError("Нельзя сменить владельца проданной квартиры")
        if not isinstance(new_owner, Owner):
            raise TypeError("new_owner должен быть Owner")
        self._owner.remove_property(self)
        self._owner = new_owner
        new_owner.add_property(self)
    
    def add_utilities_debt(self, amount: float):
        if self._status == PropertyStatus.SOLD:
            raise RuntimeError("Нельзя начислить ЖКХ на проданную квартиру")
        self._utilities_debt += validators.validate_positive_float(amount, "Сумма", allow_zero=True)
    
    def pay_utilities(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        payment = validators.validate_positive_float(amount, "Платеж")
        self._utilities_debt = max(0, self._utilities_debt - payment)
    
    def take_mortgage(self):
        if self._status != PropertyStatus.AVAILABLE:
            raise RuntimeError(f"Нельзя оформить ипотеку в статусе {self._status.value}")
        if self._mortgage_rate == 0:
            raise RuntimeError("Не указана ставка")
        self._status = PropertyStatus.MORTGAGE
        self._mortgage_debt = self._price
        print(f"Ипотека оформлена")
    
    def pay_mortgage(self, amount: float):
        if self._status != PropertyStatus.MORTGAGE:
            raise RuntimeError("Ипотека не оформлена")
        payment = validators.validate_positive_float(amount, "Платеж")
        if payment >= self._mortgage_debt:
            self._mortgage_debt = 0
            self._status = PropertyStatus.AVAILABLE
            print(f"Ипотека погашена")
        else:
            self._mortgage_debt -= payment
            print(f"Остаток: {self._mortgage_debt:.2f}")
    
    def sell(self, new_owner: Owner, final_price: Optional[float] = None):
        if self._status in (PropertyStatus.SOLD, PropertyStatus.RENTED, PropertyStatus.MORTGAGE):
            raise RuntimeError(f"Нельзя продать в статусе {self._status.value}")
        price = final_price if final_price else self._price
        price = validators.validate_positive_float(price, "Цена")
        self.owner = new_owner
        self._price = price
        self._status = PropertyStatus.SOLD
        print(f"Квартира продана")
    
    def __str__(self):
        debt = f", Долг: {self._utilities_debt:.2f}" if self._utilities_debt > 0 else ""
        mortgage = f", Ипотека: {self._mortgage_debt:.2f}" if self._mortgage_debt > 0 else ""
        return (f"Кв.{self._apartment_id} | {self._address} | {self._area:.1f}м² | "
                f"Цена: {self._price:,.2f} {self.currency} | Этаж: {self._floor} | "
                f"{self._status.value}{mortgage}{debt}")
    
    def __repr__(self): return f"Apartment(address={self._address!r})"
    def __eq__(self, other): return isinstance(other, Apartment) and self._apartment_id == other._apartment_id


class House:
    currency = "RUB"
    
    def __init__(self, address: str, area: float, price: float, owner: Owner,
                 land_area: float, mortgage_rate: float = 0.0):
        self._address = validators.validate_string(address, "Адрес", min_len=5)
        self._area = validators.validate_positive_float(area, "Площадь")
        self._price = validators.validate_positive_float(price, "Цена")
        
        if not isinstance(owner, Owner):
            raise TypeError("owner должен быть Owner")
        self._owner = owner
        owner.add_property(self)
        
        self._land_area = validators.validate_positive_float(land_area, "Площадь участка")
        
        self._mortgage_rate = validators.validate_positive_float(mortgage_rate, "Ставка", allow_zero=True)
        if mortgage_rate > 30:
            raise ValueError("Ставка не может быть больше 30%")
        
        self._house_id = str(uuid.uuid4())[:8]
        self._status = PropertyStatus.AVAILABLE
        self._mortgage_debt = 0.0
    
    @property
    def address(self): return self._address
    @property
    def area(self): return self._area
    @property
    def price(self): return self._price
    @property
    def owner(self): return self._owner
    @property
    def land_area(self): return self._land_area
    @property
    def status(self): return self._status
    @property
    def mortgage_rate(self): return self._mortgage_rate
    @property
    def mortgage_debt(self): return self._mortgage_debt
    
    @price.setter
    def price(self, new_price: float):
        if self._status in (PropertyStatus.SOLD, PropertyStatus.RENTED, PropertyStatus.MORTGAGE):
            raise RuntimeError(f"Нельзя изменить цену в статусе {self._status.value}")
        self._price = validators.validate_positive_float(new_price, "Цена")
    
    @owner.setter
    def owner(self, new_owner: Owner):
        if self._status == PropertyStatus.SOLD:
            raise RuntimeError("Нельзя сменить владельца проданного дома")
        if not isinstance(new_owner, Owner):
            raise TypeError("new_owner должен быть Owner")
        self._owner.remove_property(self)
        self._owner = new_owner
        new_owner.add_property(self)
    
    def take_mortgage(self):
        if self._status != PropertyStatus.AVAILABLE:
            raise RuntimeError(f"Нельзя оформить ипотеку в статусе {self._status.value}")
        if self._mortgage_rate == 0:
            raise RuntimeError("Не указана ставка")
        self._status = PropertyStatus.MORTGAGE
        self._mortgage_debt = self._price
        print(f"Ипотека оформлена")
    
    def pay_mortgage(self, amount: float):
        if self._status != PropertyStatus.MORTGAGE:
            raise RuntimeError("Ипотека не оформлена")
        payment = validators.validate_positive_float(amount, "Платеж")
        if payment >= self._mortgage_debt:
            self._mortgage_debt = 0
            self._status = PropertyStatus.AVAILABLE
            print(f"Ипотека погашена")
        else:
            self._mortgage_debt -= payment
            print(f"Остаток: {self._mortgage_debt:.2f}")
    
    def sell(self, new_owner: Owner, final_price: Optional[float] = None):
        if self._status in (PropertyStatus.SOLD, PropertyStatus.RENTED, PropertyStatus.MORTGAGE):
            raise RuntimeError(f"Нельзя продать в статусе {self._status.value}")
        price = final_price if final_price else self._price
        price = validators.validate_positive_float(price, "Цена")
        self.owner = new_owner
        self._price = price
        self._status = PropertyStatus.SOLD
        print(f"Дом продан")
    
    def __str__(self):
        mortgage = f", Ипотека: {self._mortgage_debt:.2f}" if self._mortgage_debt > 0 else ""
        return (f"Дом.{self._house_id} | {self._address} | {self._area:.1f}м² | "
                f"Участок: {self._land_area:.1f}м² | Цена: {self._price:,.2f} {self.currency} | "
                f"{self._status.value}{mortgage}")
    
    def __repr__(self): return f"House(address={self._address!r})"
    def __eq__(self, other): return isinstance(other, House) and self._house_id == other._house_id


class RentalContract:
    max_duration_months = 12
    
    def __init__(self, apartment: Apartment, tenant_name: str, tenant_phone: str,
                 monthly_rent: float, start_date, duration_months: int):
        if not isinstance(apartment, Apartment):
            raise TypeError("apartment должен быть Apartment")
        if apartment.status != PropertyStatus.AVAILABLE:
            raise ValueError("Квартира не доступна для аренды")
        
        self._apartment = apartment
        self._tenant_name = validators.validate_string(tenant_name, "Имя", min_len=2)
        self._tenant_phone = validators.validate_phone(tenant_phone)
        self._monthly_rent = validators.validate_positive_float(monthly_rent, "Аренда")
        self._start_date = validators.validate_date(start_date, "Дата")
        self._duration_months = validators.validate_positive_int(duration_months, "Длительность")
        
        if duration_months > self.max_duration_months:
            raise ValueError(f"Максимум {self.max_duration_months} месяцев")
        
        self._end_date = self._start_date + timedelta(days=30 * duration_months)
        self._contract_id = str(uuid.uuid4())[:8]
        self._is_active = True
        self._total_paid = 0.0
        apartment._status = PropertyStatus.RENTED
    
    @property
    def apartment(self): return self._apartment
    @property
    def tenant_name(self): return self._tenant_name
    @property
    def monthly_rent(self): return self._monthly_rent
    @property
    def is_active(self): return self._is_active
    
    @monthly_rent.setter
    def monthly_rent(self, new_rent: float):
        if not self._is_active:
            raise RuntimeError("Нельзя изменить неактивный договор")
        self._monthly_rent = validators.validate_positive_float(new_rent, "Аренда")
    
    def pay_rent(self, amount: float):
        if not self._is_active:
            raise RuntimeError("Договор не активен")
        if datetime.now() > self._end_date:
            self.terminate()
            raise RuntimeError("Срок истек")
        self._total_paid += validators.validate_positive_float(amount, "Платеж")
        print(f"Оплачено {amount}")
    
    def terminate(self):
        if not self._is_active:
            return
        self._is_active = False
        if self._apartment.status == PropertyStatus.RENTED:
            self._apartment._status = PropertyStatus.AVAILABLE
        print("Договор завершен")
    
    def __str__(self):
        status = "Активен" if self._is_active else "Завершен"
        return (f"Договор {self._contract_id} | {self._tenant_name} | "
                f"Плата: {self._monthly_rent} {Apartment.currency}/мес | {status}")
    
    def __repr__(self): return f"RentalContract(tenant_name={self._tenant_name!r})"
    def __eq__(self, other): return isinstance(other, RentalContract) and self._contract_id == other._contract_id


class AgencyListing:
    commission_rate = 0.03
    
    def __init__(self, property_obj, agent_name: str):
        if not isinstance(property_obj, (Apartment, House)):
            raise TypeError("property_obj должен быть Apartment или House")
        self._property = property_obj
        self._agent_name = validators.validate_string(agent_name, "Имя агента", min_len=2)
        self._listing_id = str(uuid.uuid4())[:8]
        self._created_date = datetime.now()
        self._views = 0
        self._is_featured = False
    
    @property
    def property(self): return self._property
    @property
    def agent_name(self): return self._agent_name
    @property
    def listing_id(self): return self._listing_id
    @property
    def views(self): return self._views
    @property
    def is_featured(self): return self._is_featured
    
    @is_featured.setter
    def is_featured(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("Значение должно быть bool")
        if value and self._property.status == PropertyStatus.SOLD:
            raise RuntimeError("Нельзя продвигать проданную недвижимость")
        self._is_featured = value
    
    def add_view(self): 
        self._views += 1
    
    def feature(self): 
        self.is_featured = True
    
    def calculate_commission(self, sale_price: float) -> float:
        price = validators.validate_positive_float(sale_price, "Цена")
        commission = price * self.commission_rate
        return commission * 1.2 if self._is_featured else commission
    
    def get_listing_age_days(self) -> int: 
        return (datetime.now() - self._created_date).days
    
    def __str__(self):
        return (f"Листинг {self._listing_id} {'★' if self._is_featured else '☆'} | "
                f"Агент: {self._agent_name} | Просмотров: {self._views} | {self._property}")
    
    def __repr__(self): 
        return f"AgencyListing(agent_name={self._agent_name!r})"
    
    def __eq__(self, other): 
        return isinstance(other, AgencyListing) and self._listing_id == other._listing_id