a = int(input("Enter your age: "))

# if elif else ladder

if(a>=18):
    print("you are above the age of consent")
    print("Good for you")
    

elif(a<0):
    print ("You are entering an invalid negative age")

elif(a==0):
    print ("You are entering 0")

else: 
    print("you are below the age of consent")
    print("Bad for you")

print("End of program")
