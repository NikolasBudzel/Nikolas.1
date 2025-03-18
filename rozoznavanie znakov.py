fr = open("slova.txt", "r", encoding="utf-8")
is_e = 0
is_not_e = 0
for i in fr:
    if i.count("e") > 0:
        is_e += 1
    else:
        is_not_e += 1
print(is_e,"\n",is_not_e)