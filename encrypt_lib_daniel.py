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
    test_message = my_file.readlines()
    return test_message

def convert_chunk_into_number(chunk_of_string):
    """
    Take in a chunk of a string and then convert it
    into a number using UTF-8 encoding.  return that number
    """
    # TODO: Daniel
    my_file = open("C:/Users/Triqk/github/RSAProject1/TestFile.txt", "r")
    test_message = my_file.readlines()
    number = int(text_message)
    return number



def rsa_encrypt_number(number, public_key):
    # TODO: Daniel

    #EKEY = (65537,100746831503809)
    EKEY = [65537 , 100746831503809]
    Exponent = EKEY[0]
    mod_n = EKEY[1]
    message = 5
    #EKEY = 65537
    #mod_n = 100746831503809
    #  PRIVATE_KEY = (47502589681765,100746831503809)
    encrypted_number = (message ** Exponent) % mod_n
    return encrypted_number

def rsa_encrypt_numbers(numbers, public_key):
    """
    numbers is a list of numbers.
    Iterate thru them all and encrypt each number
    Put the result in a list and then return the list
    """
    # TODO: Daniel

    encrypted_numbers = [1,2,3,4,5]

    return encrypted_numbers
