diz={"black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,"green": 5,"blue": 6,
"violet": 7,"grey": 8,"white": 9}

def value(colors):

    return diz[colors[0]]*10+diz[colors[1]]

print(value(["black","red"]))