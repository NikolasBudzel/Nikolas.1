#uloha 1
def uloha_1():
    print("uloha 1:")
    for i in range (1,11):
        print(i)

#uloha 2 a
def uloha_2a():
    print("uloha 2 a:")
    for i in range(1,int(input("N: "))+1):
        print(i)

#uloha 2 b
def uloha_2b():
    print("uloha 2 b:")
    N = int(input("N: "))+1
    for i in range(1,N):
        if i == N-1:
            print(i)
        else:
            print(i, end=",")

#uloha 3
def uloha_2():
    print("uloha 3:")
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

