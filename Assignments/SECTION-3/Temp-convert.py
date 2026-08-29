#Ask the user for a temperature in Celsius, then print it in both Fahrenheit and Kelvin.

#Formulas:
#• Fahrenheit = (C × 9/5) + 32
#• Kelvin     = C + 273.15

#Remember: input() gives you a string, so convert it with float() before doing any math — otherwise you'll hit the classic type error.

Celsius = float(input("Enter temprature in celsius:"))

Fahrenheit = (Celsius*9/5) + 32
Kelvin     = Celsius+ 273.15

print(f"{Celsius}C: {Fahrenheit}F")
print(f"{Celsius}C: {Kelvin}K")