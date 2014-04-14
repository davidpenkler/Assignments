n = input("\nEnter a number: ")

flag = True
count = 0

for k in range(2,n-1):
    if n % k == 0:
        flag = False
        break

if flag:
    print str(n) + " is a prime number"
else:
    print str(n) + " is not a prime number"