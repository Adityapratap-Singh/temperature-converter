# It is the code for the conversion of temprature in between Celsius and Fahrenheit and kelvin

print("")
print("Welcome to the Temperature Converter!")
print("You can convert between Celsius, Fahrenheit, and Kelvin.")
print("")

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    c = f_to_c(f)
    return c_to_k(c)

def k_to_f(k):
    c = k_to_c(k)
    return c_to_f(c)

while True:
    # Input temperature
    a = input("Enter the temperature (or type 'exit' to quit): ")
    if a.lower() == "exit":
        break
    a = float(a)
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        f = c_to_f(a)
        k = c_to_k(a)
        print(f"{a}°C is equal to {f}°F and {k}K")

    elif unit == 'F':
        c = f_to_c(a)
        k = f_to_k(a)
        print(f"{a}°F is equal to {c}°C and {k}K")

    elif unit == 'K':
        c = k_to_c(a)
        f = k_to_f(a)
        print(f"{a}K is equal to {c}°C and {f}°F")
        

    else:
        print("Invalid unit entered.")

    print("Thanks for using the converter. Stay cool 😎")
    print("")
    print("Made by @Mr_adex")

