n1 = 47098
n = n1
rev,sum = 0,0
while n != 0:
    r = n % 10
    rev = rev * 10 + r
    sum += r
    n //= 10
print(f"reverse of no is {rev}")
print(f"sum of digits {sum}")
n2 = n1
sum = 0
while n2 > 9:
    n2 = n2 // 10 + n2 % 10
print(f"sum until single digit {n2}")
if n1 == rev:
    print(f"{n1} is palindrome")
else:
    print(f"{n1} is not a palindrome")
count = 0
n3 = n1
while n3 != 0:
    count += 1
    n3 //= 10
print(f"count of digit is {count}")