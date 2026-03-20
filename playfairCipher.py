import numpy as np

def grid_of_letters(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    mat = []

    for ch in key:
        if ch not in seen:
            seen.add(ch)
            mat.append(ch)

    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch not in seen and ch != 'J':
            seen.add(ch)
            mat.append(ch)

    return np.array(mat).reshape(5, 5)


def prepare_text(text):
    text = text.upper().replace(" ", "").replace("J", "I")
    res = ""
    i = 0

    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                if text[i] == 'X':
                    res += text[i] + 'Z'
                else:
                    res += text[i] + 'X'
                i += 1
            else:
                res += text[i] + text[i + 1]
                i += 2
        else:
            if text[i] == 'Z':
                res += text[i] + 'X'
            else:
                res += text[i] + 'Z'
            i += 1

    return res


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2: 
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_encrypt(key, plain_text):
    matrix = grid_of_letters(key)
    prepared = prepare_text(plain_text)

    cipher = ""
    for i in range(0, len(prepared), 2):
        cipher += encrypt_pair(matrix, prepared[i], prepared[i + 1])

    return cipher



key = "MONARCHY"
plain_text = "INSTRUMENTS"

cipher = playfair_encrypt(key, plain_text)

print("Matrix:\n", grid_of_letters(key))
print("\nPrepared Text:", prepare_text(plain_text))
print("\nCipher Text:", cipher)