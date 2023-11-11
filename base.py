innitvar = input("Please enter a number: ")
basevar = int(input("Please enter the base that your number is in: "))
convertvar = int(input("Please enter the base that you would like to convert to: "))

# Create a symbol-to-value table.
SY2VA = {'0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'a': 10,
         'b': 11,
         'c': 12,
         'd': 13,
         'e': 14,
         'f': 15,
         'g': 16,
}

# Take a string and base to convert to.
# Allocate space to store your number.
# For each character in your string:
#     Ensure character is in your table.
#     Find the value of your character.
#     Ensure value is within your base.
#     Self-multiply your number with the base.
#     Self-add your number with the digit's value.
# Return the number.

integer = 0
for character in innitvar:
    assert character in SY2VA, 'Found unknown character!'
    value = SY2VA[character]
    assert value < basevar, 'Found digit outside base!'
    integer *= basevar
    integer += value

# Create a value-to-symbol table.
VA2SY = dict(map(reversed, SY2VA.items()))

# Take a integer and base to convert to.
# Create an array to store the digits in.
# While the integer is not zero:
#     Divide the integer by the base to:
#         (1) Find the "last" digit in your number (value).
#         (2) Store remaining number not "chopped" (integer).
#     Save the digit in your storage array.
# Return your joined digits after putting them in the right order.

array = []
while integer:
    integer, value = divmod(integer, convertvar)
    array.append(VA2SY[value])
answer = ''.join(reversed(array))

# Display the results of the calculations.

import numpy as np

binary_string = answer

# Reshape the binary string into a 4x34 matrix
matrix = np.array(list(binary_string), dtype=int).reshape(4, 34)
permutation_string = "0100000100101000"
permutation_matrix = np.array(list(permutation_string), dtype=int).reshape(4, 4)
result = np.dot(permutation_matrix, matrix)

print("".join(map(str, result.flatten().tolist())))

