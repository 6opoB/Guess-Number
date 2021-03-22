import random

print('Введи диапазон, в котором компьютер загадает число/Enter the range in which the computer will guess the number :')
a, b, number = int(input()), int(input()), 0
x = random.randint(a, b)
print('А теперь попробуй угадать число между/Now try to guess the number between', a, 'и/and', b, ':')
while number != x:
    number = int(input())
    if number < x:
        print('Низко берешь, товарищ! Попробуй-ка еще/Too low, mate! Try again:')
    elif number > x:
        print('Ого, слишком много! Ну-ка сначала/Wow, too much! Try once more:')
print('Ура! Угадал! Ты Ванга!/Hurray! You did it! You're a seer!')
