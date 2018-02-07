low_letters = "abcdefghijklmnopqrstuvwxyz"
low_letters_period = "abcdefghijklmnopqrstuvwxyz."
low_letters_no_w = "abcdefghijklmnopqrstuvxyz"
low_letters_no_c = "abdefghijklmnopqrstuvwxyz"
low_letters_no_m = "abcdefghijklnopqrstuvwxyz"
low_letters_no_o = "abcdefghijklmnpqrstuvwxyz"

def print_intro():
    print("\nProject 1 for CS 341\nWritten by: Marek Kowalik, 31010270\nInstructor: Marvin Nakayama, marvin@njit.edu\n")

def parse_url_fixed_again(url_string):
    done_s1 = 0
    done_s2 = 0
    done_s3 = 0
    double_com = 0
    trap = 0
    current_letter = 0
    url_length = len(url_string)
    state = 1
    previous_letter_period = 0
    period_count = 0
    print("Start State: q" + str(state))
    for letter in url_string:
        # Trap state check
        if (trap == 1):
            current_letter += 1
            print(letter + " q" + str(state) + " trap")
            continue

        # State 1
        if (state == 1) and (letter not in low_letters):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state) + " trap")
            continue
        if (state == 1) and (letter == "w") and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 1) and (letter in low_letters_no_w) and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state = 6
            done_s1 = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue

        # State 2
        if (state == 2) and (letter == "w") and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 2) and (letter not in low_letters) and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 2) and (letter in low_letters_no_w) and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue

        # State 3
        if (state == 3) and (letter == "w") and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 3) and (letter not in low_letters_period) and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        # i changed this to state = 7 instead of state = 6 and then added a done_s2 = 1
        if (state == 3) and (letter == ".") and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            previous_letter_period = 1
            period_count += 1
            state = 7
            current_letter += 1
            done_s1 = 1
            done_s2 = 1
            print(letter + " q" + str(state))
            continue

        # State 4
        if (state == 4) and (letter == ".") and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            previous_letter_period = 1
            period_count += 1
            state += 1
            current_letter += 1
            done_s1 = 1
            print(letter + " q" + str(state))
            continue
        if (state == 4) and (letter not in low_letters_period) and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 4) and (letter in low_letters) and (done_s1 == 0) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state = 6
            current_letter += 1
            done_s1 = 1
            print(letter + " q" + str(state))
            continue

        # State 5
        if (state == 5) and (letter not in low_letters) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 5) and (letter in low_letters_no_c) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 1
            previous_letter_period = 0
            current_letter += 1
            print(letter + " q" + str(state))
            continue
            ####################
        if (state == 5) and (letter == "c") and (previous_letter_period == 1) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 3
            previous_letter_period = 0
            current_letter += 1
            done_s2 = 1
            print(letter + " q" + str(state))
            continue

        # State 6
        if (state == 6) and (letter not in low_letters_period) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 6) and (letter == ".") and (previous_letter_period == 1) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            trap = 1
            period_count += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 6) and (letter in low_letters) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            current_letter += 1
            previous_letter_period = 0
            print(letter + " q" + str(state))
            continue
        if (state == 6) and (letter == ".") and (previous_letter_period == 0) and (done_s1 == 1) and (done_s2 == 0) and (done_s3 == 0) and (trap == 0):
            state += 1
            period_count += 1
            current_letter += 1
            done_s2 = 1
            print(letter + " q" + str(state))
            continue

        # State 7
        if (state == 7) and (letter != "c") and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 7) and (letter == "c") and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue

        # State 8
        if (state == 8) and (letter not in low_letters) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 8) and (letter in low_letters_no_o) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            state = 6
            current_letter += 1
            done_s2 = 0
            print(letter + " q" + str(state))
            continue
        if (state == 8) and (letter == "o") and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue

        # State 9
        # New state i just made
        if (state == 9) and (letter == "m") and (period_count == 3) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            done_s3 = 1
            state = 6
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 9) and (letter not in low_letters_period) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 9) and (letter in low_letters_no_m) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            state = 6
            current_letter += 1
            done_s2 = 0
            print(letter + " q" + str(state))
            continue
        # added this if
        if (state == 9) and (letter == "m") and (previous_letter_period == 1) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 9) and (letter == "m") and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            state += 1
            current_letter += 1
            done_s3 = 1
            print(letter + " q" + str(state))
            continue
        if (state == 9) and (letter == ".") and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 0) and (trap == 0):
            state = 7
            period_count += 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue

        # State 10

        if (state == 10) and (letter == ".") and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 1) and (trap == 0):
            state = 7
            period_count += 1
            current_letter += 1
            done_s3 = 0
            print(letter + " q" + str(state))
            continue
        if (state == 10) and (letter not in low_letters_period) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 1) and (trap == 0):
            trap = 1
            current_letter += 1
            print(letter + " q" + str(state))
            continue
        if (state == 10) and (letter in low_letters) and (done_s1 == 1) and (done_s2 == 1) and (done_s3 == 1) and (trap == 0):
            state = 6
            current_letter += 1
            done_s2 = 0
            done_s3 = 0
            print(letter + " q" + str(state))
            continue



    print("done_s1: " + str(done_s1) + "   done_s2: " + str(done_s2) + "   done_s3: " + str(done_s3) + "   period_count: " + str(period_count) + "   trap (if 1 then rejected): " + str(trap))

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
            parse_url_fixed_again(input_string)
            continue
        else:
            print("unknown input")
            running = False
            break

if __name__ == "__main__": main()
