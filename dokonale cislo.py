def sucet_del(n):
    sucet = 0
    for i in range(1,n+1):
        if n % i == 0:
            sucet = sucet + i
    return sucet



def is_perfect(n):
    if sucet_del(n) == n*2:
        return True
    else:
        return False

for i in range(1,101):
    if is_perfect(i) == True:
        print(i)
