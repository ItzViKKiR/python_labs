price=int(input('Введите цену:'))
discount=int(input('Введите скидку:'))
vat=int(input('Введите НДС:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base} ₽')
print(f'НДС: {vat_amount} ₽')
print(f'Итого к оплате: {total} ₽')