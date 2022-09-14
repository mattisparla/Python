def flatten(iterable):
    mod = []
    for elemento in iterable:
        if isinstance(elemento, list): 
            flat = flatten(elemento)
            mod += flat
        else:
            if elemento is not None:
                mod.append(elemento)
    return mod

print(flatten([1,2,[2,3,None],5,6]))
"""
Nel linguaggio python la funzione isistance() mi permette di verificare se un oggetto è un'istanza di una classe."""