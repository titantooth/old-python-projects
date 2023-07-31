import random

secret_number = random.randint(1,1000)

print('pick a number between 1 to 1000 and i\' try to guess what it is!!!')
user_choice = input('type secret:')

min = 1
max = 1000
guess = 500
diff= abs(guess - int(user_choice))
while guess != int(user_choice):
    print(f'is your number higher or lower than {guess}')
    y_n = input('h or l')
    if y_n == 'h':
        min = guess
        guess = round((min + max)/2)

    elif y_n == 'l':
        max = guess
        guess = round((min + max)/2)

print(f"{guess} is your number")


