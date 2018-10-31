from generate_lib import *

def test_pick_two_random_prime():
    print('test pick 2 random primes')
    print( pick_two_random_primes() )

def test_calculate_n():
    print('test calculate n')
    p=3
    q=7
    print( calculate_n(p,q) )

def test_calculate_phi():
    print('test calculate phi')
    p=3
    q=7
    print(calculate_phi(p,q))

def test_calculate_d():
    print('test calculate d')

    e=65537
    phi=33
    print( calculate_d(e,phi))

def test_generate_public_key():
    print('test generate public key')
 
    enc_exponent =65537
    modulus = 3200
    print( generate_public_key(enc_exponent, modulus))

def test_generate_private_key():
    print('test generate private key')

    dec_exponent = 77
    modulus =13
    print( generate_private_key( dec_exponent, modulus))

def test_save_public_key_to_file():
    print('test save public key to file ')
    public_key = (5,7)
    filename='test_public_key.txt'
    save_public_key_to_file(public_key, filename)

def test_save_private_key_to_file():
    print('test save private key to file ')
    private_key=(3,5)
    filename='test_private_key.txt'
    save_private_key_to_file(private_key, filename)

def test_extended_euclidean_algorithm():
    print('test extended euclidean algo ')

    e=65537
    phi=33
    print( extended_euclidean_algorithm(e,phi))

test_calculate_phi()
