def to_camel_case(text):
    novy = ""
    for i in range(0,len(text)):
        if text[i] != "-" or "_":
            novy += text[i]
        else:
            novy += text[i+1]
    return novy
print(to_camel_case("_hovdasdas"))