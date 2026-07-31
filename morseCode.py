#31-07-26
# Given a Morse code string, return the decoded message using the following table:
#
# Code   | Letter | Code   | Letter
# ---------------------------------
# .-     | A      | -.     | N
# -...   | B      | ---    | O
# -.-.   | C      | .--.   | P
# -..    | D      | --.-   | Q
# .      | E      | .-.    | R
# ..-.   | F      | ...    | S
# --.    | G      | -      | T
# ....   | H      | ..-    | U
# ..     | I      | ...-   | V
# .---   | J      | .--    | W
# -.-    | K      | -..-   | X
# .-..   | L      | -.--   | Y
# --     | M      | --..   | Z
#
# - Letters are separated by a single space
# - Words are separated by three spaces

morse_code = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}
def decode_morse(code):
    morse_str=""
    code_list=code.split("   ")
    for i in code_list:
        letter=i.split()
        for j in letter:
            morse_str+=morse_code[j]
        morse_str+=" "
    return morse_str[:-1]

code=input("Enter the Morse code: ")
print(decode_morse(code))