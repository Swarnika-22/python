n1 = int(input("enter the binary digit\n"))
n = n1
dec = 0
i = 0
while n != 0:
    r = n % 10
    dec += r * (2 ** i)
    n //=10
    i +=1
print(f"decimal value of b'{n1} is {dec}")