# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
OFFSET = 32  # Offset for Fahrenheit to Celsius and vice versa


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    return fahrenheit

def main():
    try:
        # Prompt user for temperature input
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on user input
        if unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp:.1f}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp:.1f}°C is {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")
        print(e)

if __name__ == "__main__":
    main()




# if name == "main"

# This line checks whether the script is being run as the main program.

# __name__ is a special built-in variable in Python. When a script is executed directly, __name__ is set to "__main__".

# When the script is imported as a module in another program, __name__ is set to the name of the script/module.

# By using if __name__ == "__main__":, we ensure that certain code only runs when the script is executed directly, and not when it is imported. This is a common practice in Python scripts to allow code to be reusable as modules without executing the entire script upon import.

# main():

# This line calls the main function, which contains all the core logic of the script (such as user interaction, temperature conversion, and error handling).

# By placing the execution of the main function within the if __name__ == "__main__": block, we ensure that the script will proceed to prompt the user and perform conversions only when the script is run directly.

# Importance:
# Script Modularity: These lines allow the script to be both an executable program and an importable module. Other scripts can import temp_conversion_tool.py and use its functions without running the main() function. This promotes code reuse and modular programming.

# Control Execution Flow: They help control the flow of execution, ensuring that certain parts of the code (i.e., user interaction) only run in specific contexts. This makes the script more versatile and maintainable.