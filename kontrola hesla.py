#heslo musi mat jedno male, jedno velke, byt ascii, aspon 10 znakov, pouzit jeden status
def checkio(heslo):
    status = True
    while status == True:
        if len(heslo) >= 10:
            for i in heslo:
                if not i.isascii():
                    status = False
        else:
            status = False
            return False
