def  celsuius_to_fahrenheit(celsuiu):
    return celsuiu * 9 / 5 + 32
print(celsuius_to_fahrenheit(0))

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def get_grade(score):
    if score >= 91:
        return 'Отлично'
    elif score >= 70:
        return 'Хорошо'
    elif score >= 50:
        return 'Удов'
    else:
        return "Неуд"
print(get_grade(70))
print(is_even(40))