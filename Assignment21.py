#1.Create a Python class called Product with a method get_discount() that returns 0. Write a subclass called Electronics 
# that overrides get_discount() to return 10.

class product:
    def get_discount(self):
        return 0

class Electronics(product):
    def get_discount(self):
        return 10

p = product()
e = Electronics()

print("product discount :",p.get_discount())
print("Electronics discount :",e.get_discount())


# # ------------------------------------------------------------------------------------------------------------------------------

# # 2.Build a class FoodOrder with a method calculate_total() that returns the base price. Create a subclass ZomatoOrder 
# #   that overrides calculate_total() to add a 5% delivery charge.

class food_order():
    def calculate_total(self):
        return 200

class zomato_order(food_order):
    def calculate_total(self):
        base_price = 200
        delivery_charge = base_price * 5/100
        return base_price + delivery_charge 

f = food_order()
z = zomato_order()

print("food total :",f.calculate_total())
print("zomato total :",z.calculate_total())        


# ------------------------------------------------------------------------------------------------------------------------------

#3.Write a function show_bonus(employee) that takes any object with a bonus() method and prints the result. Test it with two
#  classes: Influencer (bonus returns 2000) and BrandManager (bonus returns 5000), demonstrating polymorphism.\

def show_bonus(employee):
    print("Bonus :",employee.bonus())
    
class influencer():
    def bonus(self):
        return 2000

class brand_manager():
    def bonus(self):
        return 5000

i = influencer()
b = brand_manager()

show_bonus(i)
show_bonus(b)


# ------------------------------------------------------------------------------------------------------------------------------

# 4.Given this code: class User: def get_status(self): return 'active' class PremiumUser(User): pass. Update PremiumUser
#   to override get_status() so it returns 'premium'. Then, create one User and one PremiumUser and print their statuses.
#   <br><br><em><strong>Hint:</strong> Use the same method name in both classes to override.</em>

class User():
    def get_status(self):
        return 'active'

class PremiumUser(User):
    def get_status(self):
        return "premium"

u = User()
p = PremiumUser()
        
print("User status :",u.get_status())
print("Premium User status :",p.get_status())


