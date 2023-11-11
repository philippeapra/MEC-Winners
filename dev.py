import numpy as np

def base17_to_binary(base17_string):
    """Convert a base 17 string to binary."""
    decimal_value = int(base17_string, 17)
    return format(decimal_value, 'b')

def reverse_permutation_matrix(permutation_matrix_string):
    """Reverse a permutation matrix."""
    size = int(len(permutation_matrix_string) ** 0.5)
    matrix = np.array([int(bit) for bit in permutation_matrix_string]).reshape(size, size)
    inverted_matrix = np.linalg.inv(matrix)
    return np.round(inverted_matrix).astype(int)

def apply_reverse_permutation(binary_string, permutation_matrix):
    size = permutation_matrix.shape[0]
    # Ensure binary string length is a multiple of the matrix size
    padded_length = size * ((len(binary_string) + size - 1) // size)
    binary_string = binary_string.ljust(padded_length, '0')

    chunks = [binary_string[i:i + size] for i in range(0, len(binary_string), size)]

    reversed_string = ''
    for chunk in chunks:
        vector = np.array([int(bit) for bit in chunk])
        reversed_vector = np.dot(permutation_matrix, vector) % 2
        reversed_chunk = ''.join(str(bit) for bit in reversed_vector)
        reversed_string += reversed_chunk

    return reversed_string

def binary_to_string(binary_string):
    bytes = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    characters = [chr(int(byte, 2)) for byte in bytes if int(byte, 2) != 0]
    return ''.join(characters)

def reverse_process_string(base17_string, permutation_matrix_string):
    binary_string = base17_to_binary(base17_string)
    reverse_matrix = reverse_permutation_matrix(permutation_matrix_string)
    reversed_binary = apply_reverse_permutation(binary_string, reverse_matrix)
    ascii_string = binary_to_string(reversed_binary)
    return ascii_string

# Custom permutation matrix
permutation_matrix_string = '0100000100101000'

# The base 17 string to be reversed
base17_string = '11d48ed9dCQIc6ab6c6147d845e586da03b9'.replace('CQI', 'G').upper()

# Reverse process the string
reversed_string = reverse_process_string(base17_string, permutation_matrix_string)
print(reversed_string)
