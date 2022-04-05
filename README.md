
# **Python functions for manipulating sequence data**

## **flank_seq**

This function takes 4 inputs
1) The length of sequence to return upstream and downstream from each SNP
 
2) A csv bed file indicating **known variant positions**, and the allelic variants at that locus

3) A csv bed file indicating the **SNP positions** for which you want annotated flanking sequence data returned  

4) A **reference sequence fasta file** (which has been indexed with samtools via (i.e. in SHELL): samtools faidx Reference.file)
Example:
#load the flank_seq.py

#Set directory to the path with the 3 test files

############################################################
##########Example
############################################################

#Variant bed file

varfile="var.bed.csv"

#Reference file

fasta="Ref.fasta"

#SNP file

snpfile="SNP.bed.csv"

#Length of sequence to return on either side of SNPs from SNP file

freg=10

#Run Function (make sure you have write privileges in the directory you're in).
flank_seq(freg,snpfile,varfile,fasta)

#Read in the output from flank_seq

 hold=[];

    for line in open('Markers.fasta'):  
    
    hold.append(line.rstrip('\n')) 

#Check to see that annotated and fetched sequences from reference file are identical (except for indicated variants)

ref=FastaFile(fasta)

Position of first SNP

hold[0]

'>seq1:5-14'

#Lef-flanking sequence of first SNP

hold[1]

'AC[A/C]TTCGTCG'

ref.fetch("seq1",5,14+1)

'ACCTTCGTCG'

hold[3]

'>seq1:16-25'

hold[4]

'CTCCACT[A/C]TT'

ref.fetch("seq1",16,25+1)

'CTCCACTCTT'
