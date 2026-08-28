def GC_content(sequence): # Create a function
    """Calculates the GC content of a DNA sequence as a percentage."""
    total_GCs = 0
    # Variable starting at 0 and accumulates
    for nucleotide in sequence.upper():
        # Loops through sequence one character at a time
        # .upper() converts whole sequence to uppercase first
        if nucleotide == "G" or nucleotide == "C":
            total_GCs += 1
    return (total_GCs / len(sequence)) * 100

if __name__ == "__main__":
    # Code is only run directly, not if imported from this file
    sequence = input("Enter a DNA sequence: ")
    print(f"GC content: {round(GC_content(sequence), 2)}%")
    # f string inserts variable's value inbetween texts
    # Rounded to 2 decimal places

# Use "from gc_content import GC_content"