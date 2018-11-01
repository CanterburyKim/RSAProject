"""
Generate RSA Public and Private Keys library
Contains functions that will allow for
generation of public key, private key pair
and then save those to file
"""

def pick_two_random_primes():
    """
    Pick 2 random primes and then return them
    Currently, the random primes are of size
    ~10,000,000
    """
    # TODO: Leo
    pass
    # Temp values for p and q
    p = 10_000_019
    q = 10_000_079

    # TODO: pick 2 random primes and replace these values of p, q

    # TODO: look up random.choice (https://docs.python.org/3/library/random.html)


    return (p,q)

def calculate_n(p,q):
    """
    use the RSA formula to calculate n from p and q
    TODO fill in the RSA formula here
    """
    # TODO: David
    pass
    # temp value for n TODO remove this and replace with correct
    n = 100_000_980_001_501

    # TODO fill RSA formula for n here


    return n

def calculate_phi(p,q):
    """
    Use RSA formula to calculate phi from p and q
    TODO fill in the RSA formula here
    """
    # TODO: Nikita
    # Temp value for Phi.  TODO replace this
    phi = 100_000_960_001_404


    return phi

def calculate_d(e, phi):
    """
    given the e and phi use the RSA formula to calculate
    d.

    formula : e * d = 1 mod phi
    """
    # TODO: Alex
    pass
    # TODO use the RSA method to calculate d from e and phi

    d = 51_617_139_553_649

    return d

def generate_public_key(enc_exponent, modulus):
    """
    Use the encryption exponent and the modulus to
    create a 2-tuple that contains those two.
    """
    # TODO: Leo
    # temp value.  TODO change this to correct
    public_key = (1,1)

    return public_key


def generate_private_key(dec_exponent, modulus):
    """
    Use the decryption exponent and the modulus to create
    a 2-tuple that contains those two
    """
    # TODO: David
    # temp value.  TODO change this to correct
    private_key = (1,1)

    return private_key

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

def extended_euclidean_algorithm(e, phi):
    """
    Using the Extended Euclidean Algorithm to invert
    invert the form   e * d = 1 (mod phi)
    ref: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    # TODO: Leo
    # TODO look up the extended euclidean algorithm and use that pseudo code here

    # temp value for d.  TODO replace this with real value
    d = 17

    return d


def build_prime_number_list():
    """
    Take the comma separated list of prime numbers
    (acquired from Wolfram Alpha) from the file (ifname)
    and then save them to the outputfile (ofname)
    with 1 prime number per line
    """
    ifname = 'raw_primes.txt'
    ofname = 'primes.txt'




if __name__ == '__main__':
    calculate_phi( *pick_two_random_primes())
