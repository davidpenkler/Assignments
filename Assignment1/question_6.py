DNA_list = ['TGAC','aattggcc','ccCCcc']
seq_length = 0

for k in DNA_list:
    seq_length = seq_length + len(k)
avg = seq_length/len(DNA_list)

print "\nThe average is: " + str(avg)