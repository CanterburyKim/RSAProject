"""
Encryption Test
"""
import unittest
import encrypt_lib

class TestEncryptMethods(unittest.TestCase):
    def test_get_message(self):
        # TODO: Daniel
        pass

    def test_get_encryption_key(self):
        # TODO: Xander
        filename = 'fname.ext'
        pass

    def test_split_message_into_chunks(self):
        # TODO: Kevin
        message='longmessage'
        pass

    def test_convert_chunk_into_number(self):
        # TODO: Daniel
        chunk_of_string=''
        pass

    def test_convert_chunks_into_numbers(self):
        # TODO: Kevin
        pass
        chunks_of_strings=[]

    def test_rsa_encrypt_number(self):
        # TODO: Daniel
        number=6
        public_key=(3,3)
        pass

    def test_rsa_encrypt_numbers(self):
        # TODO: Xander
        numbers=[]
        public_key=(3,3)
        pass

    def test_base64_encode_numbers(self):
        # TODO: Kevin
        numbers = []
        pass

    def test_save_encrypted_string(self):
        # TODO: Xander
        cipher_text = ''
        pass


if __name__ == '__main__':
    unittest.main()
