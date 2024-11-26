def a_za_e(retazec:str):
    novy = ""
    for i in retazec:
        if i != "a":
            novy += i
        else:
            novy += "e"
    print(novy)
