fib = 0
fib_lst = [1,2]
multi5 = []
flag = True

while flag:
    fib = fib_lst[len(fib_lst)-2] + fib_lst[len(fib_lst)-1]    
    if fib < 4000:
        fib_lst.append(fib)
        if fib%5 == 0:
            multi5.append(fib)
    else:
        flag = False


print "The fibobacci sequence less that 4000 is: " + str(fib_lst)
print "The multiples of 5 are: " + str(multi5)

