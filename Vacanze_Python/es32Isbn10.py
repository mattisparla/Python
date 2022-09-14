def is_valid(isbn):
    if not isbn:
        return False
    for char in isbn:
        if char == "-":
            isbn = isbn.replace(char, "")
    if len(isbn) != 10:
        return False
    result = 0
    for i, n in enumerate(isbn):
        try:
            n = int(n)
        except ValueError:
            if n == 'X' and i == (len(isbn) - 1):
                n = 10
            else:
                return False
        result += n * (len(isbn) - i)
    
    return result % 11 == 0

if (is_valid("3-598-21508-8")):
    print("Puo essere un codice ISBN 10")
else:
    print("Noon puo essere un codice ISBN")