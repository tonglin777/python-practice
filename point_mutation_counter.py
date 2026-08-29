def count_mutations(seq1, seq2):
    """Counts the number of point mutations between two DNA sequences of equal length."""
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be the same length to compare point mutations.")
        # Stops execution

    mutations = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutations += 1
    return mutations

if __name__ == "__main__":
    while True:
    # Conditional loop is fixed on True until exit mechanism 'break'
        seq1 = input("Enter the first DNA sequence: ")
        seq2 = input("Enter the second DNA sequence: ")

        try:
            print("Number of point mutations:", count_mutations(seq1, seq2))
            break # Exits loop after sucessful print, without raising error
        except ValueError as error:
            print(error)
            print("Please try again.\n")