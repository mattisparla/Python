def rotate(text, rotation):
    lower = 'abcdefghijklmnopqrstuvwxyz' * 2
    upper = lower.upper()
    tot = ''
    for car in text:
        if car.isalpha():
            if car.islower():
                tot += lower[lower.index(car) + rotation]
            else:
                tot += upper[upper.index(car) + rotation]
        else:
            tot += car
    return tot
"""
Creare un'implementazione del cifrario rotazionale, talvolta chiamato anche cifrario di Cesare.

Il cifrario di Cesare è un semplice cifrario a scorrimento che si basa sulla trasposizione di tutte le lettere dell'alfabeto utilizzando una chiave intera tra 0e 26. L'uso di una chiave di 0o 26produrrà sempre lo stesso risultato a causa dell'aritmetica modulare. La lettera viene spostata di tanti valori quanti sono i valori della chiave.

La notazione generale per i cifrari rotazionali è ROT + <key>. Il cifrario rotazionale più comunemente usato è ROT13.

Una ROT13sull'alfabeto latino sarebbe la seguente:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: nopqrstuvwxyzabcdefghijklm
È più forte del codice Atbash perché ha 27 chiavi possibili e 25 chiavi utilizzabili.

Il testo cifrato viene scritto con la stessa formattazione dell'input, inclusi spazi e punteggiatura."""