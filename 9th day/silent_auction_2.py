import os
def clearScreen():
    os.system('clear')

collected_bids = {}
auction_is_open = True

while auction_is_open == True:
    name = ""
    while len(name) <= 0:
        name = input("Please enter your name.\n")

    bid = 0
    while bid == 0:
        bid = input("Please enter your bid.\n$")
        try:
            bid = int(bid)
        except ValueError:
            bid = 0
    
    collected_bids[name] = bid
    clearScreen()

    if input("Do you want to continue? Type \"no\" to exit.\n").lower() == "no":
        auction_is_open = False

    clearScreen()

maxBid = 0
maxBidder = []
for bidderName in collected_bids:
    bid = collected_bids[bidderName]
    if bid > maxBid:
        maxBid = bid
        maxBidder = [bidderName]
    elif bid == maxBid:
        maxBidder.append(bidderName)

if len(maxBidder) == 1:
    print(f"The winner is {maxBidder[0]} with their bid of ${maxBid}.")
else:
    print(f"There was a tie between {" and ".join(maxBidder)} who all bid {maxBid}, we will have a do-over.")