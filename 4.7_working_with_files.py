# Read the contents of your last exercise file into a variable.
with open("4.6_import_exercises.py") as f:
    import_exercises = f.read()

# Print out every line in the file
print(import_exercises)

# Print out every line in the file, but add a line numbers
with open("4.6_import_exercises.py") as f:
    for i, line in enumerate(f, start=1):
        print(f'{i}: {line.strip()}')
# Write some python code to create a grocery list.
# Create a variable named grocery_list. It should be a list, and the elements in the list 
# should be a least 3 things that you need to buy from the grocery store.
grocery_list = ["apples", "bananas", "strawberries"]
# Create a function named make_grocery_list. When run, this function should write the contents 
# of the grocery_list variable to a file named my_grocery_list.txt.
def make_grocery_list(list_of_items):
    with open("my_grocery_list.txt", "w") as f:
        for item in list_of_items:
            f.write(item + "\n")

make_grocery_list(grocery_list)
# Create a function named show_grocery_list. When run, it should read the items from the text 
# file and show each item on the grocery list.
def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        read_file = f.read()
        print()
        print("my_grocery_list.txt contains:")
        print(read_file)

show_grocery_list()
# Create a function named buy_item. It should accept the name of an item on the grocery list, 
# and remove that item from the list.
def buy_item(item):
    with open("my_grocery_list.txt") as f:
        contents = f.readlines()
    
    item = item + "\n"
    contents.remove(item)

    with open("my_grocery_list.txt", "w") as f:
        for line in contents:
            f.writelines(line)

buy_item("bananas")
show_grocery_list()