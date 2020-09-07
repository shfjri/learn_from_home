from random import choice

author = 'shfjri'

def asks_play_again(): # function to asks user, want to play again or exit from the game


    play = input('\nWant to play again? [y/n] ')  # asks user, want to play again or exit from the game

    if play.isalpha() == True:  # if user input a letter
        play = play.lower()  # convert letter to lowercase
        if play == 'y':  # if user want to play again
            print()
            main()  # run the game again
        elif play == 'n':  # if user want to exit from the game
            print('\nThank you for playing')
        else:  # if user's input not in the option
            print('\nPlease choose one from the option.')
            asks_play_again() # asks user again, want to play again or exit from the game
    else:  # if user input a number or symbol
        print('\nYou have to choose a letter in option, not number or symbols')
        asks_play_again() # asks user again, want to play again or exit from the game

def asks_clue():


    clues = [clue for clue in (member_dict[answer])]

    asks = input('\nDo you need more clue [y/n] ? ')
    if asks.isalpha() == True:
        asks = asks.lower()
        if asks == 'y':
            print(clues[chances-1])
        elif asks == 'n':
            pass
    else:
        print('You have to choose one from the option')
        asks_clue()

    return None

def main():


    print('This game made by {}\n'.format(author))

    global chances, member_dict, answer

    chances = 3

    chika = ['mata coklat', 'next shani', 'crikaya']
    cinhap = ['psikologi', 'aurora', 'makboss']
    azizi = ['jamaah', 'tomboy', 'little monsters']
    shani = ['sempurna','center', 'jogja']
    beby = ['kapten', 'bandung', 'bytwin']
    nadila = ['akustik', 'kidal', 'groomy']
    anin = ['triple team', 'tiktok', 'mamah muda']

    member_dict = {'Chika' : chika,
                   'Cinhap' : cinhap,
                   'Azizi' : azizi,
                   'Shani' : shani,
                   'Beby' : beby,
                   'Nadila' : nadila,
                   'Anin' : anin}
    member = [key for key in member_dict.keys()]
    answer = choice(member)
    closed_answer = answer[:]

    print('Welcome to the game!')
    print('This is a game that you should guess a member in JKT48')

    new_closed_answer = ''
    for i in range(len(closed_answer)):
        new_closed_answer += closed_answer[i].replace(closed_answer[i], '*')
    print('\nThe answer is {}\n'.format(new_closed_answer))

    while chances > 0:
        print('You have {} chances to asks a clue and guess a member in JKT48'.format(chances))

        asks_clue()

        user_answer = input('\nEnter your answer: ')
        if user_answer.isalpha() == True:
            user_answer = user_answer.title()
            if user_answer == answer:
                print('\nYou won the game!')
                print('The city is {}'.format(answer))
                break
            else:
                print('\nYou enter a wrong answer')
        else:
            print('\nYou have to input a word (letter only). Not number, symbols or combination of those\n')
            chances += 1

        chances -= 1

    else:
        print('\nSorry, you failed this time')
        print('The answer is {}'.format(answer))

    asks_play_again()

main()