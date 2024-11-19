import random
def bird_language(slovo):
    vowels = "aeiouy"
    preklad = ""
    for i in slovo:
        preklad += i
        if i in vowels:
            preklad += i*2
        else:
            preklad += random.choice(vowels)
    return preklad

print(bird_language("hello"))