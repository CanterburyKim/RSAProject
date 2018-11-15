import base64


"""
Generate RSA Public and Private Keys library
Contains functions that will allow for
generation of public key, private key pair
and then save those to file
"""



def calculate_phi(p,q):
    phi = (p-1)*(q-1)

    return phi



def save_private_key_to_file(private_key, filename):
    """
    Need to usei two supporting functions:
    (a) encode number(private_key) to base64
    (b) save base64 encoded number to file
    """

    decription_exponent_in_bytes = (private_key[0]).to_bytes(6, byteorder='big')
    encoded_d_exponent_in_bytes = base64.b64encode(decription_exponent_in_bytes)

    modulus_in_bytes = (private_key[1].to_bytes(6, byteorder='big'))
    encoded_modulus_in_bytes = base64.b64encode(modulus_in_bytes)

    with open(filename, 'w') as f:
        f.write(encoded_d_exponent_in_bytes.decode('utf-8'))
        f.write('\n')
        f.write(encoded_modulus_in_bytes.decode('utf-8'))

private_key = (47502589681765,100746831503809)
filename = 'outputfile.txt'
save_private_key_to_file(private_key, filename)





def save_private_key_to_file(private_key, filename):
    """
    Need to use two supporting functions:
    (a) encode number(private_key) to base64
    (b) save base64 encoded number to file
    """
    # TODO: Nikita
    # TODO encode private key to base64 (use lib code)

    # TODO save base64 encoded private key to file

    pass




def build_prime_number_list():
    """
    Take the comma separated list of prime numbers
    (acquired from Wolfram Alpha) from the file (ifname)
    and then save them to the outputfile (ofname)
    with 1 prime number per line
    """
    ifname = 'raw_primes.txt'
    ofname = 'primes.txt'




# if __name__ == '__main__':
#     calculate_phi( *pick_two_random_primes())
