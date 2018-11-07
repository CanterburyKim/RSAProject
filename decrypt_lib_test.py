"""
   Unit test file for Decryption

"""
import unittest
import decrypt_lib


class TestDecryptMethods(unittest.TestCase):
    """
    Unit Test cases for the Decryption
    methods
    """
    def test_get_cipher_message(self):
        # TODO: Tyler
        pass
        

    def test_get_decryption_key(self):
        # TODO: Tyler
        filename = ''

        pass

    def test_rsa_decrypt_number(self):
        # TODO: Chase
        number = 6
        private_key = (5, 5)
        pass

    def test_rsa_decrypt_numbers(self):
        # TODO: Tyler
        numbers = []
        private_key = (3, 7)
        pass

    def test_base64_decode_numbers(self):
        # TODO: Tyler
        message_chunks = []
        pass

    def test_convert_number_to_message_chunk(self):
        # TODO: Chase
        number = 6
        pass

    def test_convert_numbers_to_strings(self):
        numbers = []
        # TODO: Joe
        pass

    def test_assemble_message_from_chunks(self):
        # TODO: Joe
        message_chunks = []
        pass


if __name__ == '__main__':
    unittest.main()
