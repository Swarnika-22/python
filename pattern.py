n1=5
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()

n2=6
for i in range(n2,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
n3=5
for i in range(1,n3+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()
n4=5
for i in range(1,n4+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
lst = [
    [1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1]
]
for i in lst:
    for j in i:
        if j == 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

lst = [
    [1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,0,0,1]
]
for i in lst:
    for j in i:
        if j == 1:
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()