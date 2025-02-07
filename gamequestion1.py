

#                     question 1 write a program to print a table of given number 

# n = int(input("Enter the value :"))

# for i in range(1,11):
#     print(f"{i}*{n} = {n*i}")

#                  # question 2 write a program to find the sum of natural number from 1 to n

# n = int(input("Enter the value :"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum+i
    
# print(f"The sum of natural numbers from 1 to {n} is: {sum}")



#                    Question 3 write a program to find the factor of a number 

# n = int(input("Enter the value :"))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
    

#                     question 4 write a program to read a number from user and find sum of element till the nagative number is entered by user

# n = int(input("Enter the value :"))
# for i in range(1,n+1):
#     n = int(input("Enter the number :"))
#     if n<0:
#         print("we can not continue a code ")
    

#                 SIR  HOW CAN WE ADD NUMBER 

#         #OR

# sum = 0 
# while True :
#     n = int(input("Enter the value :"))
#     if n<0:
#         break
#     sum = sum+n
# print(f"The sum of entered numbers is: {sum}")


#                     Question 5 write a program to find a factorial or product of  number given by user  

# factorial of 5 = 1*2*3*4*5 = 120

# n = int(input("Enter a positive number : "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial = factorial*i

# print(f"The factorial of {n} is: {factorial}")
            

            
# 1 = randint () function is used for 1 to (x)number given by user

# import random as rd 
# print(rd.randint(1,100))

# 2 = choice () function is used for random item from your list 

# my_list = ["car","bike","chees","fifa"]
# print(rd.choice(my_list))

# 3 = randrange () function is same as randint but with step 
# print(rd.randrange(0,100,2))

#                 question = 1  roll the dice game 

# import random as rd  # type: ignore

# dice1 = [1,2,3,4,5,6]
# dice2 = [1,2,3,4,5,6]
# def Dice_game ():
#         while True :
#                 x = input("roll the dice ? (yes(y)/No(n))").lower()
#                 #choice2,choice1 = None,None
#                 if x =="y" :
#                         choice1 = rd.choice(dice1) #OR rd.randint(1,6) 
#                         choice2 = rd.choice(dice2) #OR rd.randint(1,6)
#                         print(f"your number is {choice1} and {choice2}")                
#                 elif x =="n" :
#                         print("thanks for playing")
#                         break 
#                 else:
#                         print("invalid choice")
        
# Dice_game()

#                 question = 2  guess the number 1 to 100
# import random

# number_to_guess = random.randint(1,100)
# # print(number_to_guess)
# def guess_the_number_game ():
#         chance = 5
#         while chance>0:
#                 try:
#                         guess = int(input("Guess The Number Between 1 To 100 :"))
                        
#                         if guess < number_to_guess:
#                                 print("Too low !")
#                         elif guess > number_to_guess:
#                                 print("Too high !")
#                         else:
#                                 print("Congratulations ! you guess the number")
#                                 break
#                 except ValueError:
#                         print("please enter the valide number ")
        
#                 chance = chance-1                       
#         if chance == 0:
#                 print('Sorry, You lost the game😒')
#                 print(number_to_guess)

# guess_the_number_game()





#                 # question = 3   make a rock , paper and scissors game 
# import random 

# #elements = ["Rock","Paper","scissors"]
# emojis = {"r":"🪨", "p":"📰","s":"✂️"}
# choise = ("r","p","s")
# def rock_paper_and_scissors_game (): 
#         while True :
#                 user_choise =  input("rock , paper and scissors ? (r,p,s)").lower()
#                 if user_choise not in choise:
#                         print("invalide choise ! ")
#                         continue

#                 computer_choise = random.choice(choise)

#                 print(f"you chose {emojis[user_choise]}")
#                 print(f"computer chose {emojis[computer_choise]}")

#                 if user_choise == computer_choise:
#                         print("tie !")
#                 elif (
#                         (user_choise =="r" and computer_choise =="s") or 
#                         (user_choise =="p" and computer_choise =="r") or 
#                         (user_choise =="s" and computer_choise =="p")):
#                         print("you Win")
#                 else:
#                         print("you Loss !") 
                        
#                 should_countinue = input("Continue ? (y/n)").lower()
#                 if should_countinue =="n":
#                         break                    
        
# rock_paper_and_scissors_game()


#                 question = 4 guess the dice number in 2 chance
                
# import random 
# print(computer_choise)
# computer_choise = random.randrange(1,7)
# def guess_the_dice_number ():
#         chance = 2
#         while chance > 0:
#                 user_input = int (input("Guess the number on 2 chance :"))
#                 if computer_choise == user_input:
#                         print("you Win the game 🏆")
#                         break
#                 else:   #computer_choise != user_input
#                         print(f"this is not a number Please try again  you have this {chance-1} left😡")
#                         chance = chance-1
#                 if chance == 0:
#                                 print('Sorry, You lost the game😒')

# guess_the_dice_number()









