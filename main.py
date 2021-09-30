# practicepython.org Exercise 16: Password generator
# Write a password generator in Python - use a mix of lowercase, uppercase, numbers, and symbols.
# The password generator needs to generate a new password every time the user asks for one.

import random
import string


def password_generator():
    password = []
    random_char_list = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+', '=']
    random_word_list = ['password', 'changeme', 'passwordpassword', '123456', '123456789', '12345678secret',
                        'Qwerty1', 'Password1', 'Abc123', '111111', '123123',
                        'Password123', '1asdasdasd']
    strength = input('Do you need a strong, medium, or weak password? ').lower()
    if strength == 'strong':
        count = 0
        while count < 12:
            count = count + 1
            chance_char = random.randint(0, 10)
            if chance_char < 5:
                password_1 = list((random.choice(string.ascii_letters)))
                password = password + password_1
            elif 5 < chance_char < 9:
                password_2 = list(str((random.randint(0, 9))))
                password = password + password_2
            else:
                r = list(random.choice(random_char_list))
                password = password + r
        password[:] = [' '.join(password[:])]
        print(password[0])
    elif strength == 'medium':
        count = 0
        while count < 10:
            count = count + 1
            chance_char = random.randint(0, 10)
            if chance_char < 8:
                password_1 = list((random.choice(string.ascii_letters)))
                password = password + password_1
            elif 8 < chance_char < 10:
                password_2 = list(str((random.randint(0, 9))))
                password = password + password_2
        password[:] = [' '.join(password[:])]
        print(password[0])
    elif strength == 'weak':
        password = random_word_list[random.randint(0, 12)]
        print(password)
    else:
        print('NO PASSWORD FOR YOU!!!')
        print('Please state a correct strength next time! ')
    return


x = input('Do you need a password? ').lower()
while x == 'yes':
    password_generator()
    x = input('Do you need another password? ').lower()
else:
    print('Have a great day!')
