# 1.create a Python script that takes any product name string (e.g., 'Redmi Note 12 Pro') and prints the name in all uppercase 
  # and all lowercase using the upper() and lower() methods. 

product = "Redmi Note 12 pro"
print(product.upper())
print(product.lower())


#------------------------------------------------------------------------------------------------------------------------

# 2.Write a function clean_brand_name(name) that removes leading/trailing spaces and replaces any hyphens '-' with a single 
  # space in the input string. Test it with ' oneplus-Nord '.

def clean_brand_name(name):
    name = name.strip()          
    name = name.replace("-", " ")  
    print(name)

clean_brand_name("  oneplus-Nord  ")



#------------------------------------------------------------------------------------------------------------------------

# 3. Given the string 'Apple iPhone 14 Pro Max', use string slicing to extract and print only the brand name and the model 
 # (i.e., 'Apple' and 'iPhone 14 Pro Max') separately.<br><br><em><strong>Hint:</strong> Use split() to help find 
 # the split point, then use slicing for the substrings.</em>


phone = " Apple iPhone 14 pro max"

words = phone.split()
brand = words[0]

model = " ".join(words[1: ])

print("Brand :",brand)
print("model",model) 


#------------------------------------------------------------------------------------------------------------------------

#4 Build a function format_product_display(name, price) that takes a product name and price (e.g., 'Boat Earbuds', 1299)
#  and returns a formatted string like 'Boat Earbuds - ₹1299'

def format_product_display(name, price):
  print(name,"- ₹"+ str(price))
    

format_product_display("Boat Earbuds", 1299)



#------------------------------------------------------------------------------------------------------------------------

# 5.Suppose you have a list of messy product names: [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']. Write code to clean 
#   each name (remove spaces, replace hyphens with spaces, and make the brand title case) and print the cleaned list.
#   <br><br><em><strong>Constraint:</strong> Use at least three string methods from this session.</em>

products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']


clean_products =[]

for i in products:
    i = i.strip()
    i = i.replace("-"," ")
    i = i.title()
    clean_products.append(i)

print(clean_products)




    