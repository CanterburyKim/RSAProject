"""
Encryption Test
"""

import encrypt_lib
from encrypt_lib import *

<<<<<<< HEAD
# def test_get_message():
    # TODO: Daniel
test_message = get_message()
print (test_message)

# def test_convert_chunk_into_number(chunk_of_string):
# TODO: Daniel
#the value 10 is just indicating that there is another line "line space"
#is what it is called
test_list = []
test_list = (test_message)

for msg in test_list:
    test_number = convert_chunk_into_number(msg)
    print (test_number)

=======
def test_get_message():
    # TODO: Daniel
    pass

def test_get_encryption_key(filename):
    # TODO: Xander
    pass

def test_split_message_into_chunks(message):
    # TODO: Kevin
    pass

def test_convert_chunk_into_number(chunk_of_string):
    # TODO: Daniel
    pass

def test_convert_chunks_into_numbers(chunks_of_strings):
    # TODO: Kevin
    pass
>>>>>>> 82b64457321c9542815dbe83ce75404f540b93dd

def test_rsa_encrypt_number(number, public_key):
    # TODO: Daniel
    pass
<<<<<<< HEAD
=======

def test_rsa_encrypt_numbers(numbers, public_key):
    # TODO: Xander
    pass

def test_base64_encode_numbers(numbers):
    # TODO: Kevin
    pass

def test_save_encrypted_string(cipher_text):
    # TODO: Xander
    pass
>>>>>>> 82b64457321c9542815dbe83ce75404f540b93dd
