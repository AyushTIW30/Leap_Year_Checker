# Leap Year Checker

This Python program checks whether a given year is a leap year or not. It uses the standard leap year rules to determine the result and provides a user-friendly interface with clear feedback.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [Explanation](#explanation)

## Features

- **Interactive User Interface**: The program prompts the user to input a year and provides immediate feedback about whether it's a leap year.
- **Valid Input Handling**: It checks for valid, positive integer input and handles errors gracefully.
- **Formatted Output**: The results are displayed with emojis and well-organized text to make the experience more enjoyable.
- **Modular Code**: The code is organized into functions for easier readability, maintainability, and reuse.

## How to Use

1. **Clone or Download the Repository**:
   - Clone the repository with the following command:
     ```bash
     git clone https://github.com/AyushTIW30/Leap_Year_Checker/blob/main/Leap_Year.py
     ```
   - Or download it as a ZIP file and extract it.

2. **Run the Program**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the `leap_year_checker.py` file.
   - Run the program using Python:
     ```bash
     python Leap_Year.py
     ```

3. **Input a Year**:
   - The program will prompt you to enter a year to check whether it is a leap year or not.
   - Type the year and hit Enter.
   - The program will then display the result with a friendly message.

4. **Exit the Program**:
   - After displaying the result, the program will thank you and end.

## Explanation

### Leap Year Rules
A year is considered a **leap year** if:

- It is divisible by 4.
- It is **not** divisible by 100, unless it is also divisible by 400.

For example:
- The year **2000** is a leap year (divisible by 400).
- The year **1900** is **not** a leap year (divisible by 100, but not by 400).
- The year **2020** is a leap year (divisible by 4, but not divisible by 100).

### How the Code Works

1. **`is_leap_year(year)`**: This function takes the input year and checks if it follows the leap year rules.
2. **`get_user_input()`**: This function handles the user input, ensuring it's a valid positive integer.
3. **`display_result(year, leap_status)`**: This function formats and displays the result to the user with appropriate emojis and messages.
4. **`main()`**: This function ties everything together: it gets the user input, checks if the year is a leap year, and displays the result.



