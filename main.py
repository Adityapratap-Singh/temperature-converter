# It is the code for the conversion of temprature in between Celsius and Fahrenheit and kelvin

print("Welcome to the Temperature Converter!")

a = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

if unit == 'C':
    fahrenheit = (a * 9/5) + 32
    kelvin = a + 273.15
    print(f"{a}° Celsius is equal to {fahrenheit}° Fahrenheit and {kelvin} Kelvin.")
    print("")

elif unit == 'F':
    celsius = (a - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{a}° Fahrenheit is equal to {celsius}° Celsius and {kelvin} Kelvin.")
    print("")

elif unit == 'K':
    celsius = a - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"{a} Kelvin is equal to {celsius}° Celsius and {fahrenheit}° Fahrenheit.")
    print("")

else:
    print("Invalid unit entered.")

print("Thanks for using the converter. Stay cool 😎")