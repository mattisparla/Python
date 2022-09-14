def commands(binary_str):
    mod=[]
    flag=False
    number=int(binary_str,2)
    while number!=0:
        if number>=16:
            number-=16
            flag=True
        elif number>=8:
            number-=8
            mod.append('jump')
        elif number>=4:
            number-=4
            mod.append('close your eyes')
        elif number>=2:
            number-=2
            mod.append('double blink')
        else:
            number-=1
            mod.append('wink')
    mod.reverse()
    if flag==True:
        mod.reverse()
    return mod

print(commands("00011"))
"""
Tu e il tuo compagno di coorte di quelli che "sanno" quando si tratta di binari decidete di inventare una "stretta di mano" segreta.

00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump


10000 = Reverse the order of the operations in the secret handshake.
Dato un numero decimale, convertilo nella sequenza di eventi appropriata per un handshake segreto.

Ecco un paio di esempi:

Dato l'input decimale 3, la funzione restituirebbe l'array ["wink", "doppio lampeggio"] perché il numero decimale 3 è 2+1 in potenze di due e quindi 11in binario.

Esaminiamo ora l'input 19 che è 16+2+1 in potenze di due e quindi 10011in binario. Ricordando che l'aggiunta di 16 ( 10000in binario) inverte un array e che sappiamo già quale array viene restituito dato l'input 3, l'array restituito per l'input 19 è ["doppio lampeggio", "occhiolino"].

Per semplificare le cose (e per consentirti di concentrarti sulla parte importante di questo esercizio), la tua funzione riceverà i suoi input come stringhe binarie:"""
