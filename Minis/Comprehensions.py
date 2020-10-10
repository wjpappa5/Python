names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = []
for name in names:
    lowercased.append(name.lower())

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = []
for name in names:
    titlecased.append(name.title())
    
titlecased = [name.title() for name in names]

invitations = [
    f"\nDear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
