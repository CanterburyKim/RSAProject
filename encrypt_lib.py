"""
This is the Encryption Library module
"""

def get_message():
    """
    Open a file
    Read the message from the file
    return that message
    """

    test_message = 'Hello this is a test'
    return test_message

def get_encryption_key(filename):
    """
    open the file with the filename
    know the format
    read in the exponent and modulus
    return a 2-tuple of exponent and modululs
    """
    encryption_key = (65537, 12)
    return encryption_key

def split_message_into_chunks(message):
    """
    Take a long message and then split it into 
    5-character chunks.  Put those chunks into
    a list and then return that list
    """

    chunks = ['this ', 'is a ', 'test ', 'chunk']
    return chunks

def convert_chunk_into_number(chunk_of_string):
    """
    Take in a chunk of a string and then convert it
    into a number using UTF-8 encoding.  return that number
    """

    number = 7
    return number

def convert_chunks_into_numbers(chunks_of_strings):
    """
    Takes in a list of chunks of strings and then
    convert them all into numbers.  Put those numbers
    into a list and return that list.
    """

    numbers = [7,5,6,4]

    return numbers


def rsa_encrypt_number(number, public_key):
    """
    take a number and then use the rsa formula to encrypt it
    using the public key
    """

    encrypted_number = 22

    return encrypted_number

def rsa_encrypt_numbers(numbers, public_key):
    """
    numbers is a list of numbers.  
    Iterate thru them all and encrypt each number
    Put the result in a list and then return the list
    """
    encrypted_numbers = [1,2,3,4,5]

    return encrypted_numbers

    
def base64_encode_numbers(numbers):
    """
    takes list of numbers and then base64 encodes them
    """

    # TODO use library base64 encode function to encode
    # each of the numbers in the list

    base64_encoded_strings= ['aaaaa','bcdef','ghtff']
    return base64_encoded_strings


