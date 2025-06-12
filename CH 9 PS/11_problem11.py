# Write a python program to rename a file to "renamed"_by_python.txt

with open("old.txt") as f:
    content = f.read()

with open("rename_by_python.txt", "w") as f:
    f.write(content)