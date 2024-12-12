def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_user_input():

    while True:
        try:
            year = int(input("Please enter the year you want to check: "))
            if year > 0:
                return year
            else:
                print("Please enter a valid year (positive number).")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def display_result(year, leap_status):

    if leap_status:
        print(f"✨ {year} is a Leap Year! ✨")
    else:
        print(f"❌ {year} is NOT a Leap Year. ❌")

def main():
    print("Welcome to the Leap Year Checker! 🎉")
    print("-" * 40)

    year = get_user_input()
    leap_status = is_leap_year(year)
    display_result(year, leap_status)

    print("-" * 40)
    print("Thank you for using the Leap Year Checker! 👋")


if __name__ == "__main__":
    main()
