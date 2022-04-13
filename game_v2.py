# Computer guesses the number

import numpy as np
def random_predict(number:int=1)->int:
    """ random guessing numbers

    Args:
       number(int, optional): defaults = 1
    
    Returns:
        int: number of tries
    """

    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return(count)

def score_game (random_predict) -> int:
    """ 1000 times to count mean tries to guess the number

    Args:
      random_predict([type])

    returns:
        int: mean number of tryes
    
    """
    
    count_ls = []
    np.random.seed(2)
    random_array = np.random.randint(1,101, size =1000) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Your algorithm guesses the number in {score} tries')
    return (score)

if __name__ == '__main__':
    score_game(random_predict)
