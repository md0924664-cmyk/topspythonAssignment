# 1.Create a Python dictionary called playlist_prices with at least 5 key-value pairs where the key is a Spotify playlist 
#   name (as a string) and the value is the playlist's price (as an integer). Print the dictionary.

playlist_prices={
    "Hindi":200,
    "English":100,
    "Party":500,
    "Romantic":800,
    "Sad":900
}
print(playlist_prices)


#------------------------------------------------------------------------------------------------------------------------


# 2.Write a function update_playlist_price(playlist, new_price) that updates the price of a given playlist in the
#    playlist_prices dictionary. Test it by updating the price of any one playlist and printing the updated dictionary.


playlist_prices={
    "Hindi":"200",
    "English":"100",
    "Party":"500",
    "Romantic":"800",
    "Sad":"900"
}

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Sad",250)
print(playlist_prices)


#------------------------------------------------------------------------------------------------------------------------


# 3.Remove a playlist from the playlist_prices dictionary using the del statement. Print the dictionary after deletion to 
#   confirm the change.
    

playlist_prices={
    "Hindi":"200",
    "English":"100",
    "Party":"500",
    "Romantic":"800",
    "Sad":"900"
}

print(playlist_prices)

del playlist_prices["Party"]

print(playlist_prices)


#------------------------------------------------------------------------------------------------------------------------


#4.Given two sets: set1 contains the names of restaurants you have ordered from on Zomato, and set2 contains the names of 
#  restaurants you have ordered from on Swiggy, find and print the union and intersection of these sets.
#  <br><br><em><strong>Hint:</strong> Use the union() and intersection() methods of Python sets.</em>

set1 = {"Domino's", "McDonald's", "Pizza Hut", "Subway"}
set2 = {"Pizza Hut", "KFC", "Subway", "Burger King"}

set3 = set1.union(set2)
print("union: ",set3)

set4 = set1.intersection(set2)
print("intersection: ",set4)





