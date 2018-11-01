"""
This is the Decryption Library module
"""

def get_cipher_message():
    """
    Open a file
    Read the message from the file (which is base64 encoded)
    """
    # TODO: Tyler
    cipher_message = ['ViKvTvBn','IS7Cp8kV','QVK6xAVB','QJfEaCiG]']

    return cipher_message

def get_decryption_key(filename):
    """
    open the file with the filename
    know the format
    read in the exponent and modulus
    return a 2-tuple of exponent and modululs
    """
    # TODO: Tyler
    decryption_key = (65537, 12)
    return decryption_key



    return decrypted_number

def rsa_decrypt_numbers(numbers, private_key):
    """
    numbers is a list of numbers.
    Iterate thru them all and decrypt each number
    Put the result in a list and then return the list
    """
    # TODO: Tyler
    decrypted_numbers = [1,2,3,4,5]

    return decrypted_numbers

def base64_decode_numbers(message_chunks):
    """
    takes list of message_chunk strings and then base64 decodes them
    """
    # TODO: Tyler
    # TODO use library base64 encode function to encode
    # each of the numbers in the list

    base64_decoded_numbers= [4343,333,221,222]
    return base64_decoded_numbers
