
bill=int(input("What is the total of the bill?\n"))
split=int(input("How many people to split?\n"))
tip=int(input("Tip of 10, 12, or 15?\n"))

tip1=tip/100 + 1


total=(round(bill/split*tip1,2))
r=round(total,2)
r="{:.2f}".format(total)

print(f"Each person should pay: ${r}")
