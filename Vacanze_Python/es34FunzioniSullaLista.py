def append(list1, list2):
    for elemento in list2:
        list1.append(elemento)
    return list1


def concat(lists):
    out = []
    for lista in lists:
        for elemento in lista:
            out.append(elemento)
    return out


def filter(function, list):
    for el in list:
        if not function(el):
            list.remove(el)
    return list


def length(list):
    return len(list)


def map(function, list):
    out = []
    for el in list:
        out.append(function(el))
    return out


def foldl(function, list, initial):
    for el in list:
        initial = function(initial, el)
    return initial


def foldr(function, list, initial):
    for k in range(length(list)-1, -1, -1): #1p: punto inizio,2p: fine, 3p: avanzamento
        initial = function(list[k], initial)
    return initial


def reverse(list):
    out = []
    for k in range(length(list)-1, -1, -1):
        out.append(list[k])
    return out

"""
append( dati due elenchi, aggiungere tutti gli elementi del secondo elenco alla fine del primo elenco );
concatenate( data una serie di elenchi, combina tutti gli elementi in tutti gli elenchi in un elenco appiattito );
filter( dato un predicato e un elenco, restituisce l'elenco di tutti gli elementi per i quali predicate(item)è True );
length( data una lista, restituisce il numero totale di elementi al suo interno );
map( data una funzione e un elenco, restituisce l'elenco dei risultati dell'applicazione function(item)su tutti gli elementi );
foldl( data una funzione, un elenco e un accumulatore iniziale, piegare (ridurre) ogni elemento nell'accumulatore da sinistra usandofunction(accumulator, item) );
foldr( data una funzione, un elenco e un accumulatore iniziale, piegare (ridurre) ogni elemento nell'accumulatore da destra usandofunction(item, accumulator) );
reverse( data una lista, restituisce una lista con tutti gli elementi originali, ma in ordine inverso );"""
