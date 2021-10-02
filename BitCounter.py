def countBits(n):
    return len("".join( b for b in bin(n)[2::] if b == '1'))

print countBits(2)


"""
Return the number of bits that are equal to ones in the binary representation a given number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
