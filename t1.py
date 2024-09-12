# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_fahrenheit_kelvin(temp_c):
    fahrenheit = (temp_c * 9/5) + 32
    kelvin = temp_c + 273.15
    return fahrenheit, kelvin

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_celsius_kelvin(temp_f):
    celsius = (temp_f - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_celsius_fahrenheit(temp_k):
    celsius = temp_k - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Main program to ask the user for input and display the results
def temperature_conversion():
    print("Welcome to the Temperature Conversion Program!")
    
    # Get temperature value from the user
    temp_value = float(input("Enter the temperature value: "))
    
    # Get the original unit of the temperature from the user
    print("Please choose the unit of the temperature you entered:")
    print("1. Celsius (C)")
    print("2. Fahrenheit (F)")
    print("3. Kelvin (K)")
    unit_choice = input("Enter the number corresponding to the unit: ")

    # Conversion logic based on the input unit
    if unit_choice == '1':  # Celsius
        fahrenheit, kelvin = celsius_to_fahrenheit_kelvin(temp_value)
        print(f"{temp_value}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        
    elif unit_choice == '2':  # Fahrenheit
        celsius, kelvin = fahrenheit_to_celsius_kelvin(temp_value)
        print(f"{temp_value}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K.")
        
    elif unit_choice == '3':  # Kelvin
        celsius, fahrenheit = kelvin_to_celsius_fahrenheit(temp_value)
        print(f"{temp_value}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        
    else:
        print("Invalid input! Please enter a valid unit number (1, 2, or 3).")

# Run the temperature conversion program
temperature_conversion()
