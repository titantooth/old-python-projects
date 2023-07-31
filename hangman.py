import random,string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    used_letter = set()
    alphabet = set(string.ascii_uppercase)
    print(word)


    while len(word_letter) > 0:
        print('you have used these letters: ', ' '.join(used_letter))
        word_list = [letter if letter in used_letter else "-" for letter in word]
        print('the current word is:', " ".join(word_list))
        user_letter = input('please enter a letter: ').upper()

        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
        elif user_letter in used_letter:
            print('you already guessed that letter!')

        else:
            print('letter invalid')

hangman()