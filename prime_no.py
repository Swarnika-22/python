#prgm to print prime no of given interval
lb=int(input("Enter the lb "))
ub=int(input("Enter the ub "))
for n in range(lb,ub+1):
        if n>1:
            for i in range(2,n//2+1):
                if n % i == 0:
                    break
            else:
                print(n)