from random import randint

number = randint(1, 100)

print('Угадай число')

user_number = int(input())

while number != user_number:
    if user_number > number:
        print('Ваше число больше, чем загаданное')
    elif user_number < number:
        print('Ваше число меньше, чем загаданное')
    user_number = int(input())
print('Отличная интуиция! Вы угадали')