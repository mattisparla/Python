def find_anagrams(word, candidates):
    word = word.lower()
    ret = []
    for c in candidates:
        ret.append(c)
        c = c.lower()
        if c == word:
            ret.pop()
        else:
            for letter in c:
                if c.count(letter) != word.count(letter):
                    ret.pop()
                    break
        
    
        
    return ret

"""
Istruzioni
Un anagramma è un riarrangiamento di lettere per formare una nuova parola: ad esempio "owns"è un anagramma di "snow". Una parola non è il suo stesso anagramma: ad esempio, "stop"non è un anagramma di "stop".

Data una parola obiettivo e un insieme di parole candidate, questo esercizio richiede l'insieme di anagrammi: il sottoinsieme dei candidati che sono anagrammi della destinazione.

Il target ei candidati sono parole di uno o più caratteri alfabetici ASCII ( A- Ze a- z). I caratteri minuscoli e maiuscoli sono equivalenti: ad esempio, "PoTS"è un anagramma di "sTOp", ma StoPnon è un anagramma di sTOp. L'insieme di anagrammi è il sottoinsieme dell'insieme candidato che sono anagrammi dell'obiettivo (in qualsiasi ordine). Le parole nel set di anagrammi dovrebbero avere la stessa lettera maiuscola del set candidato.

Dati il ​​target "stone"e i candidati "stone", "tones", "banana", "tons", "notes", "Seton", l'insieme di anagrammi è "tones", "notes", "Seton"
"""