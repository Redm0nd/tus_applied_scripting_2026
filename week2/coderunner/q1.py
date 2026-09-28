print("Enter the Variable:")
variable_name = input();
print(f"The variable '{variable_name}' has been entered.")
# replace the underscores with a space
variable_name = variable_name.replace('_', ' ')
print(f"variable_name is now: {variable_name}")
variable_name = variable_name.title()
print(f"After converting to title case, variable_name is now: {variable_name}")
variable_name = variable_name.replace(' ','')
print(f"After removing spaces, variable_name is now: {variable_name}")
variable_name = variable_name[:1].lower() + variable_name[1:]
print(f"After converting the first character to lowercase, variable_name is now: {variable_name}")