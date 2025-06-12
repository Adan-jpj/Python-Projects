# Write a program to filter a list of numbers which are divisible by 5

def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,34234,53,623423,64,745,45,55]

f = list(filter(divisible5, a))
print(f)