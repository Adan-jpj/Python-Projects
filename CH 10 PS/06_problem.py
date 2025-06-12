# Can you change the self-parameter inside a class to something else(say"Adan",) Try changing to "slf" or "Adan" and see the effects.


from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(Adan,  fro, to):
        print(f"Ticket is booked in train no: {Adan.trainNo} from {fro} to {to}")
        

    def getStatus(Self):
        print(f"Train no: {Self.trainNo} is running on time")

    def getFare(self,  fro, to):
         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12399)
t.book("Jehanabad","Patna")
t.getStatus()
t.getFare("Jehanabad","Patna")
 

