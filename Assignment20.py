# 1.Create a Python class called Product with a private attribute _price. Initialize _price in the constructor and 
#    write a method to display its value.


class Product:
    def __init__(self, price):
        self._price = price  

    def display_price(self):
        print("Product Price:", self._price)

product1 = Product(499)
product1.display_price()


#--------------------------------------------------------------------------------------------------------------------------------------

#2.Add getter and setter methods for the _price attribute in your Product class to safely access and update the price. Make sure the 
#  setter prevents setting a negative price.<br><br><em><strong>Hint:</strong> Raise a ValueError if the new price is less than zero.</em>

class Product:
    def __init__(self,price):
        self._price =price
        
    # Getter method
    def get_price(self):
        return self._price
    
    # Setter method
    def set_price(self,price):
        if price<0:
            raise ValueError("Price cannot be negative")
        self._price=price
        
product1=Product(250)
product1.set_price(200)
print(product1.get_price())

#--------------------------------------------------------------------------------------------------------------------------------------

#3.Build a class called Playlist that has a private attribute _songs (a list of song names). Write methods to add a song, remove a song, 
#  and get the current list of songs using proper encapsulation.

class Playlist:
    def __init__(self):
        self._songs = []     
    def add_song(self, song):
        self._songs.append(song)

    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
        else:
            print("Song not found!")

    def get_songs(self):
        return self._songs


# Create Playlist object
playlist = Playlist()

# Add songs
playlist.add_song("Kesariya")
playlist.add_song("Believer")
playlist.add_song("Shape of You")

# Display songs
print("Playlist:", playlist.get_songs())

# Remove a song
playlist.remove_song("Believer")

# Display updated playlist
print("Updated Playlist:", playlist.get_songs())   

#--------------------------------------------------------------------------------------------------------------------------------------

#4.Create an abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: UPI and CreditCard, 
#  each implementing the pay method with a print statement showing how the payment would be processed.<br><br><em><strong>Hint:
#  </strong> Use the abc module for abstraction.</em>


from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):

    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using UPI.")

class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using Credit Card.")


# Objects
upi = UPI()
card = CreditCard()

# Method Calls
upi.pay(500)
card.pay(1200)


