# The Imperial System of measurement uses feet and inches to measure short distances.
# The following formulae can be used to convert a distance in feet and inches to metres:
# total inches = feet × 12 + inches
# centimetres = total inches × 2.54
# metres = centimetres / 100
# Write and test a program which inputs a distance in feet and inches
# and then calculates and displays the distance in metres.

feet = float(input("Enter the number of feet: "))
inches = float(input("Enter the number of inches: "))

total_inches = (feet*12) + inches;
centimetres = total_inches * 2.54;
metres = centimetres/100;
#metres = round(metres, 4)
#print(f"{total_inches}")
print(f"The distance in metres is {metres:.4f} metres")