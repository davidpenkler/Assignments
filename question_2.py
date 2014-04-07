seq=raw_input("\nPlease enter a DNA sequence: ")

if len(seq)<=6:
    print "Sequence length must be greater than 6 bp"
else:
    print "The first 3 and last 3 bp of sequence give: " + seq[:3] + seq[len(seq)-3:]