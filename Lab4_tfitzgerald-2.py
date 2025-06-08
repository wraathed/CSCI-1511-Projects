maxSticks = 4
minSticks = 1
totalSticks = 13

players = ["Player 1", "Player 2"]
playerIndex = 0
currentPlayer = players[playerIndex]

print("Each player takes turns picking up 1 to 4 sticks from a pile of 13 sticks. Whoever picks up the last stick wins.")

while totalSticks > 0:
    print(f"There are {totalSticks} stick(s) left.")
    print(currentPlayer)

    while True:
        pickup = input("How many sticks do you want to pick up? ")
        pickup_int = int(pickup)

        if pickup_int > totalSticks or pickup_int > maxSticks or pickup_int < minSticks:
            print(f"You cannot take {pickup_int} sticks.")
        else:
            break
            

    totalSticks = totalSticks - pickup_int
    
    if totalSticks <= 0:
        print(f"{currentPlayer} wins!")
        break
    else:
        if playerIndex == 0:
            playerIndex = 1
        else:
            playerIndex = 0

        currentPlayer = players[playerIndex]