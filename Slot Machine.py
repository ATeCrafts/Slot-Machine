import random

print("Welcome to the Slot Machine!")
print("Your starting balance is: $10000")
balance = 10000

if balance < 1000:
    print("Not enough balance!")
    quit()

start = input("Would you like to spin? Each spin costs $1000 (y/n): ")
while start != "y" and start != "n":
    print("Invalid input!")
    start = input("Would you like to spin? (y/n): ")

if start == "n":
    quit()

while start == "y":
    if balance < 1000:
        print("Not enough balance!")
        quit()
    balance -= 1000

    generated1 = random.randint(1, 10)
    generated2 = random.randint(1, 10)
    generated3 = random.randint(1, 10)

    print("This slot machine has 3 columns. Each column contains numbers from 1-10. Bet on the number you think will appear in each column")
    def getValidNumber(prompt):
        while True:
            value = input(prompt)
            if value.isdigit():
                value = int(value)
                if 1 <= value <= 10:
                    return value
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")
    column1 = getValidNumber("Enter the number you think will appear in column 1: ")
    column2 = getValidNumber("Enter the number you think will appear in column 2: ")
    column3 = getValidNumber("Enter the number you think will appear in column 3: ")

    print("Your input:", column1, column2, column3)
    print("What was generated:", generated1, generated2, generated3)

    if column1 == generated1:
        balance += 1000
    if column2 == generated2:
        balance += 1000
    if column3 == generated3:
        balance += 1000
    print("Current balance:", balance)

    start = input("Would you like to spin again? (y/n): ")