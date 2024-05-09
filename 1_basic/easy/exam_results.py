# Exam results

# https://bigocoder.com/courses/179/lectures/2514/problems/133?view=statement

# Write a program to enter test grades of 3 tests: Math, Natural Science and English. Calculate the total grades of 3 tests of that student.

# Input Format
# The first line contains the grade of Math.
# The second line contains the grade of Natural Science.
# The third line contains the grade of English. Knowing that the input grade is a real number between 0.0 and 10.0.

# Output Format
# A single line contains the result. Note: The result must be printed with 2 digits after the decimal point.

# Sample test
# input
# 7.5
# 9.0
# 10.0

# output
# 26.50

print(f"{sum(map(float, input().split())):.2f}")

# # Define the main function
# def main():
#     # Read the grades of Math, Natural Science, and English
#     math_grade = float(input())
#     science_grade = float(input())
#     english_grade = float(input())

#     # Calculate the total grades by adding the grades of all three subjects
#     total_grades = math_grade + science_grade + english_grade

#     # Print the total grades with 2 digits after the decimal point
#     print(f"{total_grades:.2f}")

# # Check if the script is being run directly (not imported as a module)
# if __name__ == '__main__':
#     main()  # Call the main function when the script is run directly

