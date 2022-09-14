def square(number):
    numPrec=0
    if(number <= 0 or number > 64): 
        return("Square must be between 1 and 64")
    else:
        for n in range(number):
            if(n == 0):
                numPrec=1
            else:
                numPrec=numPrec*2
    
        return numPrec
        


def total():
    tot=0
    numPrec=0
    for n in range(64):
        if(n == 0):
            tot=1
            numPrec=1
        else:
            tot=tot+numPrec*2
            numPrec=numPrec*2
    return tot

print(total())
print(square(4))