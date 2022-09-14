def leap_year(year):
    ok= False
    if(year % 4 == 0):
        if(year % 100 != 0):
                ok= True
        else:
            if(year % 400 == 0):
                ok=True
    return ok

if(leap_year(2004) == True):
    print("è un anno bisistile")
else:
    print("Non è bisistile")