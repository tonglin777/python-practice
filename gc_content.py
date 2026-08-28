def GC_content(sequence): # Create a function
    total_GCs = 0
    for nucleotide in sequence.upper():
        if nucleotide == "G" or nucleotide == "C":
            total_GCs += 1
    return (total_GCs / len(sequence)) * 100

if __name__ == "__main__":
    sequence = input("Enter a DNA sequence: ")
    print(f"GC content: {round(GC_content(sequence), 2)}%")

# Use "from gc_content import GC_content"