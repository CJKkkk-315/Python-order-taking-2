"""
Wordle
Assignment 1
Semester 1, 2022
CSSE1001/CSSE7030
"""

from string import ascii_lowercase
from typing import Optional

from a1_support import (
    load_words,
    choose_word,
    VOCAB_FILE,
    ANSWERS_FILE,
    CORRECT,
    MISPLACED,
    INCORRECT,
    UNSEEN,
)


# Replace these <strings> with your name, student number and email address.
__author__ = "<Your Name>, <Your Student Number>"
__email__ = "<Your Student Email>"


# Add your functions here

def main():
    gamelost = 0
    winres = [0 for _ in range(6)]
    while True:
        bflag = 0
        guesses = []
        table = [' ' for i in range(26)]
        words = load_words('answers.txt')
        answer = choose_word(words)
        t1 = 1
        while True:
            if bflag:
                break
            guess = input('Enter guess {}: '.format(str(t1)))
            if guess == 'k':
                print('Keyboard information')
                print('------------')
                for i in range(0,len(table),2):
                    print(chr(i+97)+': ' + table[i],end='	')
                    print(chr(i+1+97)+': ' + table[i+1])
                continue
            t1 += 1
            guesses.append(guess)
            t2 = 1
            for guess in guesses:
                rof = ''
                for i,j in zip(guess,answer):
                    if i != j and i in answer:
                        rof += MISPLACED
                        if table[ord(i)-97] == ' ' or table[ord(i)-97] == INCORRECT:
                            table[ord(i) - 97] = MISPLACED
                    elif i == j:
                        rof += CORRECT
                        table[ord(i) - 97] = CORRECT
                    else:
                        rof += INCORRECT
                        if table[ord(i) - 97] == ' ':
                            table[ord(i) - 97] = INCORRECT
                print('Guess {}: '.format(str(t2)) + ' '.join(list(guess)))
                print('         ' + rof)
                print('---------------')
                if rof == CORRECT*6:
                    print('Correct! You won in {} guesses!'.format(t2))
                    winres[t2-1] += 1
                    bflag = 1
                t2 += 1
                if t2 > 6:
                    print('You lose! The answer was: {}'.format(answer))
                    gamelost += 1
                    bflag = 1
        for i in range(len(winres)):
            print('{} moves: '.format(i + 1) + str(winres[i]))
        print('Games lost: {}'.format(str(gamelost)))
        c = input('Would you like to play again (y/n)?')
        if c == 'y':
            pass
        else :
            break





if __name__ == "__main__":
    main()
