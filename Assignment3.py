# 1.Declare four variables in Python: one integer (number of followers), one float (average rating), 
 # one string (your favorite app's name), and one boolean (is_premium_user). 
# Print each variable and its type using the type() function.


followers=2500
avg_rating=4.5
favourite_app="instagram"
is_premium_user=True

print(followers)
print(type(followers))

print(avg_rating)
print(type(avg_rating))

print(favourite_app)
print(type(favourite_app))

print(is_premium_user)
print(type(is_premium_user))

#--------------------------------------------------------------------------------------------------------------
#2.Write a Python program that takes a user's input for the price of a Zomato order as a string,
# converts it to a float using type casting, adds 18% GST, and prints the final bill amount.


price = input("Enter the  order price: ")

price_float=float(price)

print("The float amount is : ",price_float)

gst = 0.18

print("gst on order is :",price_float*gst)

print("the final bill amount is :",price_float+(price_float*gst))

#--------------------------------------------------------------------------------------------------------------
#3.Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'], 
 # convert all to floats and calculate the total cart value.

price = ['199.99', '299.50', '150']

prices = list(map(float,price))
total = sum(prices)
print(prices)
print("total cart value is :",total)


#--------------------------------------------------------------------------------------------------------------
#4.Build a function is_discount_applicable(order_amount) that takes a float and returns True if the amount 
 # is greater than 500, otherwise False. Print the result for order amounts 450 and 750.

def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False

print(is_discount_applicable(450))
print(is_discount_applicable(750))

#--------------------------------------------------------------------------------------------------------------
#5.You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. Use type casting to 
# convert these to floats, then find and print the highest rating.<br><br><em><strong>Hint:</strong> 
# Use the float() function inside a loop or list comprehension.</em>

ratings = ['4.5','3.0','5','4.2']

float_ratings = []

for i in ratings:
    float_ratings.append(float(i))

print(ratings)
print(float_ratings)

print("Highest Rating:", max(float_ratings))




    

     


















