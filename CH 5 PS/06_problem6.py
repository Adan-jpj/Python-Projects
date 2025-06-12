# Create an empty dictionary.Allow 4 friends to enter thir favorite language as value and use key as their names. Assume as that the name the names are new.

d = {}

name = input("Enter friends name: ") 
lang = input("Enter language name")

d.update({name: lang})
name = input("Enter friends name: ") 
lang = input("Enter language name")

d.update({name: lang})
name = input("Enter friends name: ") 
lang = input("Enter language name")

d.update({name: lang})
name = input("Enter friends name: ") 
lang = input("Enter language name")

d.update({name: lang})

print (d)
