import random


uppercaseletter1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_letter1 = random.choice(uppercaseletter1)
print(f'your first uppercase letter is : {random_letter1}')

uppercaseletter2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random_letter2 = random.choice(uppercaseletter2)
print(f'your second uppercase letter is : {random_letter2}')

lowercaseletter1 = 'abcdefghijklmnopqrstuvwxyz'
random_letter3 = random.choice(lowercaseletter1)
print(f'your first uppercase letter is : {random_letter3}')

lowercaseletter2 = 'abcdefghijklmnopqrstuvwxyz'
random_letter4 = random.choice(lowercaseletter2)
print(f'your second uppercase letter is : {random_letter4}')

digit1 = '0123456789'
random_letter5 = random.choice(digit1)
print(f'your first digit is: {random_letter5}')

digit2 = '0123456789'
random_letter6 = random.choice(digit2)
print(f'your second digit is: {random_letter6}')

punctuationsign1 = "?*!@&$%£-'."
random_letter7 = random.choice(punctuationsign1)
print(f'your first random punction is: {random_letter7}')

punctuationsign2 = "?*!@&$%£-'."
random_letter8 = random.choice(punctuationsign2)
print(f'your second random punctuation sign: {random_letter8}')

password =(random_letter2+random_letter1+random_letter3+random_letter4+random_letter5+random_letter6+random_letter7+random_letter8)

password_list = list(password)
random.shuffle(password_list)
password_str = ''.join(password_list)

print( password_str)
