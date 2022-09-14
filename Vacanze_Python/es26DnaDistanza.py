def distance(dna1, dna2):
    if (abs(len(dna1)-len(dna2)) == 0):
        cont = 0 
        lung = min(len(dna1), len(dna2))
        
        for i in range(lung):
            if dna1[i] != dna2[i]:
                cont += 1
        
        return cont
    else:
        raise ValueError("Strands must be of equal length.")

print(distance("ABDB","FGHS"))