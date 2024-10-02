# Python_GUI_Tkinter_Calculator
# Calculator Application

This Python project is a simple GUI-based calculator built using the `tkinter` library. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division, with a user-friendly graphical interface.

## Features

- **Basic operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/).
- **Interactive buttons**: Number and operator buttons to input expressions.
- **Clear functionality**: Reset the input field.
- **Evaluate**: Compute the entered expression using Python's `eval()` function.

## Dependencies

- Python 3.x
- `tkinter` library (bundled with Python)

## Code Overview

- `call_to_addition(symbol)`: Handles input of numbers and operators, updating the display.
- `evaluate()`: Evaluates the current expression entered and shows the result.
- `clear_field()`: Clears the current input and resets the display.

## Layout

The calculator has buttons for digits (0-9), operators (+, -, *, /), parentheses, and additional buttons for clearing the input (C) and calculating the result (=).
<br>
The UI is designed with a grid layout for easy access and responsive design

## How to Run

1. Make sure you have Python installed on your system.
2. Install `tkinter` (usually comes pre-installed with Python).
3. Save the code in a `.py` file and run it.

```bash
python main.py
