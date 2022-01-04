import sys, os
from typing import List

def bitsToString(bits):
    # join the bits to form a string
    return "".join(map(lambda x: str(x), bits))

def unsigned_to_denary(unsigned_bits: List[int]):
    base = 1
    res = 0
    i = len(unsigned_bits) - 1
    while i >= 0:
        res += unsigned_bits[i] * base
        i -= 1
        base *= 2
    return res

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