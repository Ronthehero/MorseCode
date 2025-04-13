#!/usr/bin/env python3

import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

INVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encode(message):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in message)

def decode(morse_code):
    return ''.join(INVERSE_MORSE_CODE_DICT.get(code, '') for code in morse_code.split())

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 morsecode.py [-e|-d] <message>")
        return

    mode = sys.argv[1]
    message = ' '.join(sys.argv[2:])

    if mode == '-e':
        print(encode(message))
    elif mode == '-d':
        print(decode(message))
    else:
        print("Unknown option:", mode)
        print("Use -e to encode or -d to decode.")

if __name__ == '__main__':
    main()
