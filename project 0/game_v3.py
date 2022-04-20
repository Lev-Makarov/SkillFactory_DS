import numpy as np

global_low_border = 1   #prepared for changes, can be wider range to run the game
global_high_border = 100  #prepared for changes, can be wider range to run the game


def guess_function (number: int=1, low_border: int=global_low_border, high_border: int = global_high_border+1)->int:
    """ Algorythm takes half of high and low borders, compares with initial number 
        if middle number less than initial number it becomes low border
        if middle number greater than initial number it becomes high border
        initial low border = 1
        initial high border = 100
    
    Args: 
        int: initial number, 1 by default
        int: initial low_border, 1 by default
        int: initial high_border, 100 by default
    
    returns:
        int: number of tries
    """
    count = 0
    predict_number = 0

    while True:
        count+=1
        predict_number = (high_border-low_border)//2+low_border
        if number == predict_number:
            break
        elif predict_number > number:
            high_border = predict_number
        else:
            low_border = predict_number
    return(count)

def score_game (guess_function, low_border = global_low_border, high_border = global_high_border) -> int:
    """ 1000 times executes the guess function to count mean tries to guess the number

    Args:
      guess_function([type])

    returns:
        int: mean number of tries
    
    """
    
    count_ls = []
    np.random.seed(2)
    random_array = np.random.randint(low_border,high_border+1, size =1000) 

    for number in random_array:
        count_ls.append(guess_function(number))
    

    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number in {score} tries')
    return (score)

if __name__ == '__main__':
    score_game(guess_function)
