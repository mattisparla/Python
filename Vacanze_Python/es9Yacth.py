from enum import Enum
# Score categories.
# Change the values as you see fit.

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    categories = {  #faccio un dizionario con le varie combinazioni associate ai nomi
        ONES: dice.count(1),
        TWOS: dice.count(2) * 2,
        THREES: dice.count(3) * 3,
        FOURS: dice.count(4) * 4,
        FIVES: dice.count(5) * 5,
        SIXES: dice.count(6) * 6,
        FULL_HOUSE: full_house(dice),
        FOUR_OF_A_KIND: four_of_a_kind(dice),       
        LITTLE_STRAIGHT: little_straight(dice),
        BIG_STRAIGHT: big_straight(dice),
        CHOICE: sum(dice),
        YACHT: yacht(dice)
        }
    return categories[category]
    
def full_house(dice):
    counts = [dice.count(die) for die in range(1,6)]
    counts.sort()
    if counts == [0, 0, 0, 2, 3]:
        return sum(dice)
    else:
        return 0
        
def four_of_a_kind(dice):
    counts = [dice.count(die) for die in range(1,7)]
    counts_old = counts.copy()
    counts.sort()
    if counts == [0, 0, 0, 0, 1, 4] or counts == [0, 0, 0, 0, 0, 5]:
        return (counts_old.index(max(counts_old)) + 1) * 4
    else:
        return 0
        
def little_straight(dice):
    dice.sort()
    return 30 if dice == [1, 2, 3, 4, 5] else 0
    
def big_straight(dice):
    dice.sort()
    return 30 if dice == [2, 3, 4, 5, 6] else 0
    
def yacht(dice):
    counts = [dice.count(die) for die in range(1,6)]
    counts.sort()
    if counts == [0, 0, 0, 0, 5]:
        return 50
    else:
        return 0
        
print(score([3,3,3,3,3], FOUR_OF_A_KIND))