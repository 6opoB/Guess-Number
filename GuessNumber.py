import random

print('Введи диапазон, в котором компьютер загадает число:')
a, b, number = int(input()), int(input()), 0
x = random.randint(a, b)
print('А теперь попробуй угадать число между', a, 'и', b, ':')
while number != x:
    number = int(input())
    if number < x:
        print('Низко берешь, товарищь! Попробуй-ка еще:')
    elif number > x:
        print('Ого, слишком много! Ну-ка сначала:')
print('Ура! Угадал! Ты Ванга!')
