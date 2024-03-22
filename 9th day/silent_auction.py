import os
def clearScreen():
    os.system('clear')

def addBid (bidsDictionary):
    name = ""
    bid = 0
    while len(name) == 0:
        name = input("What's your name?\n")
    while bid <= 0:
        bid = input("Input your bid now\n$ ")
        try:
            bid = int(bid)
        except ValueError:
            bid = 0
    bidsDictionary[name] = bid
    return bidsDictionary

bids = {}
auctionIsOpen = True
while auctionIsOpen or len(bids) == 0:
    addBid(bids)
    clearScreen()
    if input("Do you want to enter another bid? Enter \"no\" for closing the auction.\n").lower() == "no":
        auctionIsOpen = False
    else:
        clearScreen()


maxBid = 0
maxBidder = []
for bidder in bids:
    if bids[bidder] > maxBid:
        maxBid = bids[bidder]
        maxBidder = [bidder]
    elif bids[bidder] == maxBid:
        maxBidder.append(bidder)

if len(maxBidder) > 1:
    print(f"There's a tie! {" and ".join(maxBidder)} all bid exactly ${maxBid}.")
elif len(maxBidder) == 1:
    print(f"The winner is {maxBidder[0]} with their bid of ${maxBid}.")
else:
    print(f"I don't know what happened here. Here's the highest bid: ${maxBid}. Here's the people that bid this: {maxBidder}")