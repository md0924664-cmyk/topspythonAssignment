#1.Use iter() and next() to manually loop through a list of 5 trending movies from BookMyShow and print each movie name one by one.

movies = ["Pushpa 2", "Saiyaara", "War 2", "Coolie", "Superman"]

movie_iterator = iter(movies)

print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))
print(next(movie_iterator))

#---------------------------------------------------------------------------------------------------------------------------------------------

#2.Create a playlist of 6 songs (as a list of strings) and use enumerate() to print each song with its position like Spotify's 
#  tracklist (e.g., '1. Kesariya').

playlist = [
    "Kesariya",
    "Darkhaast",
    "Thodi Der",
    "Inaam",
    "Daryaa",
    "Kabira"
]

for position, song in enumerate(playlist, start=1):
    print(f"{position}. {song}")

#--------------------------------------------------------------------------------------------------------------------------------------------- 

#3.Given two lists — one of food items and one of prices — use zip() to print each food item with its price like a Zomato menu 
#  (e.g., 'Pizza - ₹250').

food_items = ["Pizza", "Burger", "Pasta", "Sandwich", "Fries"]

prices = [250, 150, 200, 120, 100]

for item, price in zip(food_items, prices):
    print(f"{item} - ₹{price}")

#--------------------------------------------------------------------------------------------------------------------------------------------- 

#4. Write a generator function called insta_posts_generator(posts) that takes a list of Instagram post captions and yields one caption at a time.
#  Use next() to get and print the next post caption each time until all captions are printed.<br><br><em><strong>Hint:</strong> Use the yield 
#  keyword inside your function and handle StopIteration when all posts are done.</em>

def insta_posts_generator(posts):
    for post in posts:
        yield post
posts = [
    "Enjoying the sunset 🌅",
    "Workout completed 💪",
    "Delicious pizza 🍕",
    "Vacation vibes 🏖️",
    "Happy weekend 😊"
    
]
post_generator = insta_posts_generator(posts)

try:
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))
    print(next(post_generator))   
except StopIteration:
    print("No more posts available.")

#---------------------------------------------------------------------------------------------------------------------------------------------

#5. Build a generator function called cashback_generator(transactions) that takes a list of Paytm transaction amounts and yields 5% cashback
#   for each transaction. Print out the cashback values for all transactions. 

def cashback_generator(transactions):
    for amount in transactions:
        yield amount * 0.05  

transactions = [500, 1000, 750, 2000, 300]

cashback = cashback_generator(transactions)

for value in cashback:
    print("Cashback: ₹", value)