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
