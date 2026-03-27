rus = [chr(i) for i in range(ord('А'), ord('Я')+1)]
word = "ТХСЗФС ЙФПСЗБСЁУФТ!"
for n in range(1, len(rus)+1):
    res = ""
    for ch in word:
        if ch in rus:
            idx = rus.index(ch)
            original_idx = (idx - n) % len(rus)
            res += rus[original_idx]
        else:
            res += ch
    print(f"Сдвиг {n}: {res}")
