import random

pc_choices = ['rock', 'paper', 'scissors']


pc_score = 0
user_score = 0
have_winner = False

while not have_winner:
    user_choice = input('rock, paper or scissors?')
    pc_choice = pc_choices[random.randint(0, 2)]
    print(f'your choice was {user_choice}' )
    print(f'the pc choice was {pc_choice}')

    if user_choice == 'rock' and pc_choice == 'scissors':
        user_score += 1
        print('you win this round')

    elif user_choice == 'rock' and pc_choice == 'paper':
        pc_score += 1
        print('the PC wins this round')
    elif user_choice == 'scissors' and pc_choice == 'paper':
        user_score += 1
        print('you win this round')
    elif user_choice == 'scissors' and pc_choice == 'rock':
        pc_score += 1
        print('the PC wins this round')

    elif user_choice == 'paper' and pc_choice == 'rock':
        user_score += 1
        print('you win this round')
    elif user_choice == 'paper' and pc_choice == 'scissors':
        pc_score += 1
        print('the PC wins this round')
    else:
        print(f'you both drew the round with {user_choice}s')
    if user_score == 3:
        have_winner = True
    elif pc_score == 3:
        have_winner = True
    if have_winner and (pc_score == 3):
        print('the game is over the PC won!')
    elif have_winner and (user_score == 3):
        print('the game is over congrats you won!')
    print((user_score,pc_score))





