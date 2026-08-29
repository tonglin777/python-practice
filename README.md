# Bioinformatics Python Scripts
A small collection of python scripts I wrote whilst learning to code, applying python fundamentals to basic bioinformatics.

## Scripts

### `gc_content.py`
Calculates the GC content of a DNA sequence as a percentage.
```python
from gc_content import gc_content
gc_content("ATGCGATCGA")
# Output: GC content: 60.00%
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
# Output: Number of point mutations: 3
```