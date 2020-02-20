# a. prompt the user for a day of the week, print out whether the day is Monday or not
user_day_of_week = input("Enter the day of the week: ")

if user_day_of_week in ("Monday", "monday", "Mon."):
    print("That is Monday")
else:
    print("That is not Monday")

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
if user_day_of_week.lower().strip() in ("monday", "mon", "tuesday", "tues", "wednesday", "wed", "thursday", "thurs", "friday", "fri"):
    print("and it is a weekday")
elif user_day_of_week.lower().strip() in ("saturday", "sat", "sunday", "sun"):
    print("and it is a weekend")

# create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
hours_worked = 60
hourly_rate = 13.38
total_paycheck = None

# write the python code that calculates the weekly paycheck. You get paid time and a half
# if you work more than 40 hours
if hours_worked > 40:
    reg_time = 40
    overtime = hours_worked - 40
    total_paycheck = round((reg_time * hourly_rate) + (overtime * (1.5 * hourly_rate)), 2)
else:
    total_paycheck = round((hours_worked * hourly_rate), 2)
print("Total Paycheck:", total_paycheck)

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i < 16:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each
# number with a new line.
i = 0
while i < 101:
    print(i, "\n")
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i > -11:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i **= 2

# Write a loop that uses print to create the output shown below.
i = 100
while i > 5:
    print(i)
    i -= 5

# Write some code that prompts the user for a number, then shows a multiplication table up
# through 10 for that number.
user_mul_request = input("Please enter a number to see multiples: ")

for n in range(1, 11):
    print(user_mul_request, "x", n, "=", n * int(user_mul_request))

# Create a for loop that uses print to create the output shown below.
for i in range(1, 10):
    print(str(i) * i)

# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to
# continue prompting the user if they enter invalid input. (Hint: use the isdigit method
# on strings to determine this). Use a loop and the continue statement to output all the
# odd numbers between 1 and 50, except for the number the user entered.
user_odd_num = 0

while True:
    user_odd_num = input("Input odd number between 1 and 50: ")

    if not user_odd_num.isdigit():
        continue
    elif 50 < int(user_odd_num) or 1 > int(user_odd_num) or int(user_odd_num) % 2 == 0:
        continue
    else:
        break

for n in range(1, 51):
    if n == int(user_odd_num):
        print("Yikes! Skipping number:", n)
    elif n % 2 == 0:
        continue
    else:
        print("Here is an odd number:", n)

# The input function can be used to prompt for input and use that input in your python 
# code. Prompt the user to enter a positive number and write a loop that counts from 0 to 
# that number. (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a 
# numeric type.)

user_count_request = 0

while True:
    user_count_request = input("Enter a positive number: ")
    
    if not user_count_request.isdigit():
        continue

    user_count_request = int(user_count_request)

    if user_count_request < 1:
        continue
    else:
        break

for n in range(1, (user_count_request + 1)):
    print(n)

# Write a program that prompts the user for a positive integer. Next write a loop that
# prints out the numbers from the number the user entered down to 1.
user_countdown_request = 0

while True:
    user_countdown_request = input("Enter positive number: ")

    if not user_countdown_request.isdigit():
        continue
    
    user_countdown_request = int(user_countdown_request)

    if user_countdown_request < 1:
        continue
    else:
        break

for n in range(user_countdown_request, 0, -1):
    print(n)

# One of the most common interview questions for entry-level programmers is the FizzBuzz
# test. Developed by Imran Ghory, the test is designed to test basic looping and
# conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
while True:
    user_power_request = 0

    while True:
        user_power_request = input("What number would you like to go up to? ")

        if not user_power_request.isdigit():
            continue
        
        user_power_request = int(user_power_request)
        break

    print("number | squared | cubed ")
    print("------ | ------- | ------ ")

    for n in range(1, user_power_request + 1):
        print(("{:<7}|{:<9}|{:<8}").format(n, n ** 2, n ** 3))
    
    user_continue = input("Do you want to continue (y/n)? ")

    if user_continue.lower() == "y":
        continue
    else:
        break

#Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

while True:
    user_grade_request = int(input("Enter a numerical grade: "))

    if user_grade_request < 88:
        print("A")
    elif user_grade_request < 80:
        print("B")
    elif user_grade_request < 67

    user_continue = input("Do you want to continue? (y/n)")

    if user_continue.lower().strip() == "y":
        break
    else:
        continue