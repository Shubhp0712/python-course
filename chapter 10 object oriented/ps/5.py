from random import randint
class train:

    def __init__(self, trainNo, seat):
        self.trainNo = trainNo
        self.seat = seat

    def bookTicket(self, fromStation, toStation):
        print(f"Your ticket has been booked in train No: {self.trainNo} from {fromStation} to {toStation}. Your seat number is {randint(1,501)}.")

    def getstatus(self):
        print(f"The train number is {self.trainNo} running on time. The seat available are {self.seat}. ")
    
    def getfare(self, fromStation, toStation):
        print(f"The fare of the ticket from {fromStation} to {toStation} is {randint(100,500)}.")

shatabdi = train(12002, 500)
shatabdi.bookTicket("Delhi", "Mumbai")
shatabdi.getstatus()
shatabdi.getfare("Delhi", "Mumbai")

rajdhani = train(12001, 400)
rajdhani.bookTicket("Mumbai", "Delhi")
rajdhani.getstatus()
rajdhani.getfare("Mumbai", "Delhi")