A= input("Enter your Text: ")
result = ""
capitalize_next = True  # Start by capitalizing the very first letter

for i in A:
  if i == " ":
    result += " "
    capitalize_next = True  # When we hit a space, the next letter is the start of a new word!
  elif capitalize_next:
    result += i.upper()
    capitalize_next = False  # Turn off the flag until we hit another space
  else:
    result += i.lower()  # Keep regular letters lowercase

print("Title Case:", result)