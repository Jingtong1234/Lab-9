
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
            # print(encode(password))
            print("Your password has been encoded and stored!")

        elif userinput == '2':
            decode_pass == decode(password)
            print("The encoded password is and the original password is")

        elif userinput == '3':
            program_run = False



if __name__ == "__main__":
    main()
