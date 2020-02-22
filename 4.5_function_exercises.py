# Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.

def is_two(x):
    '''takes a string or int and returns whether it is two'''
    if x == 2:
        return True
    elif x == "2":
        return True
    else:
        return False

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
    if type(letter) != str:
        return False
    elif len(letter) > 1 or len(letter) < 1:
        return False
    elif letter.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

print("Test for is_vowel")
print(is_vowel("a"))
print(is_vowel("b"))
print(is_vowel(""))
print(is_vowel("ab"))
print(is_vowel(3))

# Define a function named is_consonant. It should return True if the passed string is a 
# consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(letter):
    if type(letter) != str:
        return False
    elif len(letter) > 1 or len(letter) < 1:
        return False
    elif is_vowel(letter):
        return False
    else:
        return True

print("Test for is_consenant")
print(is_consonant("a"))
print(is_consonant("b"))
print(is_consonant(""))
print(is_consonant("ab"))
print(is_consonant(3))

# Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.







def cumsum(num_list):
    sum_list = []
    sum_stor = 0
    for num in num_list:
        sum_list.append(sum_stor + sum_list)
    return sum_list
        