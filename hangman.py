import random
import string

def hangman():

    words = ["committee", "quotation", "grandmother", "gesture", "donor", "spy", "goal", "smell"]

    word = random.choice(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    
    while len(word_letters) > 0 and lives > 0:
        print('Letters used: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Guess: ', ' '.join(word_list))
        print(f'Lives left: {lives}')

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else: 
                lives = lives - 1
                print('Wrong letter. You lose a life!')
        
        elif user_letter in used_letters:
            print('Letter already chosen. Try again.')

        else:
            print('Invalid character. Try again.')
    if lives == 0:
        print(f'You lost! The word was {word}')
    else:
        print(f'You won! You guessed the word {word}!')

hangman()
