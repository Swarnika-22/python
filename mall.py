b_amt = int(input("Enter the bill amt:\n"))
q = input("Do you have a membership?\n")
if q == "Y":
    dis = b_amt * 0.1
    n_amt = b_amt - dis
    print(f"Thank You! Your total bill amount is Rs{b_amt}, discount is Rs{dis} and net amount payable is Rs{n_amt}")
elif q == "N":
    dis = b_amt * 0.03
    n_amt = b_amt - dis
    print(f"Thank You! Your total bill amount is Rs{b_amt}, discount is Rs{dis} and net amount payable is Rs{n_amt}")

else:
    print("enter appropriate input")
