author = 'shfjri'


def asks_help_again(): # function to asks user, need more help or exit


    play = input('\nNeed more help? [y/n] ')  # asks user, need more help or exit

    if play.isalpha() == True:  # if user input a letter
        play = play.lower()  # convert letter to lowercase
        if play == 'y':  # if user need more help
            print()
            main()  # run the game again
        elif play == 'n':  # if user want to exit
            print('\nThank you for asking me.')
            print('Have a nice day')
        else:  # if user's input not in the option
            print('\nPlease choose one from the option.')
            asks_help_again() # asks user again, need more help or exit
    else:  # if user input a number or symbol
        print('\nYou have to choose a letter in option, not number or symbols')
        asks_help_again() # asks user again, need more help or exit

    return play


def kinetic():

    try:
        print('\nKinetic Energy Calculator')
        m = float(input('Input the mass in kg: ')) # asks user to input value of mass in kg
        v = float(input('Input the velocity in m/s: ')) # asks user to input value of velocity in m/s
        K = (1/2) * m * (v**2) # calculate the value of kinetic energy
        print('Kinetic energy of a {} kg mass with {} m/s velocity is {} J'.format(m,v,K)) # print the result
    except:
        print('\nYou have to input a number\n')
        kinetic()
    return K


def potential():

    try:
        print('\nPotential Energy Calulator')
        m = float(input('Input the mass: ')) # asks user to input value of mass in kg
        g = float(input('Input the gravity acceleration: ')) # asks user to input value of graviticy acceleration
        h = float(input('Input the altitude in meter: ')) # asks user to input value of altitude in m
        V = m * g * h # calculate the value of potential energy
        print('Potential energy of a {} kg object at {} m altitude is {} J'.format(m, h, V)) # print the result
    except:
        print('\nYou have to input a number\n')
        potential()

    return V


def choice():


    user_choice = input('''What do you want to calculate?
    a. Potential Energy
    b. Kinetic Energy\n''') # asks user, what they need a help to, calculate kinetic or potential energy

    if user_choice.isalpha() == True: # check user's input, alphabet or others
        if user_choice.lower() == 'a': # if user need a help to calculate potential energy
            potential()
        elif user_choice.lower() == 'b': # if user need help to calculate kinetic energy
            kinetic()
        else:
            print('You have to choose one of the option') # if user's input is not in the option
            choice() # asks user again
    else:
        print('Your input is not alphabet') # if user's input not alphabet
        choice() # asks user again

    return user_choice


def main():


    print('Welcome to mechanical energy calculator')
    print('It was made by {}'.format(author))

    choice() # call the choice function
    asks_help_again() # call help function

    return None

main()