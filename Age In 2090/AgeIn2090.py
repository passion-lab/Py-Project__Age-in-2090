# Practical Problem 1
# Have to take user input of either their age or year of their birth to display the year on which they will attain 100.
# Optionally, take input a particular year to display what their age will be on that year or they can exit.

curr_year = 2022
age = 10


while 1:
    age_yob = input("Enter your age or year of birth: ").strip()

    if age_yob.isnumeric():
        age_yob = int(age_yob)

        if len(str(age_yob)) <= 2:
            if age_yob == 0:
                print("You're nor birn yet!")
            elif age_yob > 100:
                print("Seems that you're the oldest person alive!")
            else:
                age = age_yob
                print(f"\nYou born in the year of {curr_year - (age_yob + 1)}")
                print(f"In the year of {curr_year + (100 - age_yob - 1)}, you'll attain 100 years old.\n")
            break

        elif len(str(age_yob)) == 4:
            if age_yob >= curr_year:
                print("You're not born yet!")
            elif age_yob < curr_year - 100:
                print("Seems that you're the oldest person alive!")
            else:
                age = curr_year - age_yob
                print(f"\nYou're {age} years old.")
                print(f"In {curr_year + (100 - age)}, you'll be 100 years old.\n")
            break

        else:
            print("You may had a wrong input. Please cross-verify your value before pressing the enter key.")
            continue

    else:
        print("Please, enter valid age or year of birth only in numeric value. Try again.")
        continue


while 1:
    is_proceed = input("Would you be like to know, how much your age will be in a particular"
                       " year?\nPress [Y]es/[N]o: ").strip()

    if is_proceed.isalpha():
        if is_proceed.lower() == "n":
            exit()
        elif is_proceed.lower() == "y":
            break
        else:
            print("Please enter valid option of either Y for yes or N for no.")
            continue

    else:
        print("Wrong input. Please enter valid option of either Y for yes or N for no.")
        continue

while 1:
    year = input("Please enter the year you wish to know your age for: ").strip()

    if year.isnumeric():
        if len(year) == 4:
            print(f"In {year}, your age will be {(int(year) - curr_year) + age} years.")
            break

        else:
            print("Please enter a valid four digit numeric year.")
            continue

    else:
        print("Wrong input. Please enter a valid four digit numeric year.")
        continue


