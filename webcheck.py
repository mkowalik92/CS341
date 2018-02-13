# Marek Kowalik
# 31010270
# mk343@njit.edu

low_letters = "abcdefghijklmnopqrstuvwxyz"
low_letters_no_w = "abcdefghijklmnopqrstuvxyz"
low_letters_no_c = "abdefghijklmnopqrstuvwxyz"
low_letters_no_m = "abcdefghijklnopqrstuvwxyz"
low_letters_no_o = "abcdefghijklmnpqrstuvwxyz"

def print_intro():
    print("\nProject 1 for CS 341\nWritten by: Marek Kowalik, 31010270\nInstructor: Marvin Nakayama, marvin@njit.edu\n")

def parse_url(url_string):
    state = 1
    trap = 0
    print("Start State: q" + str(state))
    for letter in url_string:
        # State 1
        if (state == 1) and (letter == "w") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        if (state == 1) and (letter in low_letters_no_w) and (trap == 0):
            state = 6
            print(letter + " q" + str(state))
            continue
        # State 2
        if (state == 2) and (letter == "w") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        if (state == 2) and (letter in low_letters_no_w) and (trap == 0):
            state = 6
            print(letter + " q" + str(state))
            continue
        # State 3
        if (state == 3) and (letter == "w") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        if (state == 3) and (letter in low_letters_no_w) and (trap == 0):
            state = 6
            print(letter + " q" + str(state))
            continue
        # State 4
        if (state == 4) and (letter == ".") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        if (state == 4) and (letter in low_letters) and (trap == 0):
            state = 6
            print(letter + " q" + str(state))
            continue
        # State 5
        if (state == 5) and (letter == "c") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        if (state == 5) and (letter in low_letters_no_c) and (trap == 0):
            state = 6
            print(letter + " q" + str(state))
            continue
        # State 6
        if (state == 6) and (letter == ".") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        if (state == 6) and (letter in low_letters) and (trap == 0):
            state = 6
            print(letter + " q" + str(state))
            continue
        # State 7
        if (state == 7) and (letter == "o") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        if (state == 7) and (letter in low_letters_no_o) and (trap == 0):
            state += 3
            print(letter + " q" + str(state))
            continue
        # State 8
        if (state == 8) and (letter == "c") and (trap == 0):
            state = 16
            print(letter + " q" + str(state))
            continue
        # State 9
        if (state == 9) and (letter == ".") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        if (state == 9) and (letter == "m") and (trap == 0):
            state += 3
            print(letter + " q" + str(state))
            continue
        if (state == 9) and (letter in low_letters_no_m) and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        # State 10
        if (state == 10) and (letter in low_letters) and (trap == 0):
            state = 10
            print(letter + " q" + str(state))
            continue
        if (state == 10) and (letter == ".") and (trap == 0):
            state = 8
            print(letter + " q" + str(state))
            continue
        # State 11
        if (state == 11) and (letter == "c") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        # State 12
        if (state == 12) and (letter == ".") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        if (state == 12) and (letter in low_letters) and (trap == 0):
            state = 10
            print(letter + " q" + str(state))
            continue
        # State 13
        if (state == 13) and (letter == "o") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        # State 14
        if (state == 14) and (letter == "c") and (trap == 0):
            state += 2
            print(letter + " q" + str(state))
            continue
        # State 15
        if (state == 15) and (letter == "m") and (trap == 0):
            state += 3
            print(letter + " q" + str(state))
            continue
        # State 16
        if (state == 16) and (letter == "o") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        # State 17
        if (state == 17) and (letter == "m") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        # State 18
        if (state == 18) and (letter == ".") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        # State 19
        if (state == 19) and (letter == "c") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        # State 20
        if (state == 20) and (letter == "o") and (trap == 0):
            state += 1
            print(letter + " q" + str(state))
            continue
        # State Trap
        else:
            trap = 1
            print("letter: " + letter + " state: q" + str(state) + " TRAP")
            continue
    if (trap == 0):
        print("The string \"" + url_string + "\" has been ACCEPTED!")
    else:
        print("The string \"" + url_string + "\" has been REJECTED!")

def main():
    print_intro()
    running = True

    while (running):
        check = input("Would you like to enter a string?\n")
        if (check == "n"):
            running = False
            break
        elif (check == "y"):
            input_string = input("Please enter a string: \n")
            print("The string that was entered is: " + input_string)
            parse_url(input_string)
            continue
        else:
            print("unknown input")
            running = False
            break

if __name__ == "__main__": main()
