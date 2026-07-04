# 1.Create a list called playlist_ids with 5 integers representing Spotify playlist IDs, then use append() to add a 
#   new playlist ID at the end and print the updated list. 

playlist_ids=[11,22,33,44,55]
playlist_ids.append(66)
print(playlist_ids)


#------------------------------------------------------------------------------------------------------------------------


# 2.Simulate a Flipkart shopping cart: start with a list cart_items containing 't-shirt', 'shoes'. Use extend() to add 
#   ['jeans', 'cap'] to the cart, then print the final list of items.

cart_items = ['t-shirt','shoes']
cart_items.extend(['jeans','cap'])
print(cart_items)

#------------------------------------------------------------------------------------------------------------------------


# 3. Write a function remove_last_item(order_list) that pops the last item from a Zomato order list and returns the removed item. 
#     Test it with a sample order_list.

def remove_lst_item(order_list):
    item = order_list.pop()
    print(item)

order_list = ['pizza','burger','fries','coke']
remove_lst_item(order_list)
print(order_list)


#------------------------------------------------------------------------------------------------------------------------


#4.Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second filter and observe what 
#  error you get.Explain in a comment why this happens.<br><br><em><strong>Hint:</strong> Tuples are immutable, 
#  so direct assignment won't work.</em>

insta_filters = ("Aden","Rise","Moon","Lark")
print("Original Tuple :",insta_filters)

insta_filters[1] = "Valencia"
print(insta_filters)

# Erros occurs because tuple is immutable
# immutable means once tuple is created then its element can not be changed 


#------------------------------------------------------------------------------------------------------------------------



#5.Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set of IRCTC train classes 
#  ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or tuple for each. Write one sentence 
#  explaining your choice for both.

favorite_genres = ["rock","pop","action"]
# reason for choosing list : because list is mutable
# Here we use a list because user can add , remove favorite genre at any time 

train_classes = ("Sleeper","AC 3 Tier","AC 2 Tier")
# reason for choosing tuple : because tuple is immutable
# Here we Use a tuple because the train classes are fixed and should not be changed








