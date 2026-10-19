Container1 = []
Container2 = []

while True:
  A = input("Enter a Primary Task: ")
  B = input("Enter a Secondary Task: ")

  Container1.append(A)
  Container2.append(B)

  print("Primary Tasks: ",Container1)
  print("Secondary Tasks: ",Container2)
  
  if A == "Done" and B == "Done":
    print("All tasks completed.")
    break