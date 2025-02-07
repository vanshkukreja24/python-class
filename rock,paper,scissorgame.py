
                # question = 3   make a rock , paper and scissors game 
import random 

#elements = ["Rock","Paper","scissors"]
emojis = {"r":"🪨", "p":"📰","s":"✂️"}
choise = ("r","p","s")
def rock_paper_and_scissors_game (): 
        while True :
                user_choise =  input("rock , paper and scissors ? (r,p,s)").lower()
                if user_choise not in choise:
                        print("invalide choise ! ")
                        continue

                computer_choise = random.choice(choise)

                print(f"you chose {emojis[user_choise]}")
                print(f"computer chose {emojis[computer_choise]}")

                if user_choise == computer_choise:
                        print("tie !")
                elif (
                        (user_choise =="r" and computer_choise =="s") or 
                        (user_choise =="p" and computer_choise =="r") or 
                        (user_choise =="s" and computer_choise =="p")):
                        print("you Win")
                else:
                        print("you Loss !") 
                        
                should_countinue = input("Continue ? (y/n)").lower()
                if should_countinue =="n":
                        break                    
        print("Thanks for play")
rock_paper_and_scissors_game()