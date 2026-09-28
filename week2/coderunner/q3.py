# Write and test a program to input a user's fullname (in the format firstname lastname) 
# and then generate and display a lowercase username using their firstname and the 
# first initial of their lastname.

fullname = input("Enter your first and last names, separate by a space: ")
# get the name in to lower case
fullname = fullname.lower()
first_name = fullname.split()[0]
last_name = fullname.split()[1]


#print(f"{first_name} {last_name}")

print(f"Your user name is: {first_name}{last_name[0]}")
