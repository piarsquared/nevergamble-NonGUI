##### BASICS

import msvcrt
import time
import os
import json
import random
import sys
import threading

##### GLOBALS

SAVE_FILE = "save.gamble"
currentBal = 5000
introSkip = False
currentPage = ""

stockName = "STONK"
stockPrice = 100.0
stockOwned = 0
stockRunning = True

##### STOCK SYSTEM

def update_stock_price():
    global stockPrice
    while stockRunning:
        change = random.uniform(-0.05, 0.05)
        stockPrice = round(max(1.0, stockPrice * (1 + change)), 2)
        time.sleep(5)

def show_stock_page():
    clear_term()
    page = f"\U0001F4C8 {stockName} Stock\n\nCurrent Price: ${stockPrice}\nOwned Shares: {stockOwned}"
    pageManager(page)

def watch_stock():
    clear_term()
    print("Watching stock price... Press any key to stop.\n")
    while not msvcrt.kbhit():
        print(f"\r{stockName} Price: ${stockPrice}", end="")
        time.sleep(1)
    msvcrt.getch()
    clear_term()
    pageManager(currentPage)

def buy_stock():
    global currentBal, stockOwned
    print(f"Current price: ${stockPrice}")
    amount = input("How many shares to buy? > ").strip()
    if amount.isdigit():
        amount = int(amount)
        cost = stockPrice * amount
        if currentBal >= cost:
            currentBal -= cost
            stockOwned += amount
            print(f"Bought {amount} shares for ${cost:.2f}")
        else:
            print("Not enough money.")
    else:
        print("Invalid input.")
    press2_cont()
    clear_term()
    pageManager(currentPage)

def sell_stock():
    global currentBal, stockOwned
    print(f"Owned shares: {stockOwned}")
    amount = input("How many shares to sell? > ").strip()
    if amount.isdigit():
        amount = int(amount)
        if stockOwned >= amount:
            stockOwned -= amount
            revenue = stockPrice * amount
            currentBal += revenue
            print(f"Sold {amount} shares for ${revenue:.2f}")
        else:
            print("You don't own that many.")
    else:
        print("Invalid input.")
    press2_cont()
    clear_term()
    pageManager(currentPage)

##### CORE FUNCS

def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')

def press2_cont():
    time.sleep(1)
    print('Press any key to continue...')
    msvcrt.getch()

def pageManager(page):
    global currentPage
    currentPage = page
    print(page)

def save_game():
    save_data = {
        "balance": currentBal,
        "owned": stockOwned,
        "settings": {
            "intro_skip": introSkip
        }
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(save_data, f)
    print("Game saved!")

def load_game():
    global currentBal, stockOwned, introSkip
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            try:
                save_data = json.load(f)
                currentBal = save_data.get("balance", 5000)
                stockOwned = save_data.get("owned", 0)
                introSkip = save_data.get("settings", {}).get("intro_skip", False)
            except json.JSONDecodeError:
                print("Corrupted save file. Starting fresh.")
    else:
        print("No save file found.")
        create = input("Create new save file? (y/n) > ").strip().lower()
        if create == "y":
            save_game()
        else:
            print("Exiting...")
            time.sleep(1)
            exit()

def settingsMenu():
    global introSkip
    clear_term()
    print("\u2699\ufe0f Settings\n")
    print(f"1. Intro skip: {'ON' if introSkip else 'OFF'}")
    print("2. Back")
    choice = input("Select an option: ").strip()
    if choice == "1":
        introSkip = not introSkip
        print(f"Intro skip is now {'enabled' if introSkip else 'disabled'}.")
        save_game()
        press2_cont()
        settingsMenu()
    elif choice == "2":
        clear_term()
        pageManager(currentPage)
    else:
        print("Invalid option.")
        press2_cont()
        settingsMenu()

def getUserInput():
    global stockRunning
    while True:
        usrinput = input("> ").strip().lower()

        if usrinput == "help":
            print("Commands:\nhelp, clear, save, quit, bank, settings, load save.gamble, delete save, stock, watch stock, buy, sell")
            press2_cont()
            clear_term()
            pageManager(currentPage)

        elif usrinput == "clear":
            clear_term()
            pageManager(currentPage)

        elif usrinput == "save":
            save_game()

        elif usrinput == "quit":
            print("Quit? (y/n)")
            if input("> ").strip().lower() == "y":
                stockRunning = False
                print("Goodbye.")
                time.sleep(1)
                clear_term()
                break

        elif usrinput == "delete save":
            print("Delete your save file? (y/n)")
            if input("> ").strip().lower() == "y":
                if os.path.exists(SAVE_FILE):
                    os.remove(SAVE_FILE)
                    print("Deleted save file.")
                else:
                    print("No save file found.")
                press2_cont()
                os.execl(sys.executable, sys.executable, *sys.argv)

        elif usrinput == "load save.gamble":
            load_game()
            clear_term()
            update_main_page()
            pageManager(currentPage)

        elif usrinput == "settings":
            settingsMenu()

        elif usrinput == "bank":
            clear_term()
            pageManager(update_main_page())

        elif usrinput == "stock":
            show_stock_page()

        elif usrinput == "watch stock":
            watch_stock()

        elif usrinput == "buy":
            buy_stock()

        elif usrinput == "sell":
            sell_stock()

        else:
            print("Unknown command.")

def update_main_page():
    return f"\U0001F4B5 Current balance is ${currentBal}"

##### MAIN GAME STARTUP #####

clear_term()
load_game()

if not introSkip:
    print("Welcome to Never Gamble!")
    press2_cont()
    clear_term()
    print('Type "help" to learn more.')
    press2_cont()

clear_term()
pageManager(update_main_page())

# Start stock thread
stockThread = threading.Thread(target=update_stock_price, daemon=True)
stockThread.start()

getUserInput()