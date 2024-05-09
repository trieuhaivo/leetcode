# Calculate point

# https://bigocoder.com/courses/179/lectures/2514/problems/114?view=statement

# Today is a holiday, Ben plays a game with his friends. The rules of game is very simple, each person will receive a positive integer consisting of 5 digits. If anyone has the largest point of their number, then they win. Help Ben to calculate his point.

# The point number of a number is the last digit of the sum of the digits of that number. For example the number 12345 has the sum of the digits is 1 + 2 + 3 + 4 + 5 = 15, so its point number is the last digit of 15 which is the number 5.

# Input Format
# A line consists of one positive integer x with 5 digits, constraint 10000≤x≤99999.

# Output Format
# Print point of Ben 's number x.

# Sample test

# input
# 45676

# output
# 8

# input
# 14104

# output
# 0

# Explanation for sample test
# The given number is 45676, then sum of every digits of 45676 is 4 + 5 + 6 + 7 + 6 = 28. Then the answer is the last digit of 28 is 8.

print(sum(map(int, input())) % 10)

# # Define the main function
# def main():
#         # Read a positive integer with 5 digits from the user
#         user_input = input("Enter a positive integer with 5 digits: ")
        
#         # Calculate the sum of the digits in the input number
#         digit_sum = 0
#         for digit in user_input:
#                 digit_sum += int(digit)
        
#         # Calculate the last digit of the digit_sum
#         last_digit = digit_sum %10
        
#         # Display the calculated last digit as the result
#         print("The calculated last digit is:", last_digit)

# # Check if the script is being run directly (not imported as a module)
# if__name__ == '__main__':
#         # Call the main function when the script is run directly
#         main()
