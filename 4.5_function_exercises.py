# Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.

def is_two(x):
    '''takes a string or int and returns whether it is two'''
    return x == 2 or x == "2"

print("Test for is_two")
print(is_two(2))
print(is_two("2"))
print(is_two("3"))
print(is_two(3))
print()

# Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
def is_vowel(letter):
    '''takes a single character string and returns True if it is a vowel'''
    return (letter.lower() in 'aeiou') and len(letter) == 1

print("Test for is_vowel")
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel(""))
print(is_vowel("ab"))

# Define a function named is_consonant. It should return True if the passed string is a 
# consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return len(letter) == 1 and letter.isalpha and not is_vowel(letter)

print("Test for is_consenant")
print(is_consonant("a"))
print(is_consonant("b"))
print(is_consonant(""))
print(is_consonant("ab"))

# Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.
def capital(word):
    if is_consonant(word[0]):
        return word.title()
    return word

print(capital("apple"))
print(capital("banana"))
print(capital("carrot"))
print(capital("danish"))
print(capital("eggplant"))

# Define a function named calculate_tip. It should accept a tip percentage (a number 
# between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percentage, total):
    return tip_percentage * total

print(calculate_tip(.20, 10))

# Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.
def apply_discount(discount_percentage, total):
    return total - (discount_percentage * total)

print(apply_discount(.1, 10))

# Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.
def handle_commas(string_number):
    return int(string_number.replace(",", ""))

print(handle_commas("1,000"))
print(handle_commas("1,000,000"))
print(handle_commas("1,000,000,000"))

# Define a function named get_letter_grade. It should accept a number and return the 
# letter grade associated with that number (A-F).
def get_letter_grade(number_grade):
    if number_grade >= 90:
        return "A"
    elif number_grade >= 80:
        return "B"
    elif number_grade >= 70:
        return "C"
    elif number_grade >= 60:
        return "D"
    else:
        return "F"

# Define a function named remove_vowels that accepts a string and returns a string with 
# all the vowels removed.
def remove_vowels(string):
    string_without_vowels = []

    for character in string:
        if not is_vowel(character):
            string_without_vowels.append(character)

    return ''.join(string_without_vowels)

print(remove_vowels("banana"))
print(remove_vowels("calamatorium"))

# Define a function named normalize_name. It should accept a string and return a valid 
# python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
import re
def normalize_name(string):
    string = re.sub('[^A-Za-z0-9 _]+', '', string)

    while string[0].isdigit():
        string = string[1:len(string)]

    string = string.strip()
    string = string.replace(" ", "_")
    string = string.lower()
    return string

print(normalize_name("Name"))
print(normalize_name("First Name"))
print(normalize_name("% Completed"))

# Write a function named cumsum that accepts a list of numbers and returns a list that is 
# the cumulative sum of the numbers in the list.
def cumsum(num_list):
    sum_list = []
    sum_stor = 0
    for num in num_list:
        sum_list.append(sum_stor + num)
        sum_stor += num
    return sum_list

print(cumsum([1, 2, 3]))
print(cumsum([1, 1, 1]))
print(cumsum([1, 2, 3, 4]))

# Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.
def twelveto24(time):
    separate_hour = time.split(":")
    separate_minute = separate_hour[1][0:2]

    if "am" in separate_hour[1]:
        if len(separate_hour[0]) == 1:
            return "0" + separate_hour[0] + ":" + separate_minute
        elif separate_hour[0] == "12":
            return "00" + ":" + separate_minute
        else:
            return separate_hour[0] + ":" + separate_minute
    else:
        if separate_hour[0] == "12":
            return separate_hour[0] + ":" + separate_minute
        else:
            return str(int(separate_hour[0]) + 12) + ":" + separate_minute

print(twelveto24("9:45am"))
print(twelveto24("10:25am"))
print(twelveto24("12:01am"))
print(twelveto24("12:26pm"))
print(twelveto24("4:36pm"))
print(twelveto24("10:56pm"))

def twentyfourto12(time):
    time = time.split(":")
    hour = time[0]
    minutes = time[1]

    if hour < 13:
        return


# Create a function named col_index. It should accept a spreadsheet column name, and 
# return the index number of the column.
def col_index(column_name):
    column_name = column_name.lower()
    
    total = 0
    position = 0
    for char in reversed(column_name):
        total += (ord(char) - 96) * (26 ** position)
        position += 1
    
    return total

print(col_index("A"))
print(col_index("AA"))
print(col_index("ZZ"))
print(col_index("AAA"))
print(col_index("XFD"))