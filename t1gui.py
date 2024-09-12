import tkinter as tk
from tkinter import messagebox

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

# Function to handle the conversion based on user input
def convert_temperature():
    try:
        temp_value = float(entry_temp.get())
        unit = selected_unit.get()

        if unit == "Celsius":
            fahrenheit, kelvin = celsius_to_fahrenheit_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K")
        
        elif unit == "Fahrenheit":
            celsius, kelvin = fahrenheit_to_celsius_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°F = {celsius:.2f}°C, {kelvin:.2f}K")
        
        elif unit == "Kelvin":
            celsius, fahrenheit = kelvin_to_celsius_fahrenheit(temp_value)
            result_label.config(text=f"{temp_value}K = {celsius:.2f}°C, {fahrenheit:.2f}°F")
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid temperature value.")

# Set up the main application window
app = tk.Tk()
app.title("Temperature Conversion")
app.geometry("400x300")
app.resizable(False, False)

# Labels and Entry for input temperature
label_temp = tk.Label(app, text="Enter Temperature:")
label_temp.pack(pady=10)

entry_temp = tk.Entry(app)
entry_temp.pack(pady=5)

# Radio buttons for selecting temperature unit
selected_unit = tk.StringVar()
selected_unit.set("Celsius")

frame_units = tk.Frame(app)
frame_units.pack(pady=10)

radio_celsius = tk.Radiobutton(frame_units, text="Celsius (C)", variable=selected_unit, value="Celsius")
radio_fahrenheit = tk.Radiobutton(frame_units, text="Fahrenheit (F)", variable=selected_unit, value="Fahrenheit")
radio_kelvin = tk.Radiobutton(frame_units, text="Kelvin (K)", variable=selected_unit, value="Kelvin")

radio_celsius.pack(side="left", padx=10)
radio_fahrenheit.pack(side="left", padx=10)
radio_kelvin.pack(side="left", padx=10)

# Button to trigger conversion
convert_button = tk.Button(app, text="Convert", command=convert_temperature)
convert_button.pack(pady=20)

# Label to display the results
result_label = tk.Label(app, text="Result will be shown here", font=("Arial", 12))
result_label.pack(pady=20)

# Start the application
app.mainloop()
