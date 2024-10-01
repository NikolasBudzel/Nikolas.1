def binary(number):
    power_10 = 1
    result = 0
    while number != 0:
        modulo = number % 2 # zvysok po deleni 2: 0,1
        result = result+power_10*modulo # nasobenie 1,10,100,1000(mocnina 10)-cislo piseme odzadu
        number = number // 2 # 32/2, 16/2, 8/2, ....
        power_10 *= 10
    return result
print(binary(32))

def decimal(number):
    power_2 = 2
    result = 0
    while number != 0:
        ld = number % 10
        result = result+ld*power_2
        number = number // 10
        power_2 *= 2
    return result
print(decimal(10000))