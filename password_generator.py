import random
print('Welcome to Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

num_passwords = int(input('Enter the amount of passwords you want to generate: '))
length = int(input('Enter the length of the password: '))
for p in range(num_passwords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

print('Thank you for using Password Generator!')