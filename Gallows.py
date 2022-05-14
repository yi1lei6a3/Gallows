import random

some_words = ['яблоко', 'арбуз', 'банан', 'манго', 'клубника', 'апельсин', 'виноград', 'ананс', 'персик', 'лимон',
              'кокос']

word = random.choice(some_words)

# print(word)

print('Угадай слово! В игре учавствуют:')
print(f'{some_words}')

chances = len(word) + 2

letters_guessed = ['_'] * len(word)
for letter in letters_guessed:
    print(letter, end=' ')
print()

while letters_guessed != list(word) and chances > 0:
    guess = input('введите букву: ')

    chances = chances - 1

    if not guess.isalpha():
        print('Можно вводить только буквы!')
        print('\n Осталось', chances, 'попыток')
        continue
    elif len(guess) > 1:
        print('Ввести можно только 1 букву!')
        print('\n Осталось', chances, 'попыток')
        continue
    elif guess in letters_guessed:
        print('Вы уже ввели эту букву!')
        print('\n Осталось', chances, 'попыток')
        continue

    if guess in word:
        print('Буква угадана!')
        chances = chances + 1
        for index, letter in enumerate(word):
            if letter == guess:
                letters_guessed[index] = letter
        for letter in letters_guessed:
            print(letter, end=' ')

    else:
        print('Буква не угадана!')

    print('\n Осталось', chances, 'попыток')

if chances == 0 and letters_guessed != list(word):
    print('Попытки закончились! Вы проиграли!')
else:
    print('Вы победили!')