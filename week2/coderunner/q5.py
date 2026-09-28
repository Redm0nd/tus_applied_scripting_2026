# An LC circuit, also called a resonant circuit, consists of an inductor, 
# represented by the letter L, and a capacitor, represented by the letter C. 
# The resonant frequency is given by the formula f = 1/2pi*(sqrtLC)
# where L is the inductance in henries, and C is the capacitance in farads.
# Write a program which inputs the values of the inductance and the capacitance 
# and then calculates and displays the resonant frequency on an 
# LC circuit correct to 3 decimal places.

#importing math to use pi and sqrt 
import math

inductance = float(input(("Enter the inductance: ")))
capacitance = float(input("Enter the capacitance? "))

resonant_frequency = (1/(2*math.pi*math.sqrt(inductance*capacitance)))

print(f"Resonant Frequency: {resonant_frequency:.3f}")



