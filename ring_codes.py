"""
Generate codes for circular coded photogrammetry targets.
Implementation of coding scheme of (expired) patent DE19733466A1.
https://patents.google.com/patent/DE19733466A1/

Original:
Matthew Petroff (2018) Photogrammetry Targets.
https://mpetroff.net/2018/05/photogrammetry-targets/

Python implementation by Claude
"""

def bitwise_rotate_left(val: int, bits: int, total_bits: int) -> int:
    """Perform a bitwise rotation to the left."""
    return ((val << bits) & (2**total_bits - 1)) | ((val & (2**total_bits - 1)) >> (total_bits - bits))

def find_smallest_rotation(val: int, total_bits: int) -> int:
    """Check all bitwise rotations to find smallest representation."""
    smallest = val
    for i in range(1, total_bits):
        smallest = min(bitwise_rotate_left(val, i, total_bits), smallest)
    return smallest

def calc_parity(val: int) -> bool:
    """Returns True if even parity, else False."""
    parity = True
    while val:
        parity = not parity
        val = val & (val - 1)
    return parity

def count_bit_transitions(val: int) -> int:
    """Count number of bit transitions."""
    transitions = 0
    prev_bit = 0
    while val:
        new_bit = val & 1
        if new_bit > prev_bit:
            transitions += 1
        prev_bit = new_bit
        val = val >> 1
    return transitions

def get_ring_codes(bits: int, transitions: int = -1) -> list:
    """
    Generate codes for a given number of bits and, optionally, a given number
    of transitions. Number of bits should be even.
    """
    if bits < 0:
        raise ValueError('Number of bits must be positive!')
    
    if bits % 2 != 0:
        raise ValueError('Number of bits must be even!')
    
    if transitions < -1:
        raise ValueError('Number of transitions must be positive!')

    codes = []
    half_bits = bits >> 1

    for i in range(0, 2**(bits-2)):
        code = (i << 1) + 1
        code = find_smallest_rotation(code, bits)

        # Check if lower and upper halves share bits
        lower = code & (2**half_bits - 1)
        upper = (code & ((2**half_bits - 1) << half_bits)) >> half_bits
        diff = lower & upper

        parity = calc_parity(code)

        num_transitions = -1
        if transitions != -1:
            num_transitions = count_bit_transitions(code)

        if (parity and diff > 0 and transitions == num_transitions and code not in codes):
            codes.append(code)

    return codes 