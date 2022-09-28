#!/usr/bin/env python3

import random

g = 666
p = 6661
group = range(p - 1)


def encrypt(pk, m):
    r = random.choice(group)
    c1 = (g ** r) % p
    c2 = (pk ** r * m) % p
    return (c1, c2)


def decrypt(sk, c1, c2):
    s = (c1 ** sk) % p
    m = (c2 * (s ** (p - 2))) % p
    return m


# Part one: Send '2000' to Bob

bob_pk = 2227

m = 2000
c = encrypt(bob_pk, m)

print("Alice's plaintext message reads: ", m)
print("Alice sends the following ciphertext to Bob: ", c)
