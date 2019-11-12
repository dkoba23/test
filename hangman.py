


def hangman(word):
    wrong = 0
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|"
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcom to  Hangman')

    while wrong < len(stages) - 1:
        guess = input('please enter one one word: ')
        if guess in rletters:
            index = rletters.index(guess)
            board[index] = guess
            rletters[index] = '$'
            print('you are correct')
        else:
            wrong += 1
            print('you are wrong')
        print(''.join(board))
        print('\n'.join(stages[0:wrong+1]))
        if '_' not in board:
            print('You win')
            print(''.join(board))
            win = True
            break
    if not win:
        print('You lose')
        print('The answer was {}'.format(word))




hangman('daichi')



