from english_words import english_words_lower_alpha_set as words_set
import random


def print_list_char(listo, type):
    if type == 0:
        if len(listo) == 0:
            print('There are no characters')
            return

        show = ""
        for character in listo:
            show += character
    else:
        show = "Letters: "
        for character in listo:
            show += character + ' '

    print(show)


def print_word(word, letters):
    slashes = ['']*len(word)
    indexes = []

    for letter in letters:
        if word.count(letter) > 0:
            pos = 0

            while pos < len(word):
                ind = word.find(letter, pos)

                if ind >= 0:
                    slashes[ind] = ' ' + letter
                    if ind == len(word) - 1:
                        slashes[ind] += ' '
                    pos = ind + 1
                    indexes.append(ind)
                else:
                    pos = len(word)

    for i in range(len(word)):
        if i not in indexes:
            slashes[i] = ' _'
            if i == len(word) - 1:
                slashes[i] += ' '

    print_list_char(slashes, 0)


def game(lives, word, count, letters, pos, drawing, rounds):
    if lives == 0:
        print('*' * 20)
        print('Game over. You lost in ' + str(rounds) + ' rounds')
        print('The word was: ' + word)
        print('*' * 20)
        return
    elif len(word) == count:
        print('*' * 20)
        print('You won! Discovered the word in ' + str(rounds) + ' rounds')
        print('*' * 20)
        return
    else:
        letter = input('Input a letter: ')

        if len(letter) != 1:
            print(drawing[pos])
            print_word(word, letters)
            print_list_char(letters, 1)
            print('Enter a letter!')
            game(lives, word, count, letters, pos, drawing, rounds)
        else:
            if letter in letters:
                print('Letter already said')
                game(lives, word, count, letters, pos, drawing, rounds)
            else:
                letters.append(letter)

                if letter in word:
                    amount = count + word.count(letter)

                    print(drawing[pos])
                    print_word(word, letters)
                    print_list_char(letters, 1)

                    game(lives, word, amount, letters, pos, drawing, rounds+1)
                else:
                    lives -= 1
                    pos += 1

                    print(drawing[pos])
                    print_word(word, letters)
                    print_list_char(letters, 1)

                    game(lives, word, count, letters, pos, drawing, rounds+1)


words = list(words_set)
word = words[random.randint(0, len(words)-1)]

lives = 9
drawing = ['          \n          \n          \n          \n          ',
           '          \n          \n          \n          \n---       ',
           ' |        \n |        \n |        \n |        \n---       ',
           ' |-----|  \n |        \n |        \n |        \n---       ',
           ' |-----|  \n |     O  \n |        \n |        \n---       ',
           ' |-----|  \n |     O  \n |     |  \n |        \n---       ',
           ' |-----|  \n |     O  \n |     |  \n |    /   \n---       ',
           ' |-----|  \n |     O  \n |     |  \n |    / | \n---       ',
           ' |-----|  \n |   __O  \n |     |  \n |    / | \n---       ',
           ' |-----|  \n |   __O__\n |     |  \n |    / | \n---       ']

print_word(word, [])
game(lives, word, 0, [], 0, drawing, 0)