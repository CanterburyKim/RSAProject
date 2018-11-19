"""
Generate RSA Public and Private Keys library
Contains functions that will allow for
generation of public key, private key pair
and then save those to file
"""
import base64
import encrypt_lib
def calculate_d(e, phi):
    #"""
    #given the e and phi use the RSA formula to calculate
    #d.
    d_old = 0
    r_old = phi
    d_new = 1
    r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None




    #formula : e * d = 1 mod phi
    #"""
    # TODO: Alex
    pass
    # TODO use the RSA method to calculate d from e and phi

    #for d in range(phi):
    #    if (e * d) % phi == 1:
    #        print ('d =', d)
    #        print ('yes')




    return d


def save_public_key_to_file(public_key, filename):
    #"""
    #Need to use two supporting functions:
    #(a) encode number(public_key) to base64
    #(b) save base64 encoded number to file
    #"""
    # TODO: Alex
    # TODO encode public key to base64

    # TODO save base64 encoded privaet key to file

    encryption_exponent_in_bytes = (public_key[0]).to_bytes(7, byteorder='big')
    encoded_e_exponent_in_bytes = base64.b64encode(encryption_exponent_in_bytes)

    modulus_in_bytes = (public_key[1].to_bytes(7, byteorder='big'))
    encoded_modulus_in_bytes = base64.b64encode(modulus_in_bytes)

    with open(filename, 'w') as f:
        f.write(encoded_e_exponent_in_bytes.decode('utf-8'))
        f.write('\n')
        f.write(encoded_modulus_in_bytes.decode('utf-8'))

public_key = (47502589681765,100746831503809)
filename = 'outputfile.txt'
save_public_key_to_file(public_key, filename)











pass



#if __name__ == '__main__':
#    calculate_phi( *pick_two_random_primes())
