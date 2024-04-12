
# Hello

def encode(password):
    emptystring = ""
    for i in password:
        i = int(i)
        if i == 9:
            emptystring = emptystring + str(2)
        elif i == 8:
            emptystring = emptystring + str(1)
        elif i == 7:
            emptystring = emptystring + str(0)
        else:
            i += 3
            emptystring = emptystring + str(i)
    return emptystring


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        digit = int(digit)
        if digit == 0:
            digit = 7
        elif digit == 1:
            digit = 8
        elif digit == 2:
            digit = 9
        else:
            digit -= 3
        decoded_password += str(digit)
    return decoded_password



def main():
    program_run = True
    while program_run:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        userinput = input("Please enter an option: ")
        if userinput == "1":
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif userinput == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password} and the original password is {decoded_password}")

        elif userinput == '3':
            program_run = False



if __name__ == "__main__":
    main()
