# Bioinformatics Python Scripts
A small collection of python scripts I wrote whilst learning to code, applying python fundamentals to basic bioinformatics

## Scripts

### 'gc_content.py'
Calculates the GC content of a DNA sequence as a percentage.
'''python
from gc_content import gc_content
gc_content("ATGCGATCGA")
# Output: 60.0
'''

### 'codon_translator.py"
Translates a DNA sequence (or list of sequences) into amino acids using the standard genetic code.
'''python
from codon_translator import translated
translate("ATGGCACTC")
# Output: 'MAL'
'''