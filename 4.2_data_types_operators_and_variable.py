# Identify the data type of the following values:
    # 99.9
        # float
    # "False"
        # string
    # False
        # boolean
    # '0' 
        # string
    # 0
        # integer
    # True
        # boolean
    # 'True'
        # string
    # [{}]
        # list
    # {'a': []}
        # dictionary

# What data type would best represent:
    # A term or phrase typed into a search box?
        # string
    # If a user is logged in?
        # boolean
    # A discount amount to apply to a user's shopping cart?
        # integer or float
    # Whether or not a coupon code is valid?
        # boolean
    # An email address typed into a registration form?
        # string
    # The price of a product?
        # float
    # A Matrix?
        # list
    # The email addresses collected from a registration form?
        # string
    # Information about applicants to Codeup's data science program?
        # dict, list, or string

# For each of the following code blocks, read the expression and predict what the result of
# evaluating it would be, then execute the expression in your Python REPL.
    # '1' + 2
        # Error
    # 6 % 4
        # 2
    # type(6 % 4)
        # int
    # type(type(6 % 4))
        # type
    # '3 + 4 is ' + 3 + 4
        # Error
    # 0 < 0
        # False
    # 'False' == False
        # False
    # True == 'True'
        # False
    # 5 >= -5
        # True
    # !False or False
        # True
    # True or "42"
        # True
    # !True && !False
        # False
    # 6 % 5
        # 1
    # 5 < 4 and 1 == 1
        # False
    # 'codeup' == 'codeup' and 'codeup' == 'Codeup'
        # False
    # 4 >= 0 and 1 !== '1'
        # Error
    # 6 % 3 == 0
        # True
    # 5 % 2 != 0
        # True
    # [1] + 2
        # Error
    # [1] + [2]
        # [1, 2]
    # [1] * 2
        # [1, 1]
    # [1] * [2]
        # Error
    # [] + [] == []
        # True
    # {} + {}
        # Error

# Write some Python code, that is, variables and operators, to describe the following
# scenarios. Do not worry about the real operations to get the values, the goal of these
# exercises is to understand how real world conditions can be represented with code.

    # You have rented some movies for your kids: The little mermaid (for 3 days),
    # Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if
    # they're going to like it). If price for a movie per day is 3 dollars, how much will you 
    # have to pay?
the_little_mermaid = 3
brother_bear = 5
hercules = 1
total_price = (the_little_mermaid + brother_bear + hercules) * 3
print(f"Total rental price: ${total_price}")

    # Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
    # they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
    # and Facebook 350. How much will you receive in payment for this week? You worked 10
    # hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_rate = 400
amazon_rate = 380
facebook_rate = 350
facebook_hours = 10
google_hours = 6
amazon_hours = 4
total_payment = (google_rate * google_hours) + (facebook_rate * facebook_hours) + (amazon_rate * amazon_hours)
print(f"Total payment: ${total_payment}")

    # A student can be enrolled to a class only if the class is not full and the class
    # schedule does not conflict with her current schedule.
class_has_room = True
schedule_works = True
can_enroll = class_has_room and schedule_works
print(f"Able to enroll:", can_enroll)

    # A product offer can be applied only if people buys more than 2 items, and the offer
    # has not expired. Premium members do not need to buy a specific amount of products.
num_items_bought = 3
is_premium_member = False
offer_valid = True
apply_product_offer = offer_valid and (num_items_bought > 2 or is_premium_member)
print("Apply product offer:", apply_product_offer)

# Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
    # the password must be at least 5 characters
pass_length_correct = len(password) >= 5
print("Password length correct:", pass_length_correct)
    # the username must be no more than 20 characters
username_length_correct = len(username) <= 20
print("Username length correct:", username_length_correct)
    # the password must not be the same as the username
pass_and_username_different = username != password
print("Password and username are different:", pass_and_username_different)
    # bonus neither the username or password can start or end with whitespace
pass_and_username_lack_whitespace = (username[0] != " " and username[-1] != " ") and (password[0] != " " and password[-1] != " ")
print("Password and username don't start or end with whitespace", pass_and_username_lack_whitespace)