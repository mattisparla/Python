def is_isogram(string):
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		count = 0
		for word in string:
			if letter == word.lower():
				count +=1
		if count > 1:
			return False
	return True

if(is_isogram("boscaioli") == True):
    print("è un isogramma")
else:
    print("Non è un isogramma")
    
"""Determina se una parola o una frase è un isogramma.

Un isogramma (noto anche come "parola senza motivo") è una parola o una frase senza una lettera ripetuta, tuttavia gli spazi e i trattini possono apparire più volte."""