def alphabet_position(letter):
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    position = alphabet.index(letter)
    return position

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_letter = ""

    if not char.isalpha():
        return char
    else:
       new_spot = alphabet_position(char)
       new_spot = new_spot + rot
       if new_spot < 26:
               new_letter = new_letter + alphabet[new_spot]
       else:
               new_letter = new_letter + alphabet[new_spot % 26]
    if char.islower():
        return new_letter
    else:
        return new_letter.upper()

def encrypt(text, rot):

    new_text = ""
    new_char = ""
    for char in text:
        if not char.isalpha():
            new_text = new_text + char
        else:
            new_char = rotate_character(char, rot)
            new_text = new_text + new_char
    return new_text
