# Алфавит (без Ё)
rus = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def shift_char(ch, step):
    """Сдвиг буквы ch на step позиций в алфавите rus"""
    if ch not in rus:
        return ch
    idx = rus.index(ch)
    return rus[(idx + step) % len(rus)]

def alternating_caesar_reverse_first(text, step):
    """Чередующийся Цезарь: первая буква назад, вторая вперед"""
    res = ""
    for i, ch in enumerate(text):
        if i % 2 == 0:  # первая, третья и т.д.
            res += shift_char(ch, -step)  # назад
        else:           # вторая, четвертая и т.д.
            res += shift_char(ch, step)   # вперед
    return res

# Пример текста
word = "ТХСЗФС ЙФПСЗБСЕУФТ!"
word = word.replace("Ё", "Е")  # убираем Ё

# Перебор ключей 1–33
for k in range(1, 34):
    result = alternating_caesar_reverse_first(word, k)
    print(f"Ключ={k}: {result}")