print("LOAN CALCULATOR")
print()
print("$1000 over 10 years at APR 5%")
amtborrowed = 1000
apr = 0.05
for year in range (10):
  amtborrowed += amtborrowed*apr
  print("Year",  year+1, "is", round(amtborrowed, 2) )
totalinterest = amtborrowed - 1000
totalinterest = round(totalinterest, 2)
print()
print("You paid $", totalinterest, "in inetrerst")
print()
print("you paid $", round(amtborrowed, 2), "in total")
print()
print("Thank you for using our loan calculator")