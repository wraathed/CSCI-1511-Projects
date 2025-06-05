import random

valCard = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suitCard = ["c", "h", "s", "d"]

ranVal = random.choice(valCard)
ranSuit = random.choice(suitCard)

print(f"{ranVal}{ranSuit}")