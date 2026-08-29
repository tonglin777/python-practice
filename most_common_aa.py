from amino_acid_counter import amino_acid_counter

def most_common_aa(sequence):
    counts = amino_acid_counter(sequence)
    winning_letter = max(counts, key=counts.get)
    winning_count = counts[winning_letter]
    return winning_letter, winning_count

if __name__ == "__main__":
    sequence = input("Enter a protein sequence: ")
    letter, count = most_common_aa(sequence)
    print("The most common amino acid is", letter, ", appearing", count, "times." )