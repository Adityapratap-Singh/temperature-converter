# main.py

from temperature_converter import  *

print("\nWelcome to the Temperature Converter!")
print("You can convert between Celsius, Fahrenheit, and Kelvin.\n")

while True:
    a = input("Enter the temperature (or type 'exit' to quit): ")

    if a.lower() == "exit":
        break

    try:
        temp = float(a)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        continue

    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        print(f"{temp}°C is equal to {c_to_f(temp)}°F and {c_to_k(temp)}K")
        print("")
    elif unit == 'F':
        print(f"{temp}°F is equal to {f_to_c(temp)}°C and {f_to_k(temp)}K")
        print("")
    elif unit == 'K':
        print(f"{temp}K is equal to {k_to_c(temp)}°C and {k_to_f(temp)}°F")
        print("")
    else:
        print("Invalid unit entered.")
        print("")


    print("Thanks for using the converter. Stay cool 😎")
    print("Made by @Mr_adex\n")
