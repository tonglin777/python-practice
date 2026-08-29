def gc_content(sequence): # Create a function
    """Calculates the GC content of a DNA sequence as a percentage."""
    total_gcs = 0
    # Variable starting at 0 and accumulates
    for nucleotide in sequence.upper():
        # Loops through sequence one character at a time
        # .upper() converts whole sequence to uppercase first
        if nucleotide == "G" or nucleotide == "C":
            total_gcs += 1
    return (total_gcs / len(sequence)) * 100

if __name__ == "__main__":
    # Code is only run directly, not if imported from this file
    sequence = input("Enter a DNA sequence: ")
    print(f"GC content: {gc_content(sequence):.2f}%")
    # f string inserts variable's value inbetween texts
    # Rounded to a firxed 2 decimal places

# Use "from gc_content import GC_content"