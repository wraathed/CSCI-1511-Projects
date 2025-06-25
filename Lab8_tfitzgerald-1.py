from coin import Coin

'''
Lab 8
Tyson Fitzgerald
two players flip coins to see who can gather the most by the end
6/24/2025
'''

def main():
    player1 = Coin()
    player2 = Coin()

    print("welcome to coin flip! each player has 20 coins, whoever gets all the coins wins")
    print("-----------------------------------------")
    play_again = input("do you want to play? (y/n): ")

    while play_again == 'y':
        
        player1.toss()
        player2.toss()

        p1_side = player1.get_sideup()
        p2_side = player2.get_sideup()

        print(f"player 1: {p1_side}")
        print(f"player 2: {p2_side}")

        if p1_side == p2_side:
            print("coins were the same, player 1 wins this round")
            player1.set_amount(1)
            player2.set_amount(-1)
        else:
            print("coins were different, player 2 wins this round")
            player2.set_amount(1)
            player1.set_amount(-1)

        print(f"player 1 coins: {player1.get_amount()}")
        print(f"player 2 coins: {player2.get_amount()}")

        print("-------")
        play_again = input("do you want to play again? (y/n): ")

    print("Game Over")
    final_p1_coins = player1.get_amount()
    final_p2_coins = player2.get_amount()

    print(f"Final coins: Player 1: {final_p1_coins} | Player 2: {final_p2_coins}")

    if final_p1_coins > final_p2_coins:
        print("Player 1 wins with more coins!")
    else:
        print("Player 2 wins with more coins!")


if __name__ == "__main__":
    main()