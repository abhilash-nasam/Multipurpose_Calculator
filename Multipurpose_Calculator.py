import math
# --------------------------
# BASIC CALCULATOR FUNCTIONS
# --------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# --------------------------
# SCIENTIFIC CALCULATOR
# --------------------------

def square_root(x):
    return math.sqrt(x)

def power(a, b):
    return math.pow(a, b)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# --------------------------
# UNIT CONVERTER
# --------------------------

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# --------------------------
# BMI CALCULATOR
# --------------------------

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# --------------------------
# SIMPLE INTEREST
# --------------------------

def simple_interest(p, r, t):
    return (p * r * t) / 100

# --------------------------
# MAIN MENU
# --------------------------

def main():
    while True:
        print("\n========= MULTI-PURPOSE CALCULATOR =========")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Unit Converter")
        print("4. BMI Calculator")
        print("5. Simple Interest Calculator")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        # ---------------------- BASIC CALCULATOR ----------------------
        if choice == 1:
            print("\n--- BASIC CALCULATOR ---")
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            print("Addition:", add(a, b))
            print("Subtraction:", subtract(a, b))
            print("Multiplication:", multiply(a, b))
            print("Division:", divide(a, b))

        # ---------------------- SCIENTIFIC CALCULATOR ----------------------
        elif choice == 2:
            print("\n--- SCIENTIFIC CALCULATOR ---")
            print("1. Square Root")
            print("2. Power")
            print("3. Sine")
            print("4. Cosine")
            print("5. Tangent")

            s = int(input("Choose operation: "))

            if s == 1:
                x = float(input("Enter number: "))
                print("Square Root:", square_root(x))

            elif s == 2:
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                print("Power:", power(a, b))

            elif s == 3:
                x = float(input("Enter angle in degrees: "))
                print("Sine:", sine(x))

            elif s == 4:
                x = float(input("Enter angle in degrees: "))
                print("Cosine:", cosine(x))

            elif s == 5:
                x = float(input("Enter angle in degrees: "))
                print("Tangent:", tangent(x))

        # ---------------------- UNIT CONVERTER ----------------------
        elif choice == 3:
            print("\n--- UNIT CONVERTER ---")
            print("1. Kilometer to Miles")
            print("2. Celsius to Fahrenheit")
            u = int(input("Choose conversion: "))

            if u == 1:
                km = float(input("Enter KM: "))
                print("Miles:", km_to_miles(km))

            elif u == 2:
                c = float(input("Enter Celsius: "))
                print("Fahrenheit:", celsius_to_fahrenheit(c))

        # ---------------------- BMI CALCULATOR ----------------------
        elif choice == 4:
            print("\n--- BMI CALCULATOR ---")
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (meters): "))
            print("Your BMI:", calculate_bmi(weight, height))

        # ---------------------- SIMPLE INTEREST ----------------------
        elif choice == 5:
            print("\n--- SIMPLE INTEREST CALCULATOR ---")
            p = float(input("Principal Amount: "))
            r = float(input("Rate of Interest: "))
            t = float(input("Time (years): "))
            print("Simple Interest:", simple_interest(p, r, t))

        elif choice == 6:
            print("Thank You for using the Calculator!")
            break

        else:
            print("Invalid choice. Try again.")

# RUN PROGRAM
main()
