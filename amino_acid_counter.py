def amino_acid_counter(sequence):
    """Counts the occurrences of each amino acid in a protein sequence."""
    counts = {} # Empty dictionary
    for amino_acid in sequence.upper():
        if amino_acid in counts:
            counts[amino_acid] += 1
        else:
            counts[amino_acid] = 1 # Builds up dictionary when looping through sequence
    return counts

if __name__ == "__main__":
    sequence = input("Enter a protein sequence: ")
    print(amino_acid_counter(sequence))