def cifre(n):
    lista=[]                 # nessuna cifra... 
    while(n != 0): 
        quoziente=n//10 
        resto =n%10          # cifra meno significativa 
        lista.append(resto)  # aggiunge alla lista
        n=quoziente          # una cifra in meno
                              
    lista.reverse()          
    return lista

def is_armstrong_number(numero):
    lista=cifre(numero)
    nCifre=len(str(numero))
    num=0

    for n in lista:
        num=num+n**nCifre

    return (num == numero)