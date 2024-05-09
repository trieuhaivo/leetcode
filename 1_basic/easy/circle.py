# Circle

# https://bigocoder.com/courses/179/lectures/2514/problems/115?view=statement

# Give the radius of a circle, calculate its circumference and area.

# Known that:

# Circumference of circle = 2 * radius * PI
# Area of circle = radius * radius * PI Convention: PI = 3.14

# Input Format
# A single line consists of a positive real number not exceeding 2000 - the radius of the circle.

# Output Format
# Consists of two lines.

# The first line is the circumference of the circle.
# The second line is the area of the circle. Note: Results must be printed with 2 digits after the decimal part.

# Sample test
# input
# 5.00

# output
# 31.40
# 78.50

# Import the math module to access mathematical functions and constants
import math

# Define the main function
def main():
    radius = float(input())  # Read a floating-point number input from the user and store it as 'radius'

    # Calculate the circumference using the formula: circumference = 2 * π * radius
    circumference = 2 * math.pi * radius
    
    # Calculate the area using the formula: area = π * radius^2
    area = math.pi * radius ** 2

    # Print the calculated circumference with 2 decimal places
    print(f"{circumference:.2f}")

    # Print the calculated area with 2 decimal places
    print(f"{area:.2f}")

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    main()  # Call the main function when the script is run directly

