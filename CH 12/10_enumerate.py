l = [3,53, 543, 535]

# index = 0 
# for item in l:
    
#     print(f"The item number at index {index} is {item}")
#     index += 1

#This can be simplified using eumerate function

for index, item in enumerate(l):
     print(f"The item number at index {index} is {item}")