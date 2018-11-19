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

    decription_exponent_in_bytes = (private_key[0]).to_bytes(7, byteorder='big')
    encoded_d_exponent_in_bytes = base64.b64encode(decription_exponent_in_bytes)

    modulus_in_bytes = (private_key[1].to_bytes(7, byteorder='big'))
    encoded_modulus_in_bytes = base64.b64encode(modulus_in_bytes)

    with open(filename, 'w') as f:
        f.write(encoded_d_exponent_in_bytes.decode('utf-8'))
        f.write('\n')
        f.write(encoded_modulus_in_bytes.decode('utf-8'))

private_key = (47502589681765,100746831503809)
filename = 'outputfile.txt'
save_private_key_to_file(private_key, filename)







# ni = 6
# ni = ni.encode('utf-8')
# yes = base64.b64decode(ni)
# print(yes)

def read_key_from_file(filename):
    with open(filename, 'r') as f:
        my_lines = f.read().splitlines()
        print(my_lines)
        exponent = base64.b64decode(my_lines[0])
        exp_good = int.from_bytes(exponent, byteorder='big')

        mod = base64.b64decode(my_lines[1])
        mod_good = int.from_bytes(mod, byteorder='big')

        key = (exp_good, mod_good)
    return(key)

print(read_key_from_file(filename))


# if __name__ == '__main__':
#     calculate_phi( *pick_two_random_primes())
