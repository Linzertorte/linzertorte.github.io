def get_token(s):
    return s.split(" ")[0]

f = open("souvlaki2.txt", "r")
txt = f.read().split("\n")
i = 0
while i < len(txt):
    if True:
        if not get_token(txt[i]).isdigit(): exit() # alert
        print(txt[i])
        print(txt[i+1])
        print(txt[i+2])
        print(txt[i+3])
        if get_token(txt[i+5]).startswith("-"):
            print(txt[i+4])
            if get_token(txt[i+6]).isdigit():
                print(txt[i+5])
                print()
                i+=6
            elif get_token(txt[i+6]) == "":
                print(txt[i+5])
                print()
                i+=7
            else:
                print(txt[i+5]+" "+txt[6])
                print()
                if get_token(txt[i+7]).isdigit():
                    i+=7
                else: i+=8
        else: 
            print(txt[i+4]+" "+txt[i+5])
            if get_token(txt[i+7]).isdigit():
                print(txt[i+6])
                print()
                i+=7
            elif get_token(txt[i+7]) == "":
                print(txt[i+6])
                print()
                i+=8
            else:
                print(txt[i+6]+" "+txt[i+7])
                print()
                if get_token(txt[i+8]).isdigit():
                    i+=8
                else: i+=9