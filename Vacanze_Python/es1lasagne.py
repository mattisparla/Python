EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2
#       equal to the time it takes to prepare a single layer

def bake_time_remaining(tempoInForno):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-tempoInForno
    

def preparation_time_in_minutes(strati):
    """Calculate the preparation time.
 
    :param number_of_layers: int the number of lasagna layers made
    :return: int amount of prep time (in minutes), based on 2 minutes per layer added
 
    This function takes an integer representing the number of layers added to the dish,
    calculating preparation time using a time of 2 minutes per layer added.
    """
    return strati*PREPARATION_TIME


def elapsed_time_in_minutes(nStrati,tempoInForno):
    """Calculate the elapsed time.
 
    :param number_of_layers: int the number of layers in the lasagna
    :param elapsed_bake_time: int elapsed cooking time
    :return:  int total time elapsed (in in minutes) preparing and cooking
 
    This function takes two integers representing the number of lasagna layers and the         time already spent baking
     and calculates the total elapsed minutes spent cooking the lasagna.
    """
    
    prep=preparation_time_in_minutes(nStrati)
    return tempoInForno+prep
