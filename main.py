#main.py
import Assignment_module

# Path used
# C:\Users\rubi\Documents\Masters 2014\Python\Practice\Assignment 2\fastafile.fasta

path = raw_input("Enter input path: ")
destination = raw_input("Enter destination path: ")

#define sequence from fasta file
seq = Assignment_module.read_fasta_file(path)[1]

#find the gene including start and stop codons by ORF
gene = Assignment_module.get_gene_by_ORF(seq,Assignment_module.get_ORF(seq))


if gene != -1:
    #translate protein sequence
    protein_seq = Assignment_module.translate(gene)
    #write protein sequence to fasta file
    Assignment_module.get_fasta(destination,raw_input("File name (with no extention): "),protein_seq)     
    
    if raw_input("\nWould you like to repeat analysis with the reverse complement? (y/n): ") == "y":
        
        #get reverse complement of DNA sequence
        rev_comp = Assignment_module.reverse_complement(seq)
        
        #Repeat analysis on reverse complement
        gene = Assignment_module.get_gene_by_ORF(rev_comp,Assignment_module.get_ORF(rev_comp))
    
        protein_seq = Assignment_module.translate(gene)
        Assignment_module.get_fasta(destination,raw_input("\nFile name (with no extention): "),protein_seq)
    else:
        print "Analysis complete!"    
else:
    print "\ncannot translate as there is no open reading frame"




