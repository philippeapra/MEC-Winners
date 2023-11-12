import numpy as np
import os

def base17_to_binary(base17_string):
    decimal_value = int(base17_string, 17)
    return format(decimal_value, 'b')


def reverse_permutation_matrix(permutation_matrix_string):
    size = int(len(permutation_matrix_string) ** 0.5)
    matrix = np.array([int(bit) for bit in permutation_matrix_string]).reshape(size, size)
    inverted_matrix = np.linalg.inv(matrix)
    return np.round(inverted_matrix).astype(int)


def apply_reverse_permutation(binary_string, permutation_matrix):
    size = permutation_matrix.shape[0]
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


output_file_name = 'out.txt'
outputs = []

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'in.txt'), 'r') as input_file:
    for line in input_file:
        content = line.strip( ).split(':')
        print(content)
        permutation_matrix_string = content[0]
        base17_string = content[1].replace("CQI", "G").upper()

        binary_string = base17_to_binary(base17_string)
        reverse_matrix = reverse_permutation_matrix(permutation_matrix_string)
        reversed_binary = apply_reverse_permutation(binary_string, reverse_matrix)
        decoded_string = binary_to_string(reversed_binary)
        outputs.append(decoded_string)

        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), output_file_name), 'w', encoding='utf-8') as output_file:
            for output in outputs:
                """
                try:
                    output_file.write(output + "\n")
                except UnicodeEncodeError:
                    output_file.write("null\n")
                """
                output_file.write(output + "\n")



