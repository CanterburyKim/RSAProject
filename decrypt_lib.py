"""
This is the Decryption Library module
"""

def get_cipher_message():
    """
    Open a file
    Read the message from the file (which is base64 encoded)
    """

    cipher_message = ['ViKvTvBn','IS7Cp8kV','QVK6xAVB','QJfEaCiG]']

    return cipher_message

def get_decryption_key(filename): 
    """
    open the file with the filename
    know the format
    read in the exponent and modulus
    return a 2-tuple of exponent and modululs
    """
    decryption_key = (65537, 12)
    return decryption_key

def rsa_decrypt_number(number, private_key):
    """
    take a number and then use the rsa formula to decrypt it
    using the private key
    """

    decrypted_number = 22

    return decrypted_number

def rsa_decrypt_numbers(numbers, private_key):
    """
    numbers is a list of numbers.  
    Iterate thru them all and decrypt each number
    Put the result in a list and then return the list
    """
    decrypted_numbers = [1,2,3,4,5]

    return decrypted_numbers

def base64_decode_numbers(message_chunks):
    """
    takes list of message_chunk strings and then base64 decodes them
    """

    # TODO use library base64 encode function to encode
    # each of the numbers in the list

    base64_deoded_numbers= [4343,333,221,222]
    return base64_deoded_numbers

def convert_number_to_message_chunk(number):
    """
    takes a number and then converts it into a string
    """
    message_chunk = 'this is'

    return message_chunk

def convert_numbers_to_strings(numbers):
    """
    numbers is a list of numbers.
    Convert each of those into a string,
    put it into a list and return that list
    """
    

def assemble_message_from_chunks(message_chunks):
    """
    Take a long message and then split it into 
    5-character chunks.  Put those chunks into
    a list and then return that list
    """

    assembled_message = 'hello I must be going'
    return assembled_message