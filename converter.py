import sys, os

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

    # join the bits to form a string
    return "".join(map(lambda x: str(x), bits))

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

    from_num = int(input("Input number: "))

    if from_format == "denary":
        if to_format == "unsigned-binary":
            print(denary_to_unsigned(from_num))

if __name__ == "__main__":
    main()