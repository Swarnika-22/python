#prgm for billing amt
b_amt=int(input("Enter the billing amount"))
if b_amt > 6000:
    discount=(b_amt*0.1)
    n_amt=b_amt-discount
else:
    n_amt=b_amt
print(f"Your net billing amount is {n_amt}")