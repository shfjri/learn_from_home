from random import choice

author = 'shfjri'

def main():
    print('This game was built by {}\n'.format(author))

    number = [i for i in range(0,11)]
    answer = choice(number)

    chance = 5

    print('Welcome to the game!')


    while chance > 0:
        print('You have {} chances to guess a number from 0-10'.format(chance))
        guess = input('Choose a number from 0-10. Enter your guess: ')
        print()

        try:
            guess = int(guess)
            if type(guess) == int:
                if guess == answer:
                    print('Congrats! You guess the number')
                    print('The number is {}'.format(answer))
                    print('Thank you for playing')
                    break

                elif guess > answer:
                    print('Your guess is higher than the answer.')
                elif guess < answer:
                    print('Your guess is lower than the answer')

        except:
            print('You have to choose a number, not alphabet')
            chance += 1
        chance -= 1

    else:
        print('Sorry, you failed guess the number')
        print('The number is {}'.format(answer))
        print()

main()
