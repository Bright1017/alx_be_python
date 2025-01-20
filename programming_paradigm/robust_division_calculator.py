"""
1. Robust Division Calculator with Command Line Arguments
mandatory
Score: 0.0% (Checks completed: 0.0%)
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

Task Description:
Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.

robust_division_calculator.py:
Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

Division by Zero: Use a try-except block to catch ZeroDivisionError.
Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
Return appropriate messages for errors or the result for successful division.

Implementation Notes for you:
Focus on error handling within safe_divide in robust_division_calculator.py. Ensure you cover the scenarios detailed above.
Test your function using main.py by passing different types of inputs via command line arguments. This method allows you to quickly assess how well your error handling works in various situations.
This task helps you practice writing error-resistant code, a crucial skill in software development.

"""


import sys

def division_calculator():
    try:
        # Ensure there are exactly three arguments: the script name, dividend, and divisor
        if len(sys.argv) != 3:
            raise ValueError("Usage: python division_calculator.py <dividend> <divisor>")

        # Parse command line arguments
        dividend = float(sys.argv[1])
        divisor = float(sys.argv[2])

        # Perform division
        result = dividend / divisor

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    division_calculator()

