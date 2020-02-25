# Import and test 3 of the functions from your functions exercise file.

# Your functions exercise are not currently in a file with a name that can be easily 
# imported. Copy your functions exercise file and name the copy functions_exercises.py.

# Import each function in a different way:

# import the module and refer to the function with the . syntax
import functions_exercises

print(functions_exercises.cumsum([1, 2, 3, 4, 5]))

# use from to import the function directly
from functions_exercises import twelveto24

print(twelveto24("12:00am"))

# use from and give the function a different name
from functions_exercises import col_index as column_number

print(column_number("AAAA"))

# For the following exercises, read about and use the itertools module from the standard 
# library to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, 
# and 3?
import itertools

product_list = []

for product in itertools.product("ABC", "123"):
    product_list.append(product)

print(len(product_list))

print()

# How many different ways can you combine two of the letters from "abcd"?
combination_list = []

for combination in itertools.combinations_with_replacement("abcd", 2):
    combination_list.append(combination)

print("Number of different ways can you combine two of the letters from 'abcd':", len(combination_list))

# Save this file as profiles.json inside of your exercises directory. Use the load function 
# from the json module to open this file, it will produce a list of dictionaries. Using 
# this data, write some code that calculates and outputs the following information:
from json import load

profiles = load(open("profiles.json"))

# Total number of users
total_users = len(profiles)
print("Total number of users:", total_users)

# Number of active users
active_users = [profile for profile in profiles if profile["isActive"]]
total_active_users = len(active_users)
print("Total active users:", total_active_users)

# Number of inactive users
inactive_users = [profile for profile in profiles if not profile["isActive"]]
total_inactive_users = len(inactive_users)
print("Total inactive users:", total_inactive_users)

# Grand total of balances for all users
user_balances = [float(profile["balance"].replace("$", "").replace(",", "")) for profile in profiles]
total_balances = sum(user_balances)
print("Grand total of balances for all users: ${:,}".format(total_balances))

# Average balance per user
avg_balance = round(total_balances / len(user_balances), 2)
print("Average balance per user: ${:,}".format(avg_balance))

# User with the lowest balance
lowest_balance = min(user_balances)
user_with_lowest_balance = ""
for profile in profiles:
    balance = float(profile["balance"].replace("$", "").replace(",", ""))
    if balance == lowest_balance:
        user_with_lowest_balance = profile["name"]

print(user_with_lowest_balance)

# User with the highest balance
highest_balance = max(user_balances)
user_with_highest_balance = ""
for profile in profiles:
    balance = float(profile["balance"].replace("$", "").replace(",", ""))
    if balance == lowest

# Most common favorite fruit


# Least most common favorite fruit


# Total number of unread messages for all users

