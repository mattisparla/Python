def convert(number):
    s=""
    ok=False
    if number % 3 == 0:
        s=s+"Pling"
        ok=True
    if number % 5 == 0:
        s=s+"Plang"
        ok=True
    if number % 7 == 0:
        s=s+"Plong"
        ok=True
    if ok==True:
        return s
    else:
        return str(number)