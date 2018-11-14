"""
Generate RSA Public and Private Keys library
Contains functions that will allow for
generation of public key, private key pair
and then save those to file
"""


def calculate_d(e, phi):
    #"""
    #given the e and phi use the RSA formula to calculate
    #d.

    #formula : e * d = 1 mod phi
    #"""
    # TODO: Alex
    pass
    # TODO use the RSA method to calculate d from e and phi

    for d in range(phi):
        if (e * d) % phi == 1:
            print ('d =', d)
            print ('yes')




    return d


def save_public_key_to_file(public_key, filename):
    """
    Need to use two supporting functions:
    (a) encode number(public_key) to base64
    (b) save base64 encoded number to file
    """
    # TODO: Alex
    # TODO encode public key to base64

    # TODO save base64 encoded privaet key to file
    pass



#if __name__ == '__main__':
#    calculate_phi( *pick_two_random_primes())
