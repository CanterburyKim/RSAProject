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

    test_message = 'Hello this is a test'
    return test_message

def convert_chunk_into_number(chunk_of_string):
    """
    Take in a chunk of a string and then convert it
    into a number using UTF-8 encoding.  return that number
    """
    # TODO: Daniel
    number = 7
    return number



def rsa_encrypt_number(number, public_key):
    """
    take a number and then use the rsa formula to encrypt it
    using the public key
    """
    # TODO: Daniel
    encrypted_number = 22

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
