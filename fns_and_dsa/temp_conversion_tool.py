# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        # Prompt the user for input
        temperature = input("Enter the temperature value: ")
        if not temperature.replace('.', '', 1).isdigit() and not (temperature[0] == '-' and temperature[1:].replace('.', '', 1).isdigit()):
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temperature)
        unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? Enter C or F: ").strip().upper()

        # Perform the conversion based on the user's input
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)
