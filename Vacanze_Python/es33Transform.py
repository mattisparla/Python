def transform(old):
    new = {}
    for key in old:
        for value in old[key]:
            new[value.lower()] = key
    return new


"""
L'obiettivo. il gol
Estrarremo alcuni punteggi di Scrabble da un sistema legacy.

Il vecchio sistema memorizzava un elenco di lettere per punteggio:

1 punto: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
2 punti: "D", "G",
3 punti: "B", "C", "M", "P",
4 punti: "F", "H", "V", "W", "Y",
5 punti: "K",
8 punti: "J", "X",
10 punti: "Q", "Z",
Il nuovo brillante sistema Scrabble invece memorizza il punteggio per lettera, il che rende molto più veloce e facile calcolare il punteggio per una parola. Memorizza anche le lettere in minuscolo indipendentemente dal caso delle lettere di input:

"a" vale 1 punto.
"b" vale 3 punti.
"c" vale 3 punti.
"d" vale 2 punti.
Eccetera.
La tua missione, se dovessi scegliere di accettarlo, è trasformare il formato dei dati legacy nel nuovo formato brillante."""
