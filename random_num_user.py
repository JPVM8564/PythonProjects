import random

def random_number_user(x):
    
    low = 1
    high = x
    answer = ''
    while answer != 'c' and low != high:
        guess = random.randint(low, high)
        answer = input((f"Is {guess} too low (l), too high (h), or correct? : ").lower())
        if answer == "l":
            low = guess + 1
        elif answer == "h":
            high = guess - 1
    print(f"Got it! Your number is {guess}")


random_number_user(1000)
