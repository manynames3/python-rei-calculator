# Real Estate Investment return calculator by Aiden Rhaa
  # Assumptions: Cash purchase & 8% selling cost.
    # In v2, converted user input sections to while True, try, except. In order to prevent users from entering non-integer input.

print("Welcome to REI calculator\n")


# user input purchase price. user must enter an integer, other wise they will be re-asked.
while True:
  try:
    purchase_price = int(input("Purchase Price: $"))
    break
  except:
    print("That's not a valid option!")


# user input holding period. user must enter an integer, other wise they will be re-asked.
while True:
  try:
    holding_period = int(input("Holding period in years: "))
    break
  except:
    print("That's not a valid option!")


# user input appreication rate. user must enter an integer, other wise they will be re-asked.
while True:
  try:
    appreciation_rate = int(input("Expected Annual Appreciation %: "))
    break
  except:
    print("That's not a valid option!")


# value of the property at the end of holding period 
future_value = round(purchase_price * (1 + appreciation_rate/100) ** holding_period)


# selling cost at the end of holding period, 8%
selling_cost = round(future_value * 0.08)


# outcome of your real estate investment
print(f"\nIn {holding_period} years, your investment property will be worth ${future_value}. After 8% selling cost of ${selling_cost}, this investment will have netted you ${future_value - purchase_price} in profit!")


# year by year look at numbers
print("\nHere is annualized look at the numbers: ")

counter = 1
while counter <= holding_period:
  gained_value = purchase_price *  (appreciation_rate/100)
  purchase_price += int(gained_value)
  print(f"Year {counter}: ${purchase_price}")
  counter += 1