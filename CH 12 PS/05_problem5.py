n = int(input("Enter a number: "))

tabel = [n*i for i in range(1, 11)]
with open("tabels.txt", "a") as f:
    f.write(f"Tabel of {n}: {str(tabel)} \n")