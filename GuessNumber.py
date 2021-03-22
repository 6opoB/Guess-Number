import random

print('Enter the range in which the computer will guess the number :')
a, b, number = int(input()), int(input()), 0
x = random.randint(a, b)
print('Now try to guess the number between', a, 'and', b, ':')
while number != x:
    number = int(input())
    if number < x:
        print('Too low, mate! Try again:')
    elif number > x:
        print('Wow, too much! Try once more:')
print('Hurray! You did it! You are a seer!')
