from random import randrange
from time import time
done1 = True
game_number = 0
print()
print('                  >>>>>>>>>>>  Number Guessing Game  <<<<<<<<<<<')
print()
print()
while done1 :
    done2 = True
    done4 = True
    random_number1 = randrange(1,10)
    random_number2 = random_number1 * 10
    random_number3 = random_number2 + 11
    random_number4 = randrange(random_number2,random_number3)
    attempt = 0
    while done2 :
        attempt = attempt + 1
        if attempt == 1 :
            game_number = game_number + 1
            print('+------------------------------------------------------------------------+')
            print('                            >> Game Number : ',game_number,'<<')
            print()
            print('* Guess a number between',random_number2,'and',(random_number3 - 1),'-:')
            start_time = time()
        if attempt <= 6 :
            print('Attempt',attempt,end='')
            user_guess = eval(input(' : '))
        if user_guess == random_number4 and attempt <= 6 :
            end_time = time()
            print()
            print('                            >> correct Guess ! <<')
            print()
            print('* Total Attempt/s taken : ',attempt,', Time taken : ',int(end_time - start_time),'Seconds')
            print()
            print('+------------------------------------------------------------------------+')
            done2 = False
        if user_guess != random_number4 and attempt <= 5 :
            print()
            print('* Incorrect Guess ! Try Again')
        if attempt > 6 :
            print()
            print('                       >> Too many wrong Attempts ! <<')
            print('* Number was : ',random_number4)
            print()
            print('+------------------------------------------------------------------------+')
            done2 = False
    while done4 :
        print()
        user_input = input('>> Press P to Play Again ! or Press E to Exit : ')
        if user_input == 'p' or user_input == 'P' :
            done4 = False
            print()
        elif user_input == 'e' or user_input == 'E' :
            done4 = False
            done1 = False
            print()
        else :
            print()
            print('                             >> Wrong Input ! <<')
