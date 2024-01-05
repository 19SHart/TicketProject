print("Welcome to the fun fair!")

ChildPrice = 12
AdultPrice = 20
SeniorPrice = 11
WristbandPrice = 20
ParkingPrice = 0

def ticketAsk(ticket, pretty):
    while True: 
        try:
            user = int(input("How many {pretty} would you like? "))
        except ValueError:

print("Current Prices:\nChild: {ChildPrice}\nAdult: {AdultPrice}\nSenior: {SeniorPrice}\nWristband: {WristbandPrice}\nParking: {ParkingPrice}")
