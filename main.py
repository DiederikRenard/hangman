from random import choice


def random_word():
    with open('hangman_wordlist.txt') as file:
        contents = file.readlines()
        return choice(contents)


hangman = [
        f"""_______
|      |
|      
|
|       
|      
|-------|""",
        f"""_______
|      |
|      o
|
|       
|      
|-------|""",
        f"""_______
|      |
|      o
|      |
|
|      
|-------|""",
        f"""_______
|      |
|      o
|     /|
|
|      
|-------|""",
        f"""_______
|      |
|      o
|     /|l
|
|      
|-------|""",
        f"""_______
|      |
|      o
|     /|l
|     /
|
|-------|""",
        f"""_______
|      |
|      o
|     /|l
|     / l
|
|-------|""",


    ]


def run_game():
    word = random_word().strip()
    letters_in_word: list = ['_' for letter in word]

    # print(word)
    print(hangman[0])

    lives = 6

    wanna_play = True

    while wanna_play:
        print(*letters_in_word)

        user_guess: str = input('Guess a letter: ')
        try:

            if user_guess in word:
                for num in range(len(letters_in_word)):
                    if word[num] == user_guess:
                        letters_in_word[num] = user_guess
                if '_' not in letters_in_word:
                    print(f'You won! the word was: {word}')
                    continue_playing = input('Want to play again? Y/N: ').lower()
                    if continue_playing != 'y':
                        wanna_play = False
                        print('Thanks for playing!')
                        return
                    else:
                        run_game()
            else:
                lives -= 1
                if lives <= 0:
                    print(hangman[-1])
                    print('You have lose all your lives, GAME OVER!')
                    continue_playing = input('Want to play again? Y/N: ').lower()
                    if continue_playing != 'y':
                        wanna_play = False
                        print('Thanks for playing!')
                        return
                    else:
                        run_game()
                print(f'Wrong guess, you have {lives} lives left.')
                print(hangman[6 - lives])

        except ValueError:
            print('Please enter a correct letter.')


if __name__ == '__main__':
    run_game()
