# Write a class Train which has method to book a ticket, get status(no. of seats) and fare information of train 

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,  fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        

    def getStatus(Self):
        print(f"Train no: {Self.trainNo} is running on time")

    def getFare(self,  fro, to):
         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12399)
t.book("Jehanabad","Patna")
t.getStatus()
t.getFare("Jehanabad","Patna")
 

