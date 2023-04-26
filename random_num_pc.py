import random

def random_number_pc(a, b):
     
    number = random.randint(a, b)

    while True:
        guess = int(input("Guess a number: "))
        if guess > number:
            print("Wrong number. Try lower")
            continue
        elif guess < number:
            print("Wrong number. Try higher")
            continue
        elif guess == number:
            break
    print("You got it!")

random_number_pc(1, 1000)