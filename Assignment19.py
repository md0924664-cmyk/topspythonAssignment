#1.Define a Python class called Song with attributes title, artist, and duration (in seconds), and use the __init__() constructor to
#  initialize these values when creating an object.

class song():
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    
song1 = song("song1","artist1",200)

print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration)


#---------------------------------------------------------------------------------------------------------------------------------------------

#2. Create an object of the Song class for your favorite track from Spotify, and print out its title and artist using object attributes.


class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        


song1 = Song("Darkhaast", " Arijit Singh & Sunidhi Chauhan ", 269)

print("Title :", song1.title)
print("Artist :", song1.artist)

#---------------------------------------------------------------------------------------------------------------------------------------------------

#3. Add a method play_preview(self) to your Song class that prints 'Playing 30-second preview of [title] by [artist]'. 
#    Call this method for your Song object.

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")


song1 = Song("Darkhaast", "Arijit Singh")

# Call the method
song1.play_preview()

#------------------------------------------------------------------------------------------------------------------------------------------

# 4.Create a class called FoodOrder with attributes restaurant_name, items (a list), and total_price. Add a method add_item(self, item, price) that
#   adds the item to the items list and updates total_price. Demonstrate by creating a FoodOrder object and adding two items like you would on Zomato. 


class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price


# Create a FoodOrder object
order = FoodOrder("Zomato")

# Add two items
order.add_item("Pizza", 299)
order.add_item("Burger", 149)

# Display the order details
print("Restaurant:", order.restaurant_name)
print("Items:", order.items)
print("Total Price:", order.total_price)

#------------------------------------------------------------------------------------------------------------------------------------------

#5.Refactor your Song class so that it also tracks a play_count attribute (starting at 0), and add a method increment_play_count(self)
#  that increases play_count by 1 each time it's called. Show how you would use this to count how many times a user plays a song.
#  <br><br><em><strong>Hint:</strong> Call increment_play_count() multiple times and print play_count to see the update.</em>

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.play_count = 0

    def increment_play_count(self):
        self.play_count += 1


# Create a Song object
song1 = Song("Darkhaast", "Arijit Singh")

# User plays the song
song1.increment_play_count()
song1.increment_play_count()
song1.increment_play_count()

# Display play count
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Play Count:", song1.play_count)
