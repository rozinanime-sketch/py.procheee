for i in (range(0,10)):
    print(i)

while True:
    if i != 0:
        break
    else:
        print(i)

list={1,2,3,4,5,6,7,8,9,10,"sdd"}
for i in list:
    print(i, end="")

array=[1.123, 22]
for i in array:
    if type(i)==str:
        print(i)
    else:
        print("Нет стринг")

word = "Hello"
for id in word:
    if id == "l":
        break
    print(id, end="")

letters = [("Точка", 10, 1.2), ("Валд", 22,1.3), ("Озон",2, 1.2), ("MAX", 5, 12.4),("DSC", 5, 2.1)]
for idcs in letters:
    print(idcs)


n = len(letters)

for w in range(n):
    for h in range(n - w - 1):
        if letters[h][2] > letters[h + 1][2]:
            letters[h], letters[h + 1] = letters[h + 1], letters[h]
print(letters)

product_name = "Ноутбук"
quantity = 2
price = 59999.90
is_number = True
coupon_code = "SALE20" or "NONE"
cart = {
    "product_name":product_name,
    "quantity":quantity,
    "price":price,
}
allowed_coupons = ["SALE20", "NEWYEAR", "VIP"]
total = price * quantity
discount = 0

if coupon_code in allowed_coupons and total > 10000:
    discount = total * 0.20
elif is_number:
    discount = total * 0.05
else:
    discount = 0

before_disc = total
after_disc = total - discount
tax = after_disc * 0.13
final_price = after_disc + tax
points = int(final_price * 0.01)
quantity_count = quantity ** 2
points_quantity_count = points + quantity_count
if "о" in product_name:
    product_name += " Акция"
print(f"=== ЧЕК МАГАЗИНА ===\nТовар: {product_name}\nЦена за шт: {price}\nКоличество: {quantity}\n--------------\nСумма до скидки: {before_disc}\nСкидка: {discount.__round__(2)}\nСумма после скидки: {after_disc}\nНалог(13%): {tax.__round__(2)}\n------------------\nИтого к оплате: {final_price}\n--------------------\nНачислено баллов: {points_quantity_count} (вкл. бонус за объем)\nТип данных суммы: {(type(final_price))} ")






