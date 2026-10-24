A=str(input("Enter the Text you want to check:"))
B=str(input("Enter The Alphabet You want to count:"))

Container=[]

for i in (A):
    if i == B:
        Container.append(i)
    else:
        pass

print(f"Your Alpahbet{B}comes:{len(Container)} Times.")


