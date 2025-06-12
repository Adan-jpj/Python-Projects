# Write a program to open three files 1.txt, 2.txtand 3.txt any these files are not present, a message without

try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank You!")