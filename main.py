#Jevan Tenaglia
def encode(password):
    result =""
    for i in range (len(password)):
        if int(password[i])<=6:
            result += str(int(password[i]) + 3)
        elif int(password[i]) == 7:
            result += "0"
        elif int(password[i]) == 8:
            result += "1"
        elif int(password[i]) == 9:
            result += "2"
    print(f'"{password}" will become "{result}" after encoding')

def password_decoder(password):
    decoded_password = ""
    for digit in password:
        # Convert the digit to an integer, add 3, and take the remainder divided by 10
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

if __name__ == '__main__':
    password =""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        selection = int(input("Please enter an option:"))
        if selection == 1:
            password = input("Please enter your password to encode:")
            password = encode(password)
            print("Your password has been encoded and stored!")
        if selection == 2:
            decode_pass = password_decoder(password)
            print(f"The encoded password is {password}, and the original password is {decode_pass}")
        if selection == 3:
            quit()
