#Q1 If download_time stores the value 54.33, what is the result of the following condition
#download_time < 60

download_time = 54.33;
print(download_time < 60)
# True

# If download_time stores the value 60, what is the result of the following condition
#download_time < 60

download_time = 60;
print(download_time < 60)
# False

# Q3 The variables amount_used and total_disk_space store decimal values.
# Which of the following is the correct statement (in Python!) to check 
# if the amount_used is greater than the total_disk_space?
amount_used = 100.1
total_disk_space = 99.9
#print(amount_used > total_disk_space)
if amount_used > total_disk_space:
    print("amount_used is greater than total_disk_space")

# Q4 Which of the following is the correct statement (in Python!) 
# to check if percent_free is equal to zero?

#percent_free = 1;
percent_free = 0;
if percent_free == 0:
    print("percent_free is equal to 0")

# Q5 A program is determining a message to display based on the percentage of free space. 
# A code block starts with:
# if percent_free == 0:
#    print("Warning: System full")
# Which of the following code blocks is the correct way (in Python!) 
# to then check if percent_free is less than 5?

percent_free = 20;

if percent_free == 0:
    print("Warning: System full")
elif percent_free < 5:
    print("You have less than 5% memory free")
# Q6: Which of the following code blocks is correct (in Python)?
else:
  print("System has sufficient disk space")


# Q7 What is the output of
# print("Status:", "Yellow" if temperature > 27 else "Green")
# when temperature is 18?

temperature = 18;
print("Status:", "Yellow" if temperature > 27 else "Green")

# Q8 The variable total stores an integer (whole number). 
# Which of the following if statements is the correct way to check if the total is equal to 7 or 11?

total = 5;
if total == 7 or total == 11:
    print("Total is equal to 7 or 11")

total = 5;
if total == 7 or 11:
    print("Total is equal to 7 or 11")
    print(bool(total is 7 or 11))

total = 5;
if total is 7 or 11:
    print("Total is equal to 7 or 11")
    print(bool(total is 7 or 11))

options = {
    "a": lambda total: 7 == total == 11,
    "b": lambda total: total ==7 or 11,
    "c": lambda total: total == 7 or total == 11,
    "d": lambda total: total is 7 or 11,
}

# What the correct answer should be for each test value
expected = {5: False, 7: True, 11: True, 0: False}

for name, check in options.items():
    print(f"Option {name}:")
    for value, should_be in expected.items():
        result = bool(check(value))
        status = "OK " if result == should_be else "BAD"
        print(f" total={value:<3} got {str(result):<5} expected {str(should_be):<5} {status}")

# Q9 Which of the following statements is the correct way 
# to then check if the total is equal to 2, 3 or 12:


options = {
    "a": "total is 2, 3 or 12",
    "b": "total == 2 or 3 or 12",
    "c": "total == 2 or total == 3 or total == 12",
    "d": "total == 2 == 3 == 12",
}

#expected = {1: False, 2: True, 3: True, 12: True, 15: False}
#for name, condition in options.items():
#    print(f"Option {name}: if {condition}:")
#    code = f"result = False\nif {condition}:\n    result = True"
#    for value, should_be in expected.items():
#        scope = {"total": value}
#        try:
#            exec(code, scope)
#        except SyntaxError:
#            print("  SyntaxError: not valid Python")
#            break

#        result = scope["result"]
#        status = "OK " if result == should_be else "BAD"
#        print(f"  total={value:<3} got {str(result):<5} expected {str(should_be):<5} {status}")

# Q10 The variable username contains a string. 
# What is the correct code to determine the length of the string, 
# that is, the number of characters in the string contained in the username variable?

username = "dylan"
print(len(username))

#print(username.length())

# Q11 A username must have between 4 and 8 characters (inclusive).
# Which of the following is not the correct code for a condition to 
# the check if the value of username contains a suitable number of characters?
# Hint: If you find this a bit confusing, try it out in the interactive Python interpreter
#  with different lengths of username, e.g. valid ones like "root", "joseph", "jbloggs" 
# (3 of the answers should return True, and the incorrect answer should return False), 
# and try invalid usernames such as "joe", "josephbloggs" and 
# again check which answers correctly return False)

username = "joesgs"

#if not len(username) < 4 and not len(username > 8):
#    print("True")
#else:
#    print("False")

if len(username) >=4 and len(username) <= 8:
    print("True")
else:
    print("False")

# Q12 A username must have between 4 and 8 characters (inclusive).
# Which of the following is the Pythonic code for a condition to 
# the check if the value of username contains a suitable number of characters?

username = "ro"

if not len(username) < 4 and not len(username) > 8:
    print ("Valid username length")
else: 
    print("Invalid username length")

if len(username) >= 4 or len(username) <= 8:
    print ("Valid username length")
else: 
    print("Invalid username length")

if 4 <= len(username) <=8:
    print ("Valid username length")
else: 
    print("Invalid username length")

if len(username) >=4 and len(username) <= 8:
    print ("Valid username length")
else: 
    print("Invalid username length")

# Q13 The variable username contains a string. 
# Assuming that the first character is a letter, 
# which of the following is the correct condition
#  to check if the first character of the string
#  in username is a lowercase letter?

username = "Dylan"

print(bool(username[0].lower())) # True, will always return True as it converts first letter to lower .
print(bool(username[1].islower())) # True
print(bool(username[0].islower())) # True
print(bool(username[1].lower())) # True

# Q14 The variable username contains a string. 
# Which of the following is the correct code for a condition to check if all
#  the characters in username are alphanumeric (i.e. letters and numbers)?

username = "dylanrs1edmond"

#if username.alpha():
#    print("true")
#else:
#    print("false")

if username.isalnum():
    print("true")
else:
    print("false")

#if username.alnum():
#    print("true")
#else:
#    print("false")

if username.isalpha():
    print("true")
else:
    print("false")

# Q15 A username is valid if
# it has between 4 and 8 characters, inclusive
# and the first character is a lowercase letter
# and all the characters are alphanumeric
# Which of the following combined conditions is the 
# correct code to validate a username based on the above rules?

username = "dylan22222212"

if 4 <= len(username) <= 8 and username[0].islower() and username.isalnum:
    print(f"True {username} meets the criteria")
else:
    print(f"False, {username} does not meet the criteria")

if 4 >= len(username) <= 8 and not username[0].islower() and not username.isalnum():
    print(f"True {username} meets the criteria")
else:
    print(f"False, {username} does not meet the criteria")

# c this one is correct as it meets all the criteria with an and 
if 4 <= len(username) <= 8 and username[0].islower() and username.isalnum():
    print(f"True {username} meets the criteria")
else:
    print(f"False, {username} does not meet the criteria")

if 4 <= len(username) <= 8 or username[0].islower() or username.isalnum():
    print(f"True {username} meets the criteria")
else:
    print(f"False, {username} does not meet the criteria")

# Q16 What is the output from the following code?
attendance = 0
if attendance:
    print("Students attended class")
else:
    print("No students attended class")

# Q17 what is the output from the following code?
value = 10
if value > 5:
    if value < 15:
        print("In range")
    else:
        print("Too high")
else:
    print("Too low")
    # In range

#Q18 Which of the following statements about the match-case structure is correct?
# a.The subject can be any expression, 
# but patterns must always be simple constants

# b.The subject must always be an integer, 
# and patterns can only be integer literals

# c.The subject can only be a variable,
# and patterns cannot include multiple alternatives

# d.The subject can be any expression, and patterns
#  can include literals, variables, sequence patterns, or wildcards

def check_number(x):
    match x:
        case "*":
            print("It's 10")
        case 20:
            print("It's 20")
        case _:
            print("It's neither 10 nor 20")

check_number("*")
check_number(30)
check_number(20)

command = "quit"

match command:
    case "quit":
        print("Bye")
    case "go" | "walk":
        print("Moving")
    case [x, y]:
        print(f"Two items: {x}, {y}")
    case _:                     # wildcard: matches anything, binds nothing
        print("Unknown command")

# Q19 What is the output from the following code?
greeting = "hello"
match greeting:
    case "hi":
        print("Hi")
    case "Hello":
        print("Hello")
    case "HELLO":
        print("HELLO")
    case _:
        print("Other")
# Other

# Q20
# Assuming connected contains a boolean value,
#  which of the following is the most Pythonic way
#  to rewrite the following code?
connected = False
if connected == False:
    print("Failed to connect")

if connected is False:
    print("Failed to connect")

if not connected:
    print("Failed to connect")

# can't be this doesn't compile
#if connected not True:
    #print("Failed to connect")


if bool(connected) == False:
    print("Failed to connect")

# When a variable already holds a boolean, 
# you don't compare it to True or False. 
# You use it directly as the condition, and not flips it.

for connected in [True, False]:
    if not connected:
        print(connected, "-> Failed to connect")
    else:
        print(connected, "-> Connected")