# current_price = 150 
# target_price = 155

# while current_price < target_price :
#     print("price is still below the target price ")
#     current_price+=1
# print("now the price is above the target price and now you can sell the stockṇ")




# price = [110,112,114,1234,111,123]
# thresold_price = 1111
# index = 0

# while True :
#     index < len(price)
#     if price[index] > thresold_price:
#         print(f"the price {price[index]} above the thresold price at {index}")
#         break
#     index+=1
# else:
#     print("there is no price breach ")
    
# print("search is complete")





# price = [110,112,114,111,123]
# total_price = 0
# average_price = 0
# for i in price:
#     total_price+=i
# average_price = total_price/len(price)
# print(f"5 days average price is {average_price}")
# print(f"5 days total price is {total_price}")    



'''
19. How would you iterate through the characters in the string "Hello"?

1 = for i in range(len("Hello")): print("Hello"[i])wrong
2 = for character in "Hello": print(character)
 [correct answer] 3 = Both a and b correct   
4 = Neither a nor b
'''

  # question 1  You are designing an algorithm to trade stocks.If the current price of
# a stock is above the 10-day moving average, print "Buy Signal"; otherwise, print "Sell Signal"
# . Assume you have a list of daily prices and that the moving average can be calculated.

# price_for_10_days = [10,12,14,16,19,16,21,24,20,7]


# import random

# # Generate a list of 10 random numbers between 1 and 100
# price_for_10_days = [random.randint(11, 99) for i in range(10)]
# print(price_for_10_days)

# total_price = sum(price_for_10_days)
# moving_average = total_price/len(price_for_10_days)


# print(moving_average)
# for i in price_for_10_days:
#     current_price = i
    
#     if current_price > moving_average:
#         print(f"buy signal at {current_price}  ")
#     else:
#         print(f"sell signal at {current_price}  ")
    


# question 2 = with For Loop : You have data on the opening and closing prices of multiple stocks 
# in a portfolio. Using a for loop, calculate and print the total daily gain or loss for each 
# stock in the portfolio.

# Example data for opening and closing prices of stocks in a portfolio

# portfolio = {
#     'Stock_A': {'open': 100, 'close': 110},
#     'Stock_B': {'open': 50, 'close': 45},
#     'Stock_C': {'open': 75, 'close': 80},
#     'Stock_D': {'open': 200, 'close': 190},
# }

# # Calculate and print the daily gain or loss for each stock
# for stock, prices in portfolio.items():
#     gain_loss = prices['close'] - prices['open']
#     print(f"{stock}: Daily gain/loss = {gain_loss}")

