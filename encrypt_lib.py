"""
This is the Encryption Library module
"""

def get_message():
    """
    Open a file
    Read the message from the file
    return that message
    """
    # TODO: Daniel
    my_file = open("C:/Users/Triqk/github/RSAProject1/TestFile.txt", "r")
    test_message = my_file.read().rstrip()
    return test_message


def convert_chunk_into_number(chunk_of_string):

    """
    Take in a chunk of a string and then convert it
    into a number using UTF-8 encoding.  return that number
    """
    # TODO: Daniel

    str_msg = []
    str_msg = (chunk_of_string)
    input_msg = []

    for char in str_msg:
        input_msg.append(ord(char))

    my_number = input_msg

    return my_number




def rsa_encrypt_number(number, public_key):
    # TODO: Daniel

    #EKEY = (65537,100746831503809)
    Exponent = public_key[0]
    mod_n = public_key[1]
    #EKEY = 65537
    #mod_n = 100746831503809
    #  PRIVATE_KEY = (47502589681765,100746831503809)
    encrypted_number = (number ** Exponent) % mod_n
    return encrypted_number

def rsa_encrypt_numbers(numbers, public_key):
    Exponent = public_key[0]
    mod_n = public_key[1]
    #EKEY = 65537
    #mod_n = 100746831503809
    #  PRIVATE_KEY = (47502589681765,100746831503809)
    encrypted_numbers = (numbers ** Exponent) % mod_n
    # TODO: Daniel
    return encrypted_numbers
