
# Temperature Conversion Program

This repository contains two Python programs that convert temperatures between Celsius, Fahrenheit, and Kelvin scales:
1. **Command-Line Version**: A terminal-based program.
2. **GUI Version**: A graphical user interface (GUI) application using Tkinter.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Programs](#running-the-programs)
  - [Command-Line Version](#command-line-version)
  - [GUI Version](#gui-version)
- [Usage Examples](#usage-examples)
  - [Command-Line](#command-line-example)
  - [GUI Example](#gui-example)
- [License](#license)

## Features
- Convert temperatures between Celsius, Fahrenheit, and Kelvin.
- Easy-to-use command-line interface.
- GUI built using Tkinter for a user-friendly experience.

## Prerequisites
Before you begin, ensure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/) (with `tkinter` for GUI)
- [VS Code](https://code.visualstudio.com/) or another Python IDE (optional but recommended)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/temperature-conversion.git
   ```

2. Navigate to the project directory:
   ```bash
   cd temperature-conversion
   ```

## Running the Programs

### Command-Line Version
To run the command-line version of the temperature conversion program:

1. Open a terminal and navigate to the project folder.
2. Run the following command:
   ```bash
   python temperature_conversion.py
   ```

3. The program will prompt you for a temperature and the original unit of measurement, and it will display the converted values for the other two units.

### GUI Version
To run the GUI version of the temperature conversion program:

1. Open a terminal and navigate to the project folder.
2. Run the following command:
   ```bash
   python temperature_conversion_gui.py
   ```

3. A window will appear where you can input the temperature value and select the unit of measurement. Press the "Convert" button to see the result.

## Usage Examples

### Command-Line Example
```bash
Welcome to the Temperature Conversion Program!
Enter the temperature value: 25
Please choose the unit of the temperature you entered:
1. Celsius (C)
2. Fahrenheit (F)
3. Kelvin (K)
Enter the number corresponding to the unit: 1
25.0°C is equal to 77.00°F and 298.15K.
```

### GUI Example
In the GUI window:
- Input `25` as the temperature.
- Select `Celsius` as the unit.
- Click the **Convert** button, and the result will display:
  ```
  25°C = 77.00°F, 298.15K
  ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
