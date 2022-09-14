def response(hey_bob):
    # Strips funzione usata per togliere lo spazio bianco
    frase = hey_bob.strip()
    
    if frase == "":
        return "Fine. Be that way!"
    elif frase.isupper():
        if frase.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif frase.endswith("?"):
        return "Sure."
    else:
        return "Whatever."
