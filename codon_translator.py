codons = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 
          'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 
          'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 
          'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R', 
          'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 
          'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 
          'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 
          'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R', 
          'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 
          'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A', 
          'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 
          'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 
          'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 
          'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L', 
          'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_', 
          'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

def translate_sequence(sequence):
    # Define function, input is sequence
    """Translates a single DNA sequence into a protein string."""
    # Docstring "help(translated_sequence)"
    protein = str()
    # Create an empty string, store variable in protein
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        # String slicing to split DNA sequence into codons
        protein += codons[codon]
        # Dictionary lookup to find corresponding amino acid
    return protein

def translate(input_data):
    # Deciding what to do, not direct translation
    """Accepts either a single sequence (str) or a list of sequences."""
    if isinstance(input_data, list):
        # Check if the type is a list
        # Same function works for one sequence or many
        return [translate_sequence(seq) for seq in input_data]
        # If TRUE
    else:
        return translate_sequence(input_data)

if __name__ == "__main__":
    # Quick tests
    print(translate("ATAATC")) # Single sequence
    print(translate(["ATAATC", "ATGGCA", "GGATCC"])) # List of sequences

    # Interative use
    sequence = input("Enter a DNA sequence: ")
    print(translate(sequence))