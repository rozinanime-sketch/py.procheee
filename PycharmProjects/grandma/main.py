import random
count = 0
print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!, ")
while count < 3:
    q = input()
    if q == "POKA":
        count += 1
        print("НЕТ, НИ РАЗУ С ",random.randrange(1930, 1950), " ГОДА!")
    else:
        count = 0
        if q == q.upper():
            print("НЕТ, НИ РАЗУ С", random.randrange(1930, 1950), " ГОДА!.")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
    if count == 3:
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break