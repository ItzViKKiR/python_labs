# ЛР-5 — Функции как аргументы. Стратегии и делегаты.

## Предметная область
Недвижимость

## Объекты
Система управления недвижимостью:
- объекты аренды 
- объекты с ипотекой 

## Реализованные функции и стратегии

### Стратегии сортировки 
- by_price(item) — по цене
- by_owner(item) — по имени владельца
- by_rent_term(item) — по сроку аренды
- by_price_and_owner(item) — по цене, затем по владельцу

### Функции-фильтры 
- is_available(item) — объект доступен для аренды/продажи
- has_debt(item) — есть задолженность по ЖКХ
- is_rental(item) — объект является экземпляром RentalProperty

### Фабрики функций (высший порядок)
- make_price_filter(max_price) — создаёт предикат фильтрации по максимальной цене
- apply_discount(factor) — создаёт функцию применения скидки к цене объекта

### Callable-стратегии
- DiscountStrategy — применяет фиксированную скидку 10% при вызове объекта
- RentTermIncreaseStrategy — увеличивает срок аренды на 1 месяц при вызове


### Методы коллекции PropertyCollection
- sort_by(key_func) — возвращает новую отсортированную коллекцию
- filter_by(predicate) — возвращает новую отфильтрованную коллекцию
- apply(func) — применяет функцию ко всем элементам текущей коллекции (возвращает себя)


## Демонстрация работы

В `demo.py` реализованы три сценария:

### Сценарий 1 — Цепочка операций

![P1](/Year1_Sem2/labs/lab05/images/p1.png)

### Сценарий 2 — Взаимозаменяемость стратегий

![P2](/Year1_Sem2/labs/lab05/images/p2.png)

### Сценарий 3 — Callable-стратегии

![P3](/Year1_Sem2/labs/lab05/images/p3.png)



# Factory? Factory!

<p align="center">
  <img width="498" height="281" src="https://media1.tenor.com/m/rul-xnjkETUAAAAC/endfield-akendfield.gif">
</p>


