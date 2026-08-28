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

def translated_sequence(sequence):
    """Translates a single DNA sequence into a protein string."""
    # Docstring "help(translated_sequence)" for the function
    protein = str()
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3] # String slicing to split DNA sequence into codons
        protein += codons[codon]
    return protein

def translate(input_data):
    """Accepts either a single sequence (str) or s list of sequences."""
    if isinstance(input_data, list):
        # Same function works for one sequence or many
        return [translated_sequence(seq) for seq in input_data]
    else:
        return translated_sequence(input_data)

if __name__ == "__main__":
    sequence = input("Enter a DNA sequence: ")
    print(translate(sequence))