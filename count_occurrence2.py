A=str(input("Enter Your sentance:"))

vovel=("aeiouAEIOU")
consonant=("")
num=("1234567890")
space=(" ")
other=("!@#$%^&*")

vovels=[]
consonants=[]
nums=[]
spaces=[]
others=[]

for i in (A):
    if i in (vovel):
        vovels.append(i)
    elif i in (num):
        nums.append(i)
    elif i in (space):
        spaces.append(i)
    elif i in (other):
        others.append(i)
    else:
        consonants.append(i)

print("Number of vovels in sentance is:",len(vovels))
print("Number of numbers in sentance is:",len(nums))
print("Number of spacesin sentance is:",len(spaces))
print("Number of spacial characters in sentance is:",len(others))
print("Number of consonants in sentance is:",len(consonants))










