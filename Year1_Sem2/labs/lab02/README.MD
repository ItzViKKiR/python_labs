# ЛР-2 — Коллекция объектов

## Предметная область
Недвижимость

## Объект
Property — объект недвижимости.

Более детально: [LAB01](/Year1_Sem2/labs/lab01)

## Коллекция
District — контейнер объектов Property.

Возможности:
- добавление и удаление объектов
- поиск по владельцу
- итерация
- индексация
- сортировка
- фильтрация

## Реализовано
- add / remove / remove_at
- find_by_owner
- __len__, __iter__, __getitem__
- sort / sort_by_price
- get_available
- get_with_debt

## Сценарии
1. Базовая работа с коллекцией

![demo1](/Year1_Sem2/labs/lab01/images/models.png)

2. Поиск и итерация

![demo2](/Year1_Sem2/labs/lab01/images/search.png)

3. Сортировка, фильтрация, индексация

![demo3](/Year1_Sem2/labs/lab01/images/sort.png)