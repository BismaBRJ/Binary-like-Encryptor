"""
Binary-like Encryptor
By: Bisma Rohpanca Joyosumarto

This program encrypts a message using only 2 characters, 1 and 0, making it look
like binary, although it isn't.

Available functions are encrypt(message) and decrypt(encryption), which are
self-explanatory.
"""

from sys import platform as _platform
if _platform == "win32":
    from keyhandlers import caesar_cipher
elif _platform == "darwin":
    pass

def encrypt(message):
    List = []

    # Message >> list of each character's ordinal value

    for character in message:
        List.append(ord(character))

    # List of each character's ordinal value
    # >> those values, broken down into sums of scientific notation
    
    # (Sometimes the author just doesn't remember the algorithm for this step.)
    
    # For each place value of the number, this is the scientific notation
    # formula:
    
    # 10**number_length *
    # ((number % 10**(current_place_value + 1)) -
    # (number % 10**current_place_value))
    
    # Where current_place_value would be the power of ten used for a value in
    # that place. (Ones = 0, Tens = 1, Hundreds = 2, Thousands = 3, etc.)

    old_list = List[:]
    List = []

    for value in old_list:
        value_length = len(str(value))
        sum_of_scientific_notation = ""
        for current_digit in range(value_length - 1, -1, -1):
            multiplier = (value % (10**(current_digit + 1))) - (value % (10**
                                                              current_digit))
            multiplier = int(str(multiplier)[0])
            sum_of_scientific_notation += ("10**" + str(current_digit) + " * "
                                           + str(multiplier) + " + ")
        sum_of_scientific_notation = sum_of_scientific_notation[:len(
            sum_of_scientific_notation) - 3]
        List.append(sum_of_scientific_notation)

    # Sums of scientific notations >> Encryption
    # Encryption:
    # 01...01 = str((len(01...01) / 2) - 1)
    # 001 = "10**"
    # 0001 = " * "
    # 00001 = " + "
    # 000001 = ,

    Encryption = "1"
    # The first character of this encryption is always 1, making it look like
    # binary.
    
    is_number = False
    # Bool to check whether the next character is a number and should be
    # encrypted as such: 01...01
    
    sum_of_scientific_notation = List[0]
    List = List[1:]

    while True:
        if sum_of_scientific_notation[0:4] == "10**":
            sum_of_scientific_notation = sum_of_scientific_notation[4:]
            Encryption += "001"
            is_number = True
        elif sum_of_scientific_notation[0:3] == " * ":
            sum_of_scientific_notation = sum_of_scientific_notation[3:]
            Encryption += "0001"
            is_number = True
        elif sum_of_scientific_notation[0:3] == " + ":
            sum_of_scientific_notation = sum_of_scientific_notation[3:]
            Encryption += "00001"
            is_number = False
        elif sum_of_scientific_notation == "" and List == []:
            break
        elif sum_of_scientific_notation == "":
            sum_of_scientific_notation = List[0]
            List = List[1:]
            Encryption += "000001"
            is_number = False
        elif is_number:
            number = int(sum_of_scientific_notation[0])
            Encryption += "01"
            while number != 0:
                Encryption += "01"
                number = number - 1
            sum_of_scientific_notation = sum_of_scientific_notation[1:]
            is_number = True

    return Encryption

def decrypt(encryption):    
    # Is it a valid encryption?

    valid = True
    
    if encryption[0] != "1":
        valid = False
        
    # Tries to make it valid (if possible)

    if valid:
        current_index = 0
        indexes_to_remove = []
        done = False

        while True:
            try:
                current_character = encryption[current_index]
            except IndexError:
                done = True

            if done:
                break
        
            if (current_character == " " or
                current_character == "\a" or
                current_character == "\b" or
                current_character == "\t" or
                current_character == "\n"):
                indexes_to_remove.append(current_index)
            
            current_index += 1

        for current_index in indexes_to_remove:
            encryption = (encryption[0:current_index] +
                          encryption[current_index + 1:])

    # If it is simply not valid:

    if not valid:
        return "error"

    # Encryption >> Sums of scientific notations
    # Encryption:
    # 01...01 = str((len(01...01) / 2) - 1)
    # 001 = "10**"
    # 0001 = " * "
    # 00001 = " + "
    # 000001 = ,

    encryption = encryption[1:]
    List = "[\""

    while True:
        if encryption[0:2] == "01":
            encryption = encryption[2:]
            number = 0
            while encryption[0:2] == "01":
                encryption = encryption[2:]
                number += 1
            List += str(number)
        elif encryption[0:3] == "001":
            List += "10**"
            encryption = encryption[3:]
        elif encryption[0:4] == "0001":
            List += " * "
            encryption = encryption[4:]
        elif encryption[0:5] == "00001":
            List += " + "
            encryption = encryption[5:]
        elif encryption[0:6] == "000001":
            List += "\", \""
            encryption = encryption[6:]
        else:
            List += "\"]"
            break

    # Sums of scientific notations
    # >> List of each character's ordinal value

    old_list = eval(List)
    List = []

    try:
        for sum_of_scientific_notation in old_list:
            List.append(eval(sum_of_scientific_notation))
    except Exception:
        return ""

    # List of each character's ordinal value >> Message

    message = ""

    for value in List:
        message += chr(value)

    return message
