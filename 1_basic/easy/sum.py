# Sum

# https://bigocoder.com/courses/179/lectures/2514/problems/157?view=statement

# Write a program allowing user to enter 2 integers which are the amount of Upan's and Ipan's candy, respectively. Then calculate and print out the total candy of Upan and Ipan on the screen.

# Input Format
# Consisting of only a line with 2 integers a and b, seperated by a space (a and b are 32-bit integers), with a, b are number of Upan's and Ipan's candy, respectively. It is guaranteed that the sum of a and b is also a 32-bit integer.

# Output Format
# Print the result following the format "a+b=c" of where c is the total candy of Upan and Ipan.

# Sample test
# input
# 4 5

# output
# 4 + 5 = 9

a, b = map(int, input().split())
print(f'{a} + {b} = {a + b}')

# # Define a function to calculate the total candy by summing Upan's and Ipan's candy
# def calculate_total_candy(upan_candy, ipan_candy):
#     total_candy = upan_candy + ipan_candy  # Calculate the sum of Upan's and Ipan's candy
#     return total_candy  # Return the calculated total candy

# # Define the main function
# def main():
#     # Input the amount of Upan's and Ipan's candy as space-separated integers
#     upan_candy, ipan_candy = map(int, input().split())

#     # Calculate the total candy using the 'calculate_total_candy' function
#     total_candy = calculate_total_candy(upan_candy, ipan_candy)

#     # Output the result in a formatted string
#     print(f"{upan_candy} + {ipan_candy} = {total_candy}")

# # Check if the script is being run directly (not imported as a module)
# if __name__ == '__main__':
#     main()  # Call the main function when the script is run directly
