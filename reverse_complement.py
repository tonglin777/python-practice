def reverse(sequence):
    """Reverses the input sequence."""
    return sequence[::-1]

def complement(sequence):
    """Returns the complement of a DNA sequence."""
    result = str()
    for nucleotide in sequence:
        if nucleotide == 'A':
            result += 'T'
        elif nucleotide == 'T':
            result += 'A'
        elif nucleotide == 'C':
            result += 'G'
        else:
            result += 'C'
    return result

def reverse_complement(sequence):
    """Returns the reverse complement of a DNA sequence."""
    return complement(reverse(sequence))

if __name__ == "__main__":
    sequence = input("Enter a DNA sequence: ")
    print("The reverse complement of", sequence, "is", reverse_complement(sequence))