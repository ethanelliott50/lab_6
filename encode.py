'''
Lab 6
Authors: Ethan Elliott and Adi Chauhan
Class: COP3502C
Section: 22282
Description: Password encoder and decoder
'''

# Encodes password by adding 3 to each digit
def encode(password):

    encoded_password = ''

    for i in password:

        digit = str(int(i) + 3)
        if int(digit) >= 10:
            digit = digit[1]
        encoded_password += digit

    return encoded_password

if __name__ == "__main__":
    while True:
            # Prints menu
            print('Menu')
            print('-------------')
            print('1. Encode')
            print('2. Decode')
            print('3. Quit')
            print()
            option = int(input("Please enter an option: "))

            # Encoding option
            if option == 1:
                encoded_password = encode(input("Please enter your password to encode: "))
                print('Your password has been encoded and stored!')
            # Decoding option
            elif option == 2:
                decoded_password = decode(encoded_password)
                print('The encoded password is ', encoded_password, 'and the original password is ', decoded_password)
            elif option == 3:
                break
