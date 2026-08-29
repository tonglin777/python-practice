# Bioinformatics Python Scripts
A small collection of Python scripts I wrote whilst learning to code, applying Python fundamentals to basic bioinformatics.

## Scripts

### `gc_content.py`
Calculates the GC content of a DNA sequence as a percentage.
```python
from gc_content import gc_content
gc_content("ATGCGATCGA")
# Output: 'GC content: 60.00%'
```

### `codon_translator.py`
Translates a DNA sequence (or list of sequences) into amino acids using the standard genetic code.
```python
from codon_translator import translate
translate("ATGGCACTC")
# Output: 'MAL'
```

### `point_mutation_counter.py`
Counts the number of point mutations (differing positions) between two equal-length sequences.
```python
from point_mutation_counter import count_mutations
count_mutations("GAGCCT", "CATCGT")
# Output: 'Number of point mutations: 3'
```

### `reverse_complement.py`
Returns the reverse complement of a DNA sequence.
```python
from reverse_complement import reverse_complement
reverse_complement("ATGC")
# Output: 'The reverse complement of ATGC is GCAT'
```

### `consensus_sequence.py`
Builds a position frequency matrix from a list of aligned sequences and generates the consensus sequence.
```python
from consensus_sequence import consensus_sequence
consensus_sequence("ATCCAACT", "GGGCAACT", "ATGGATCT")
# Output: 'Consensus sequence: ATGCAACT'
```
### `amino_acid_counter.py`
Counts how many times each amino acid appears in a protein sequence.
```python
from amino_acid_counter import amino_acid_counter
amino_acid_counter("MALWMRLLPLLALLALWGPD")
# Output: '{'M': 2, 'A': 3, 'L': 8, 'W': 2, 'R': 1, 'P': 2, 'G': 1, 'D': 1}'

Working through these codes built up my confidence with loops, dictionaries, string manipulation, and writing reusable functions. I started off writing simple codes for my university Python session and extended it into my own standalone tools.