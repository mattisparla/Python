def score(x, y):
    distanza = (x ** 2  + y ** 2) ** 0.5
    
    if distanza <= 1:
      return 10
    elif distanza <= 5 :
      return 5
    elif distanza <= 10 :
      return 1
    else:
      return 0


      