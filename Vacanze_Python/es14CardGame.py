from statistics import mean, median
"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    list=[number,number+1,number+2]
    return list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    listaCompleta=rounds_1+rounds_2
    return listaCompleta


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    somma=0
    for n in hand:
        somma=somma+n
    return somma/len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) ==     calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = mean(hand)  #mean funzione della libreria che calcola media
    approx_average = (hand[0] + hand[-1]) / 2
    
    return average in (approx_average, median(hand)) #median funzione per la mediana


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed     card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    med = card_average(hand)
    indiceMedio = int((len(hand) - 1)/2)
    return med == hand[indiceMedio]


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if (hand[-1] == 11):
        hand[-1] = 22
    return hand
