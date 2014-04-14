#Assignment_module.py

#read in fasta file and return contents in a tuple
def read_fasta_file(path):
    f = open(path,"r+")
    seq_name = f.readline()
    count =0
    full_seq = ""
    seq = f.readlines()

    for k in seq:
        if k[len(k)-1] == "\n":
            full_seq = full_seq + k[:len(k)-1:]
        else:
            full_seq = full_seq + k
    tpl = (seq_name[1:len(seq_name)-1],full_seq)
    return tpl

#Find the reverse complement of dna sequence
def reverse_complement(fwd_seq):
    comp = ""
    for k in fwd_seq:
        if k == "A":
            comp = comp + "T"
        elif k == "T":
            comp = comp + "A"
        elif k == "C":
            comp = comp + "G"
        elif k == "G":
            comp = comp + "C"
        else:
            print "Error in DNA sequence"
            break
    rev_comp_seq = comp[::-1]
    return rev_comp_seq

#Find the first open reading frame
def get_ORF(seq):
    orf = 0  
    flag1 = False
    flag2 = False
    while (flag1 == False or flag2 == False) and orf!=len(seq)-9:
        flag1 = False
        flag2 = False
        start = ""
        stop = ""
        orf_temp = orf
        
        while flag1 != True and orf_temp<=len(seq)-9:
            start = seq[orf_temp]+seq[orf_temp+1]+seq[orf_temp+2]
            if start == "ATG":
                flag1 = True
                break
            orf_temp = orf_temp + 3
        
        orf_temp2 = orf_temp + 3
        
        while flag1 == True and flag2 == False and orf_temp2<=len(seq)-3:           
            stop = seq[orf_temp2]+seq[orf_temp2+1]+seq[orf_temp2+2]
            if stop == "TAG" or stop == "TAA" or stop == "TGA":
                flag2 = True
                return orf
            orf_temp2 = orf_temp2 +3
            
        orf = orf + 1

    return -1 


#return the gene encoded by the ORF
def get_gene_by_ORF(seq,orf):
    if orf == -1:
        print "No open reading frame found"
        return -1
    
    flag1 = False
    flag2 = False
    stop = ""
    start = ""
    
    while flag1!=True:
        start = seq[orf]+seq[orf+1]+seq[orf+2]
        if start == "ATG":
            flag1 = True
            break
        orf = orf+3
        
    orf_stop = orf+3
    
    while flag2 != True:
        stop = seq[orf_stop]+seq[orf_stop+1]+seq[orf_stop+2]
        if stop == "TAG" or stop == "TAA" or stop == "TGA":
            flag = True
            break
        orf_stop = orf_stop + 3
    
    gene = seq[orf:orf_stop+3]    
    
    return gene

#translate a gene to protein sequence
def translate(seq):
    #Amino Acid Codon Dictinary
    codon_dict = {"TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L","ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V","GTG":"V","TCT":"S","TCC":"S","TCA":"S","TCG":"S","AGT":"S","AGC":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P","ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A","TAT":"Y","TAC":"Y","TAA":"stop","TAG":"stop","TGA":"stop","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","AAT":"N","AAC":"N","AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E","TGT":"C","TGC":"C","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R","GGT":"G","GGC":"G","GGA":"G","GGG":"G","TGG":"W"}
    
    
    protein_seq = ""
    k = 0
        
    while k <= len(seq)-3:
        codon = ""
        codon = seq[k]+seq[k+1]+seq[k+2]
        protein_seq = protein_seq + codon_dict[codon]
        k = k + 3
    return protein_seq



#write protein sequence to fasta file
def get_fasta(destination,ID,seq):
    f = open(destination+ID+".fasta","w")
    f.write(">"+ID+"\n")
    start = 0
    end = 60
    if len(seq) < 60:
        f.write(seq[:])
    else:
        
        while len(seq)-end >= 60:
            f.write(seq[start:end]+"\n")
            start = end
            end = end + 60
        f.write(seq[end:])
    f.close()
    print "fasta file created successfully"
    return 