def encryption(S, n):
    int(n)
    S.lower()
    encrypted_string = ""
    for i in S:
        if i.isalpha() == True:
            a = ord(i) - 97
            a += n
            a = a % 26
            encrypted_string += chr(a + 97)
        else:
            encrypted_string += i
    encrypted_string += str(n)
    return encrypted_string


print(encryption('Hi my name is Leslie', 18))


def decryption(W):
    W = list(W)
    shift = ''
    while W[-1] in '1, 2, 3, 4, 5, 6, 7, 8, 9, 0':
        shift = W.pop() + shift
    shift = int(shift)
    decrypted_string = ''
    for char in W:
        if char == " ":
            decrypted_string = decrypted_string + char
        else:
            decrypted_string = decrypted_string + chr((ord(char) - shift - 97) % 26 + 97)
    str(decrypted_string)
    return decrypted_string


print(decryption("zwddg wnwjqtgvq18"))
