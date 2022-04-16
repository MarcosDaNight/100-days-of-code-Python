from traceback import print_tb


print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = float(input("What percemtage tip would you like to give? 10, 12 or 15? "))/100
people = int(input("How many people split the bill? "))

result = (bill * tip) / people

answer = f"Each person should pay: ${result}"

print(answer)