import os
import random
import time


# Main menu to select game
def main_menu(wallet):

    """_This is for the main menu where you choose your wanted action._
    """

    clear_console()
    print("----[Welcome to the CasinoCabin]----")
    print("----[Select your game]----\n")

    print("[1] Roulette  [4] Blackjack      [7] Deposit money")
    print("[2] Poker     [5] Horses         [8] Widthdraw money")
    print("[3] Slots     [6] Blackjack      [9] Exit" + "\n")
    # errorHandling(wallet)

    print("Wallet: $", wallet)
    game = int(input("\nPlease Select your game: "))

    if game == 1:
        print("[Sorry this game is still under construction]")
        time.sleep(2)
        main_menu(wallet)
    elif game ==2:
        print("[Sorry this game is still under construction]")
        time.sleep(2)
        main_menu(wallet)
    elif game == 3:
        slots(wallet)
    elif game == 4:
        print("[Sorry this game is still under construction]")
        time.sleep(2)
        main_menu(wallet)
    elif game == 5:
        print("[Sorry this game is still under construction]")
        time.sleep(2)
        main_menu(wallet)
    elif game == 6:
        print("[Sorry this game is still under construction]")
        time.sleep(2)
        main_menu(wallet)
    elif game == 7:
        deposit_funds(wallet)
    elif game == 8:
        withdraw_funds(wallet)   
    elif game == 9:
        print("---[Thank you for playing at the CasinoCabin]---")
        exit


# Function to clear console when wanted

def clear_console():

    """_This function is made to clear the console to make the casino cleaner and more simple to use._
    """

    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)

# Shows the current wallet

def show_wallet(wallet):

    """_This shows your current wallet, your current assets. _
    """

    print("\nWallet: $", wallet , "\n")

# Checks if the bett is over the wallet amount

def bet_check(wallet, bet):

    """_Checks if you have enough assets to place your wanted bett. _
    """

    if bet == 0:
        main_menu(wallet)
    
    if wallet == 0:
        print("Sorry! Not enough funds!")
        time.sleep(3)
        main_menu(wallet)

    if bet > wallet:
        print("Not enough funds for that bet!")
        time.sleep(1.4)
        main_menu(wallet)

# Deposit new funds into wallet

def deposit_funds(wallet):

    """_This makes it possible for you to deposit new founds into your wallet. _
    """

    clear_console()

    print("----[Deposit Funds]----\n")
    deposit = int(input("How much would you like to deposit?: $"))

    wallet += deposit

    print("Succesfully updated wallet with: $", deposit)
    time.sleep(2)

    main_menu(wallet)

# Withdraw funds from wallet

def withdraw_funds(wallet):

    """_This makes it possible for you to withdraw founds from your wallet. _
    """

    clear_console()
    print("----[Withdraw Funds]----\n")
    withdrawal = int(input("How much would you like to withdraw?: $"))

    wallet -= withdrawal

    print("Succesfully withdrawed: $", withdrawal)
    time.sleep(2)
    main_menu(wallet)

# Slot machine selection
def slots(wallet):

    """_This is the main menu for the slots. _
    """
    clear_console()

    print("====[Welcome to Slots!]====\n")
    
    print("---[Please select a slots machine]---")

    print("[1] Royalle\n")
    print("[2] King\n")

    slot_choice = input("Please select your choice: ")

    if slot_choice == "1":
        royalle(wallet)
    elif slot_choice == "2":
        king(wallet)
    else:
        main_menu(wallet)

# Royalle slot machine
def royalle(wallet):

    
    """_This is the royalle slots machine. _
    """

    clear_console()

    lane1 = ['Royalle','Grapes','Banana','Lemon','Pear','Strawberry']
    lane2 = ['Royalle','Grapes','Banana','Lemon','Pear','Strawberry']
    lane3 = ['Royalle','Grapes','Banana','Lemon','Pear','Strawberry']

    random_lane1 = random.choice(lane1)
    random_lane2 = random.choice(lane2)
    random_lane3 = random.choice(lane3)

    print("----[Now playing Royalle]----\n")

    print("If you bet 0, you'll return to the main menu\n")

    show_wallet(wallet)
    bet = int(input("\nPlease place your bet: $"))

    bet_check(wallet, bet)
    winning_jackpot = bet * 12300
    winning1 = bet * 12
    
    winner = "Congratulations! You won: $", winning1

    jackpot = "[JACKPOT] CONGRATULATIONS! YOU WON THE JACKPOT! You could've won: $",winning_jackpot

    for i in lane1:

        random_lane1 = random.choice(lane1)
        random_lane2 = random.choice(lane2)
        random_lane3 = random.choice(lane3)

        print("| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
        time.sleep(0.2)

        if random_lane1.startswith("Royalle") & random_lane2.startswith("Royalle") & random_lane3.startswith("Royalle"):
            print(jackpot)
            wallet += winning_jackpot
            time.sleep(5)
            royalle(wallet)
        elif random_lane1.startswith("Royalle") & random_lane2.startswith("Royalle"):
            print(winner)
            wallet += winning1
            time.sleep(5)
            royalle(wallet)
        elif random_lane1.startswith("Royalle") & random_lane3.startswith("Royalle"):
            print(winner)
            wallet += winning1
            time.sleep(5)
            royalle(wallet)
        elif random_lane2.startswith("Royalle") & random_lane3.startswith("Royalle"):
            print(winner)
            wallet += winning1
            time.sleep(5)
            royalle(wallet)

    print("You lost, better luck next time!")
    wallet -= bet
    time.sleep(2)
    royalle(wallet)

    return wallet

# King slot machine game
def king(wallet):

    """_This is the king slots machine. _
    """

    clear_console()

    lane1 = ['King','Grapes','Banana','Lemon','Pear','Strawberry']
    lane2 = ['King','Grapes','Banana','Lemon','Pear','Strawberry']
    lane3 = ['King','Grapes','Banana','Lemon','Pear','Strawberry']

    random_lane1 = random.choice(lane1)
    random_lane2 = random.choice(lane2)
    random_lane3 = random.choice(lane3)

    print("----[Now playing King]----\n")

    print("If you bet 0, you'll return to the main menu\n")

    show_wallet(wallet)
    bet = int(input("\nPlease place your bet: $"))

    bet_check(wallet, bet)
    winning_jackpot = bet * 12300
    winning1 = bet * 12
    
    winner = "Congratulations! You won: $", winning1

    jackpot = "[JACKPOT] CONGRATULATIONS! YOU WON THE JACKPOT! You could've won: $",winning_jackpot

    for i in lane1:

        random_lane1 = random.choice(lane1)
        random_lane2 = random.choice(lane2)
        random_lane3 = random.choice(lane3)

        print("| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
        time.sleep(0.2)

        if random_lane1.startswith("King") & random_lane2.startswith("King") & random_lane3.startswith("King"):
            print(jackpot)
            wallet += winning_jackpot
            time.sleep(5)
            king(wallet)
        elif random_lane1.startswith("King") & random_lane2.startswith("King"):
            print(winner)
            wallet += winning1
            time.sleep(5)
            king(wallet)
        elif random_lane1.startswith("King") & random_lane3.startswith("King"):
            print(winner)
            wallet += winning1
            time.sleep(5)
            king(wallet)
        elif random_lane2.startswith("King") & random_lane3.startswith("King"):
            print(winner)
            wallet += winning1
            time.sleep(5)
            king(wallet)

    print("You lost, better luck next time!")
    wallet -= bet
    time.sleep(2)
    king(wallet)

    return wallet

# First menu to start main menu
def first_menu():

    """_This is the first menu that you come to when you start the casino. _
    """

    clear_console()
    print("----[Welcome to the CasinoCabin]----\n")
    wallet = int(input("Please deposit funds: $"))
    main_menu(wallet)

first_menu()

if __name__ == main():
    main()
