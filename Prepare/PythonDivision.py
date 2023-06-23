# Task
# The provided code stub reads two integers,  a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  a // b. The second line should contain the result of float division, a / b.

# No rounding or formatting is necessary.

# Example
# a = 3
# b = 5

# The result of the integer division 3 // 5 = 0.
# The result of the float division is 3/5 = 0.6.
# Print:

# 0
# 0.6
# Input Format

# The first line contains the first integer, a .
# The second line contains the second integer, b.

# Output Format

# Print the two lines as described above.

# Sample Input 0

# 4
# 3
# Sample Output 0

# 1
# 1.33333333333


a = int(input())  # Read the first integer
b = int(input())  # Read the second integer

# Perform integer division and print the result
print(a // b)

# Perform float division and print the result
print(a / b)