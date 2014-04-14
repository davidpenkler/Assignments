seq=raw_input("\nPlease enter a DNA sequence: ")

count = len(seq)
rev_seq = ""

#reversing by iterating with a while loop
while count >= 1:
    rev_seq = rev_seq + seq[count-1]
    count = count -1
print rev_seq

#reversing by splicing
print seq[::-1]
