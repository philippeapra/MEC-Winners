import numpy as np


def hex_cqi_to_binary(hex_cqi_string):
    # Define the Hex-CQI mapping
    hex_cqi_mapping = {str(i): format(i, '04b') for i in range(10)}
    hex_cqi_mapping.update({chr(i + 55): format(i, '04b') for i in range(10, 16)})
    hex_cqi_mapping['CQI'] = '10001'  # CQI represents the 17th digit in our base-17 system

    # Replace each Hex-CQI character with its binary representation
    binary_string = ''
    i = 0
    while i < len(hex_cqi_string):
        if hex_cqi_string[i:i + 3] == 'CQI':
            binary_string += hex_cqi_mapping['CQI']
            i += 3
        else:
            binary_string += hex_cqi_mapping[hex_cqi_string[i]]
            i += 1

    return binary_string


def base2_to_base17(num_base2):
    num_base10 = int(num_base2, 2)
    num_base17 = hex(num_base10)[2:]
    return num_base17


def base17_to_base2(num_str):
    """
    Converts a base 17 number (represented as a string) to a base 2 number.
    """

    # Define the characters used in base 17
    base17_chars = "0123456789ABCDEFG"

    # Convert the base 17 number to base 10
    num_base10 = 0
    for digit in num_str:
        if digit.upper() in base17_chars:
            num_base10 = num_base10 * 17 + base17_chars.index(digit.upper())
        else:
            return "Invalid input. Not a base 17 number."

    # Convert the base 10 number to base 2
    num_base2 = bin(num_base10)[2:]

    return num_base2

def binary_to_ascii(binary_string):
    text = ''.join(chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8))
    return text


def ascii_to_binary(ascii_string):
    binary_string = ""
    for char in ascii_string:
        binary_string += bin(ord(char))[2:].zfill(8)
    return binary_string



four_by_four_vector = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]

string = "Hello world!"
#
# print(ascii_to_binary(string))

def invert_matrix(matrix):
    return np.linalg.inv(matrix)



# Example usage
base17_num = "1A3F"
base2_num = base17_to_base2(base17_num)
print(base2_num)


def create_a_4_by_x_matrix(base2_num):
    matrix = []
    for i in range(0, len(base2_num), 4):
        matrix.append([int(base2_num[i]), int(base2_num[i + 1]), int(base2_num[i + 2]), int(base2_num[i + 3])])
    return matrix


print(len(base17_to_base2("11d48ed9dCQIc6ab6c6147d845e586da03b9".replace("CQI", "G").upper())))

