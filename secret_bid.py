from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
import random
# print(logo)
high_bid=int(0)
bid_dict = {
  "cheat1" : int(99),
  "cheat2" : int(105),
  "cheat3" : random.randint(1, 199),
  "cheat4" : random.randint(1, 199),
  "cheat5" : random.randint(1, 199),
}
more_bids="Y"
while more_bids.upper() == "Y":
  name=input("To enter a bid, input your name\n")
  bid=int(input(f"Hi {name} what is your bid? "))
  print(f"{name} bids {bid}.\n")
  # bid_dict = {     name: bid,   }
  bid_dict[name] = bid
  more_bids=input("Are there any more bids? y or n? ")
  clear()

print("No more bidders, we are calculating the winner \n") 
print(bid_dict)
print(type({bid_dict["cheat1"]}))
print({bid_dict["cheat2"]})

print("...\n")
for key in bid_dict:
  # print(KEY) 
  print(f"{key} bids {bid_dict[key]}")
  bid_to_test = bid_dict[key]
  if high_bid < bid_to_test:
    high_bid = bid_to_test
    winner = key

print(f"The highest bid was {high_bid}, congratulations {winner}! \n")


