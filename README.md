
**Python functions for manipulating sequence data**

**flank_seq**

This function takes 4 inputs
1) The length of sequence to return upstream and downstream from each SNP
 
2) A csv bed file indicating known variant positions, and the allelic variants at that locus

3) A csv bed file indicating the SNP positions for which you want annotated flanking sequence data returned  

4) A reference sequence fasta file (which has been indexed with samtools via: samtools faidx Reference.file)
Example:
#load the flank_seq.py

#Set directory to the path with the 3 test files

