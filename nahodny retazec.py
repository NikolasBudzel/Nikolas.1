import random
x = int(input("napis mi dlzku: "))
def nahodny_retazec(x):
    samohlasky = "aeiouy"
    spoluhlasky = "qwrtpsdfghjklzxcvbnm"
    nr = ""
    for i in range(0, x):
        if i % 2 == 0:
            nr = nr + random.choice(samohlasky)
        else:
            nr = nr + random.choice(spoluhlasky)
    return nr
print(nahodny_retazec(x))