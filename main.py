print("Welcome to the fun fair!")

ChildPrice = 12
AdultPrice = 20
SeniorPrice = 11
WristbandPrice = 20
total = 0

def ticketAsk(ticket, pretty):
    while True: 
        try:
            user = int(input(f"How many {pretty} would you like? "))
            break
        except ValueError:
            print("Not a number!")
    return ticket * user

print(f"Current Prices:\nChild: {ChildPrice}\nAdult: {AdultPrice}\nSenior: {SeniorPrice}\nWristband: {WristbandPrice}\nParking: {ParkingPrice}")

total = total + ticketAsk(ChildPrice, "Child Tickets")
total = total + ticketAsk(AdultPrice, "Adult Tickets")
total = total + ticketAsk(SeniorPrice, "Senior Tickets")
total = total + ticketAsk(WristbandPrice, "Wristbands")
surname = input("What is your surname? ")

while True:
    user = input("Do you require parking? (y/n)").lower()
    if user == "y":
        parking = True
        break
    elif user == "n":
        parking = False
        break
    else:
        print("Invalid input!")

print(f"Your total: {total}")

while True:
    user = input("Enter notes. (10/20) ")
    if user == "10":
        total = total - user
    elif user == "20":
        pass
    else:
        print("Not a valid note!")
    if total < 0:
        print("Done!")
        break