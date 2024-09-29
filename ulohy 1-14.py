#uloha 1
from itertools import count
from sys import excepthook, exception


def uloha_1():
    for i in range (1,11):
        print(i)

#uloha 2 a
def uloha_2a():
    for i in range(1,int(input("N: "))+1):
        print(i)

#uloha 2 b
def uloha_2b():
    N = int(input("N: "))+1
    for i in range(1,N):
        if i == N-1:
            print(i)
        else:
            print(i, end=",")

#uloha 3
def uloha_3():
    N = int(input("N: "))+1
    for i in range(5,N,2):
        print(i)

#uloha 4
def uloha_4(N):
    for i in range(1,N+1):
        print(f" druha mocnina {i} je {i*i}")

#uloha 5
def uloha_5(a,b):
    if a <= b:
        for i in range(a,b):
            print(f"druha odmocnina {i} je {round((i**0.5), 2)}")
    else:
        print("parameter a musi byt mensi ako b")

#uloha 6
def uloha_6():
    for x in range(1,21):
        if x == 3:
            print(f"x = {x} funkcia nie je definovana")
        else:
            y = (x ** 2 - 1) / (x - 3)
            print(f"x = {x} y = {y}")

#uloha 7
def uloha_7(N):
    for i in range(1,N+1):
        if i % 3 == 0:
            print(i)

#uloha 8
def uloha_8():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)

#uloha 9
def uloha_9(z,k):
    for i in range(z,k):
        if i % 2 == 1:
            print(i)

#uloha 10
def uloha_10(N):
    for i in range(N,0,-1):
        if i == 1:
            print(i)
        else:
            print(i, end=",")

#uloha 11
def uloha_11(N):
    for i in range(0,N):
        if i % 7 == 0 and i % 4 == 0:
            print(i)

#uloha 12
def uloha_12(N):
    x = 0
    for i in range(1,N+1):
        x += i
    print(x)

#uloha 13
def uloha_13(N):
    x = 0
    for i in range(1,N+1):
        if i % 2 == 0:
            x += i
    print(x)

#uloha 14
def uloha_14(a,b):
    x = 0
    for i in range(a,b+1):
        if i % 8 == 0:
            x += 1
    print(x)

#uloha 15
def uloha_15(N):
    prvocislo = True
    for i in range(N-1,1,-1):
        if N % i == 0:
            prvocislo = False
            break
    print(f"cislo {N} je prvocislo: {prvocislo}")
