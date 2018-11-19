"""
Encryption Test
"""

import encrypt_lib
from encrypt_lib import *

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


def rsa_encrypt_number(number , public_key):
#    number = 6
#    public_key = (65537 , 100746831503809)
    exponent = public_key[0]
    mod_n = public_key[1]
    encrypted_number = (number ** exponent) % mod_n
    return encrypted_number


def rsa_encrypt_numbers(numbers, public_key):
    encrypted_numbers = [];
    for n in numbers:
        #public_key = (65537 , 100746831503809)
        encrypted_number = rsa_encrypt_number(n, public_key)
        encrypted_numbers.append(encrypted_number)
    #    print (encrypted_number)
    return encrypted_numbers

numbers = [1, 2, 3, 4]
public_key = (65537 , 100746831503809)
encrypted_numbers = rsa_encrypt_numbers(numbers, public_key)
print (encrypted_numbers)
