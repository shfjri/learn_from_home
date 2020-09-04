from random import choice

author = 'shfjri'

def asks_user(): # function to asks user, want to play again or exit from the game
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
            asks_user() # asks user again, want to play again or exit from the game
    else:  # if user input a number or symbol
        print('\nYou have to choose a letter in option, not number or symbols')
        asks_user() # asks user again, want to play again or exit from the game

def main(): # the games
    print('This game was built by {}\n'.format(author))

    answer = choice([i for i in range(0,11)]) # choose a random number from 0-10

    chance = 3 # chances to guess the number

    print('Welcome to the game!')

    while chance > 0: # if you still have a chances
        print('You have {} chances'.format(chance))
        guess = input('Choose a number from 0-10. Enter your guess: ') # asks the user to enter their guess number
        print()

        try: # do a try
            guess = int(guess) # convert string to integer
            if type(guess) == int:
                if guess == answer: # if user input the correct number
                    print('Congrats! You guessed the number correctly')
                    print('The number is {}'.format(answer))
                    break # exit from while loop

                elif guess > answer: # if user input larger number than the answer
                    print('Your guess is higher than the answer\n')
                elif guess < answer: # if user input smaller number than the answer
                    print('Your guess is lower than the answer\n')

        except: # if failed to try convert string to integer
            print('You have to choose a number, not alphabet or symbol\n')
            chance += 1 # it used in order makes chances not changed
        chance -= 1

    else: # if user have no chances again
        print('Sorry, you failed guess the number')
        print('The number is {}'.format(answer)) # tell user the answer

    asks_user()

main()
