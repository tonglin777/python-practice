def build_pfm(sequences):
    # Builds the matrix
    """Builds a position frequency matrix from a list of equal-length DNA sequences."""
    pfm = list()
    for i in range(len(sequences[0])):
        counts = {"A": 0, "T": 0, "G": 0, "C": 0}
        for seq in sequences:
            counts[seq[i]] += 1
        pfm.append(counts)
    return pfm

def consensus_sequence(sequences):
    """Validates input and returns the consensus sequence for a list of DNA sequences."""
    if not isinstance(sequences, list):
        raise ValueError("Input must be a list of sequences.")
    if len(sequences) < 2:
        raise ValueError("There must be more than one sequence in the list.")
    if any(len(seq) != len(sequences[0]) for seq in sequences):
        # Checks if any sequences whose length doesn't match the first one's
        raise ValueError("All sequences must be the same length.")
        # Every sequence has to be aligned

    pfm = build_pfm(sequences)

    result = str()
    for position in pfm:
        result += max(position, key=position.get)
    return result

if __name__ == "__main__":
    # Quick check
    sequences = ["ATCCAGCT", "GGGCAACT", "ATGGATCT", "AAGCAACC", "TTGGAACT", "ATGCCATT", "ATGGCACT"]
    print("Consensus sequence:", consensus_sequence(sequences))

    # Interactive use
    sequences = list() # Empty list that builds up as sequences are entered

    print("Enter DNA sequences one at a time. Press Enter on a blank line when finished.")

    while True:
        seq = input("Enter a sequence: ")
        if seq == "":
            break
        sequences.append(seq) # Adds sequence inputs into growing list

    print("\nSequences entered:", sequences)
    print("Consensus sequence:", consensus_sequence(sequences))