# Write a program to read the text from a given file 'poems.txt' and figure out wether it contain the word 'twinkel'.

f = open("poem.txt")
content = f.read()
if("twinkel" in content):
    print("The word twinkel is present in the content")

else:
     print("The word twinkel is not present in the content")



f.close()