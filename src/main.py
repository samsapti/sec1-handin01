#!/usr/bin/env python3

import random

g = 666
p = 6661
group = range(p - 1)

def encrypt(pk, m):
    r = random.choice(group)
    c1 = (g ** r) % p
    c2 = ((pk ** r) * m) % p
    
    return (c1, c2)


def decrypt(sk, c):
    s = (c[0] ** sk) % p
    m = (c[1] * (s ** (p - 2))) % p

    return m


# Part one: Send '2000' to Bob

print("** Part one: **")

bob_pk = 2227

m = 2000
c = encrypt(bob_pk, m)

print("Alice's plaintext message reads:", m)
print("Alice sends the following ciphertext to Bob:", c)


# Part two: Intercept Alice's message

print("\n** Part two: **")

bob_sk = 0

for sk in group:
    if (g ** sk) % p == bob_pk:
        bob_sk = sk
        break

print("Eve finds Bob's secret key using a brute-force attack:", bob_sk)
print("Eve decrypts Alice's message:", decrypt(bob_sk, c))


# Part three

print("\n** Part three: **")

modified_c = (c[0], c[1] * 3)
modified_m = decrypt(bob_sk, modified_c)

print("Mallory successfully modifies Alice's ciphertext:", modified_c)
print("Bob decrypts the modified ciphertext:", modified_m)
