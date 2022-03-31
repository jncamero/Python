########################################################################################        
import pandas as pd
from pysam import FastaFile
import numpy as np
import os

def flank_seq(freg,snpfile,varfile,Ref):
    flanks=pd.read_csv(varfile,header=None)
    outfile = open("Markers.fasta", "a")
    with open(snpfile) as f:
        ref=FastaFile(fasta)
        for line in f:
            fname = line.rstrip().split(',') #using rstrip to remove the \n
            chr=fname[0]
            pos=int(fname[1])
    #Filter polymorphic regions upstream and downstream from SNP
            subs=flanks[(flanks.iloc[:,0]==chr)&(flanks.iloc[:,1]>pos-freg)&(flanks.iloc[:,1]<pos+freg)]
            subs2=subs.sort_values(by=1, ascending=False)
            l1=">"+chr+":"+str(pos-freg)+"-"+str(pos-1)
            left=ref.fetch(chr,pos-freg,pos) 
            l2=">"+chr+":"+str(pos)+"-"+str(pos)
            snp = "["+fname[2]+"/"+fname[3]+"]"       
            l3=">"+chr+":"+str(pos+1)+"-"+str(pos+freg)
    #Pull flanking sequence from fasta
            right=ref.fetch(chr,pos+1,pos+1+freg)
            if subs2.shape[0]>0:
                for i in range(0,subs2.shape[0]):
                    x = subs2.iloc[i,:]
                    if x.iloc[1]<pos:
                        #print("left")
                        #Position of SNP in string
                        a=(freg)-(pos-x[1])              
                        fs=pos-freg
                        left=left[0:a]+"["+x[2]+"/"+x[3]+"]"+left[(a+1):(pos+freg)]
                    elif x.iloc[1]>pos: 
                        #print('right')
                        #Position of flanking SNP in string
                        a=(freg)-(freg-(x[1]-pos))-1 
                        right=right[0:a]+"["+x[2]+"/"+x[3]+"]"+right[(a+1):(pos+freg)]
            lines=l1,"\n",left,"\n",l2,"\n",snp,"\n",l3,"\n",right,"\n"
            outfile.writelines(lines)
    outfile.close()
    return(0)
