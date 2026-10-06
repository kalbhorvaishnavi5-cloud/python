print("Hello, World!")


#create 2 variables cost_price , selling_price and calculate profit or loss 
cost_price = 100
selling_price = 120

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No profit, no loss")
    
    
#write a program to check if a number is even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")  
    
    
    
#write A program check wheather the age is valid and elegible for voting or not   

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")



#write a proggram to find the word1 and word2 are anagrams or not

word1 = "listen"
word2 = "silent"

if sorted(word1) == sorted(word2):
    print("The words are anagrams")
else:
    print("The words are not anagrams")



