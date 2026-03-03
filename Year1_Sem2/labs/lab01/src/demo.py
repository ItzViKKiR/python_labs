from model import Owner, Apartment, House, RentalContract, AgencyListing
from datetime import datetime

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")

print_separator("1. Создание владельцев")
owner1 = Owner("Иванов Иван Иванович", "+7 (999) 123-45-67", "ivanov@mail.com")
owner2 = Owner("Петрова Анна Сергеевна", "+7 (999) 765-43-21", "petrova@mail.com")
print(owner1)
print(owner2)

print_separator("2. Создание квартиры и дома")
apt = Apartment("ул. Ленина, д.1, кв.5", 45.5, 7500000, owner1, 3, mortgage_rate=9.5)
house = House("ул. Лесная, д.10", 120.0, 15000000, owner2, 600, mortgage_rate=8.0)
print(apt)
print(house)

print_separator("3. Демонстрация ипотеки")
apt.take_mortgage()
print(apt)
apt.pay_mortgage(1000000)
apt.pay_mortgage(2000000)

try:
    apt.sell(owner2)
except RuntimeError as e:
    print(f"Ошибка: {e}")

apt.pay_mortgage(4500000)
print(apt)

print_separator("4. Работа с долгами ЖКХ")
apt.add_utilities_debt(5000)
print(f"После начисления: {apt}")
apt.pay_utilities(3000)
print(f"После оплаты: {apt}")

print_separator("5. Договор аренды")
contract = RentalContract(
    apartment=apt,
    tenant_name="Сидоров Петр",
    tenant_phone="+7 (999) 111-22-33",
    monthly_rent=35000,
    start_date=datetime.now(),
    duration_months=6
)
print(contract)
contract.pay_rent(35000)
contract.terminate()
print(contract)

print_separator("6. Листинг агентства")
listing = AgencyListing(house, "Смирнова Е.В.")
print(listing)
listing.add_view()
listing.add_view()
listing.add_view()
listing.feature()
print(f"После продвижения: {listing}")
print(f"Комиссия: {listing.calculate_commission(16000000):,.2f}")

print_separator("7. Смена владельца")
print(f"Владелец: {apt.owner.full_name}")
apt.owner = owner2
print(f"Новый владелец: {apt.owner.full_name}")

print_separator("8. Продажа")
print(f"До продажи: {house}")
house.sell(owner1, 16500000)
print(f"После продажи: {house}")

print_separator("9. Демонстрация состояния владельца")
print(f"owner1 активен: {owner1.is_active}")
try:
    owner1.deactivate()
except RuntimeError as e:
    print(f"Ошибка деактивации: {e}")
owner1.remove_property(apt)
owner1.remove_property(house)
owner1.deactivate()
print(f"После деактивации: {owner1}")

print_separator("10. Валидация")
try:
    apt_invalid = Apartment("", -10, -5000, owner1, 200)
except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")

print_separator("11. Атрибуты класса")
print(f"Apartment.currency = {Apartment.currency}")
print(f"apt.currency = {apt.currency}")
print(f"Owner.tax_rate = {Owner.tax_rate}")

print_separator("12. Сравнение")
print(f"apt == house? {apt == house}")
print(f"owner1 == owner2? {owner1 == owner2}")

print_separator("13. Итоговое состояние")
print(owner1)
print(owner2)
print(apt)
print(house)
print(contract)
print(listing)