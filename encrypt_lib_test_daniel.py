from encrypt_lib_daniel import *

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


def test_rsa_encrypt_number(number, public_key):
    # TODO: Daniel
    pass
