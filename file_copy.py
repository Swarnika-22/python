with open("xyz.txt")as f:
    with open("abc.txt","w")as f1:
        for line in f:
            f1.write(line)
f = open("abc.txt","r")           
print(f.read())