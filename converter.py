import sys, os
from typing import List

def bitsToString(bits):
    # join the bits to form a string
    return "".join(map(lambda x: str(x), bits))

def signed_to_twos_complement(signed_bits: List[int]) -> List[int]:
    # 1. flip all the digits
    for i in range(len(signed_bits)):
        if signed_bits[i] == 1:
            signed_bits[i] = 0
        elif signed_bits[i] == 0:
            signed_bits[i] = 1

    # 2. add one to the number
    stringified = str(signed_bits)
    with_one_added = bin(int(stringified, 2) + 1)
    ## Removing the binary indicators in front eg. `0b1001` => `1001`
    ## and converting the resulting string to a list of integers
    bits = list(map(lambda x: int(x), list(with_one_added[2:])))

    return bits


def unsigned_to_denary(unsigned_bits: List[int]):
    base = 1
    res = 0
    i = len(unsigned_bits) - 1
    while i >= 0:
        res += unsigned_bits[i] * base
        i -= 1
        base *= 2
    return res

def signed_to_denary(signed_bits: List[int]):
    # if the left most digit of the binary number
    # is one, it's negative
    if signed_bits[0] == 1:
        twos_complement = signed_to_twos_complement(signed_bits)
        return unsigned_to_denary(twos_complement) * -1
    else:
        # it's positive, just treat it like an unsigned binary number
        # because an unsigned number is positive, and the most significant digit is zero(thus the calculation won't be affected)
        return unsigned_to_denary(signed_bits)

def denary_to_unsigned(denary: int):
    # reject negative values
    if denary < 0:
        return []
    # use an array to represent bits
    bits = []

    quotient = denary
    while quotient != 0:
        remainder = quotient % 2
        bits.insert(0, remainder)
        quotient = int(quotient / 2)
    return bitsToString(bits)

def main():

    formats = ["unsigned-binary", "signed-binary", "twos-complement", "denary"]

    from_format = input("From: ")
    to_format = input("To: ")

    if from_format not in formats:
        print(f"Accepted `from` values: {formats}")
        return
    if to_format not in formats:
        print(f"Accepted `to` values: {formats}")
        return

    input_val = input("Input number/binary: ")

    if from_format == "denary":
        input_val = input(input_val)
        if to_format == "unsigned-binary":
            print(denary_to_unsigned(input_val))
    if from_format == "unsigned-binary":
        input_val = list(map(lambda x: int(x), list(input_val)))
        if to_format == "denary":
            print(unsigned_to_denary(input_val))

if __name__ == "__main__":
    main()