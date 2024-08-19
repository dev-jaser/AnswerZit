import string
import random  # import random module to be able to randomize password generation

# function that will generate a password taking user input for length and choice of upper/lowercase, numerical, and symbol chars then return password to user


def generatePassword(length, uppercase, lowercase, numeric, symbol):
    chars = ''
    if uppercase == 1:
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        uppercase = 0
    if lowercase == 1:
        chars += 'abcdefghijklmnopqrstuvwxyz'
    else:
        lowercase = 0
    if numeric == 1:
        chars += '0123456789'
    else:
        numeric = 0
    if symbol == 1:
        chars += r'!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

    new_password = ''  # initialize empty string that will hold the randomly generated password
    # loop through the chars for the user specified number of times: append a new char each time to the new_password variable
    for _ in range(length):
        random_char = random.choice(chars)
        new_password += random_char

    return new_password


def main():

    print("Answerzit Password Generator")

    while True:  # Create a loop to ensure user selects a length within range 3 - 18;
        # prompt user pick a number which = LENGTH of generated password
        length_response = int(
            input('How long do you want your password to be? MIN = 3  MAX = 18 '))
        # if user picked out of range: warn user and and prompt for new number
        if length_response not in range(3, 19):
            print('WARNING: You selected a length out of range! Try Again!')
        else:
            break

    while True:
        while True:
            uppercase_response = int(
                input('Do you want to include UPPERCASE characters? (1 = YES, 0 = NO)'))
            # if user picked out of range: warn user and and prompt for new number
            if uppercase_response not in range(0, 2):
                print(
                    'WARNING: You must select either 1: \'YES\' or 0: \'NO\'! Try Again!')
            else:
                break
        while True:
            lowercase_response = int(
                input('Do you want to include LOWERCASE characters? (1 = YES, 0 = NO)'))
            # if user picked out of range: warn user and and prompt for new number
            if lowercase_response not in range(0, 2):
                print(
                    'WARNING: You must select either 1: \'YES\' or 0: \'NO\'! Try Again!')
            else:
                break
        while True:
            numeric_response = int(
                input('Do you want to include NUMERIC characters? (1 = YES, 0 = NO)'))
            # if user picked out of range: warn user and and prompt for new number
            if numeric_response not in range(0, 2):
                print(
                    'WARNING: You must select either 1: \'YES\' or 0: \'NO\'! Try Again!')
            else:
                break
        while True:
            symbol_response = int(
                input('Do you want to include SYMBOL characters? (1 = YES, 0 = NO)'))
            # if user picked out of range: warn user and prompt for new number
            if symbol_response not in range(0, 2):
                print(
                    'WARNING: You must select either 1: \'YES\' or 0: \'NO\'! Try Again!')
            else:
                break
        break

    new_password = generatePassword(
        length_response, uppercase_response, lowercase_response, numeric_response, symbol_response)
    print(f'Your Generated Password: {new_password}')
 # Final display of password, returns to menu there-after.
    return


if __name__ == "__main__":
    main()
