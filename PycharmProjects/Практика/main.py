# 1 упр
n = int(input("Любое число "))
for i in range(1, n+1):
    if n % i != 0:
        print(f"квадрат {i} равен {i ** 2}")
# 2 упр
user_input = str(input("По одному символу "))
count = 0
while True:
    length = len(user_input)
    count += 1
    count = length
    if user_input == ".":
        break
    print(f"количество {count}")
    break

# 3 упр
dd = []
def number(*args):
    return sum(args)
def mid (lst):
    return sum(lst) / len(lst)
while True:
    gfg = float(input("Любое произвольное число: "))
    dd.append(gfg)
    print(number(gfg))
    cont_input = input("Вы закончили? если да нажмите: y/Y")
    if cont_input == "y" or cont_input == "Y":
        break
print(dd)
print(sum(dd))
print(mid(dd))


