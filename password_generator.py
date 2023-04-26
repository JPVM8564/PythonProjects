import random

print('PASSWORD GENERATOR')

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&^*'
num = int(input('How many passwords would you like? '))
lenght = int(input('How long would you like the passwords to be? '))

print('Here are your passwords: ')

for pwd in range(num): #remember to use range
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(characters)
    print(passwords)