print(" ")

print("-----------------------------------------")
print("********* Welcome To Student Management System **********")

sms=open("data.txt","a+")

def viewname():
    sms=open("database.txt","r")
    for i in sms:
        print(i)
    sms.close()



def addname():
    sms=open("database.txt","a+")
    a=input("Enter the new student name : ")
    a=a+'\n'
    sms.write(a)
    print("student name added")
    sms.close()


def removename():
    sms=open("database.txt","a+")
    a = input("Search student name to Remove : ")
    a=a+'\n'
    sms.seek(0)
    rn = sms.readlines()
    if a in rn:
        rn.remove(a)
        print("Removed student name from list",a)
        s=''
        s = ''.join([str(i) for i in rn])
        f1 = open('database.txt','w')
        f1.write(s)
        f1.close()
    else:
        print("Student not found")
    sms.close()


def searchname():
    sms=open("database.txt","r")
    a=input("search student name : ")
    readfile = sms.read()
    if a in readfile:
        print("Studnet found",a)
    else:
        print("student found",a)
    sms.close()




while(True):
    print("---------------------------------------------------------------------------")
    print("Please chose any one option")
    print("1. To view list:")
    print("2. To add new student list")
    print("3. To remove the data")
    print("4. To search data")
    print("5. Exit")


    ch=int(input("Enter your choice : "))

    if ch==1:
        viewname()

    elif ch==2:
        addname()

    elif ch==3:
        removename()

    elif ch==4:
        searchname()

    elif ch==5:
        exit()

    else:
        print("Wrong Entry")


    c=input("Do you want to countinue y/n :")

    if(c=="y"):
        continue
    elif(c=="n"):
        break
        
    
        





        
