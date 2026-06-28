"""
Morse Code Translator

Author: Tomáš Nguyen
Created: 2026

A command-line application that translates
plain text to Morse code and vice versa.
"""

TO_MORSE_CODE_DICT = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",

    # Space
    " ": "/"
}
FROM_MORSE_CODE_DICT = {value: key for key, value in TO_MORSE_CODE_DICT.items()}

print("Welcome to the Morse Code Translator!\n")
print("Supported inputs:")
print("• Letters (A-Z)")
print("• Numbers (0-9)")
print("• Standard International Morse Code punctuation\n")
print("To translate Morse code:")
print("• Separate each character with a space.")
print("• Use '/' to represent spaces between words.\n")

while True:
    user_input = input("Type text you want to translate: ").upper()
    translated = []

    if set(user_input).issubset({'-', '.', ' ', '/'}):
        user_input = user_input.split()
        translation_dict = FROM_MORSE_CODE_DICT
        separator = ""
    else:
        translation_dict = TO_MORSE_CODE_DICT
        separator = " "

    for item in user_input:
        code = translation_dict.get(item)
        if code is None:
            print("\nInvalid input. Please try again.\n")
            break
        translated.append(code)
    else:
        print(f"Translation: {separator.join(translated)}")
