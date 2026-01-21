# Open for extension = naya behaviour add kar sakte ho
# 👉 Closed for modification = existing code ko chedna nahi

# ❌ Pehla Animal example – OCP violation
def animal_sound(animals):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
# 🗣️ Soch ke dekho:

# Aaj lion, mouse

# Kal snake aa gaya

# Parson dog aa gaya

# Har baar kya kar rahe ho?
# 👉 animal_sound function modify kar rahe ho
        elif animal.name == 'snake':
            print('hiss')
        else:
            return None


# ❌ Yahi OCP violation hai

# 🚨 Problem kya hogi future me?

# Code bada hoga

# if-else chain aur lambi hoti jaayegi

# Same logic har jagah repeat hogi

# Ek change → bahut jagah impact

# 👉 Rigid & fragile system

# ✅ OCP ka sahi solution (Polymorphism)
# Step 1️⃣: Animal class me common method
class Animal:
    def make_sound(self):
        pass


# 🗣️ Matlab:

# “Har animal awaaz nikalta hai,
# par kaunsi awaaz – wo animal decide karega”

# Step 2️⃣: Har animal apni class
class Lion(Animal):
    def make_sound(self):
        return 'roar'

class Mouse(Animal):
    def make_sound(self):
        return 'squeak'

class Snake(Animal):
    def make_sound(self):
        return 'hiss'

# Step 3️⃣: animal_sound function simple ho gaya
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# 🧠 Ab dhyaan do:

# ❌ No if-else

# ❌ No name checking

# ✅ Only method call

# 🎯 Ab naya animal add karna?
class Dog(Animal):
    def make_sound(self):
        return 'bark'


# 👉 animal_sound change nahi hua
# 👉 OCP followed ✔

# 🔹 Discount example – same OCP concept
# ❌ Wrong approach

def give_discount():
    if customer == 'fav': # type: ignore
        20%
    if customer == 'vip': # type: ignore
        40% #type: ignore 
    else:
        return None


# 🗣️ Matlab:

# Naya customer type = naya if

# Function modify hota ja raha hai ❌

# ✅ Correct OCP way (Inheritance)
price= 100
class Discount:
    def get_discount(self):
        return price * 0.2

# VIP ke liye extend kiya
class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

# Super VIP ke liye aur extend
class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2


"""🧠 Notice karo:

Purana code touch nahi hua

Sirf new class add hui

👉 Open for extension, Closed for modification ✔

🧠 Interview me kaise bolna hai (ready answer)

“Open–Closed Principle states that software entities should be open for extension but closed for modification.
Instead of adding conditional logic, we use inheritance and polymorphism so new behavior can be added without changing existing code.”"""