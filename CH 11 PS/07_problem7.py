#Override the__len__()method on vector of problem 5 to display the dimension of the vector

class vector:
    def __init__(self, l):
       self.l = l
        

 

    def __len__(self):
        return len(self.l)

#Test the implementation
v1 = vector([1, 2, 3])       
print(len(v1))