A=str(input("Enter your line: "))
Vovels=[]
consonants=[]
for i in A:
    if i in "aeiouAEIOU":
        Vovels.append(i)
    elif i in (" "):
        pass
    else:
        consonants.append(i)

print("your line is", len(A), "characters long.")
print("Vowels:",Vovels)
print("Consonants:",consonants)
print("Number of vowels:",len(Vovels))
print("Number of consonants:",len(consonants))