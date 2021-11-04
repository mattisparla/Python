parola= input("Dimmi una parola  ")
print(f"{parola}")
print(f"La prima lettera è {parola[0]} ")
print(f"La prima lettera è {parola[-1]} ")
print(parola[1:-1])
print(parola[::2])
print(parola[::-1])
parola_nuova=parola[:2]+"?"+parola[3:]
print(parola_nuova)