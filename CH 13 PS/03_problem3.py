# A list contains the multiplication tabel of 7. write a program to convert it to vertical string of same numbers.

tabel = [str(7*i) for i in range(1,11)]

s = "\n".join(tabel)
print(s)