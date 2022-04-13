import numpy as np

number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number in range 1 to 100: '))
    if predict_number < number:
        print ('Number should be bigger')
    
    elif predict_number > number:
        print('Number should be less')
    else:
        print("You've guess the number")
        break
