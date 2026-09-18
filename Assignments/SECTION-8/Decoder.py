'''Caesar Cipher
Build an encoder and a decoder for a Caesar cipher with a given shift.
Rules:
• Shift letters by the given amount, wrapping around (z + 1 -> a)
• Preserve case (uppercase stays uppercase, lowercase stays lowercase)
• Leave non-letters (spaces, digits, punctuation) unchanged
Demonstrate a round-trip: encode a message, then decode it back to the original to prove it matches

Hint: ord() and chr() convert between characters and their number codes.'''

def caesar(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            if char.islower():
                start = ord('a')
            else:
                start = ord('A')

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        else:
            result += char

    return result
message = "Python is fun"
shift = 2
encoded = caesar(message, shift)
decoded = caesar(encoded, -shift)
print("Original:", message)
print("Encoded:", encoded)
print("Decoded:", decoded)
print("Match:", message == decoded)