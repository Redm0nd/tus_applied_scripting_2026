# Write a Python program which generates and displays your name for Witness Protection,
# by adding name of your first pet and the name of the place where you grew up.

first_pet = input("Enter the name of your first pet: ")
grew_up = input("Enter the name of the place where you grew up: ")

# names should have a capital letter at the start so need to title them. 
first_pet = first_pet.title()
grew_up = grew_up.title()

print(f"Your Witness Protection Name is: {first_pet} {grew_up}")