seq=raw_input("\nPlease enter a DNA sequence: ")

count = len(seq) 
seq_list = ['']*count

rev_seq = ""

#reversing by iterating with a while loop
while count >= 1:
    seq_list[count-1] = seq[count-1]
    if seq_list[count-1]=='T'or seq_list[count-1]=='t':
        seq_list[count-1] = 'U'
    rev_seq = rev_seq + seq[count-1]
    count = count -1
    
print "\nOrigional sequence reversed: " + rev_seq
print "Converted sequence reversed in list format: " + str(seq_list[::-1])

rev_seq_list = seq_list[::-1]

print "Converted sequence reversed in sequence string format: ",
for k in rev_seq_list:
    print str(k),


