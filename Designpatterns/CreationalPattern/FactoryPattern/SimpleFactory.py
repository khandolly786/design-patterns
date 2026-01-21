# Python Code (Factory Design Pattern – Burger Example)
# --- Product Interface ---
class Burger:
    def prepare(self):
        raise NotImplementedError


# --- Concrete Products ---
class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")


class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")


class PremiumBurger(Burger):
    def prepare(self):
        print(
            "Preparing Premium Burger with gourmet bun, premium patty, "
            "cheese, lettuce, and secret sauce!"
        )


# --- Factory Class ---
class BurgerFactory:
    def create_burger(self, burger_type):
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError("Invalid burger type!")


# --- Client Code ---
if __name__ == "__main__":
    burger_type = "standard"

    factory = BurgerFactory()
    burger = factory.create_burger(burger_type)
    burger.prepare()

# 🧠 Paragraph Explanation (Simple & Clear)

# This code demonstrates the Factory Design Pattern. The main idea of the Factory Pattern is to hide object creation logic from the client and provide a common interface to create objects. Here, Burger is an abstract base class that defines the prepare() method. Different burger types like BasicBurger, StandardBurger, and PremiumBurger provide their own implementations of this method. The BurgerFactory class is responsible for deciding which burger object to create based on the input type. The client code does not directly create burger objects using constructors; instead, it asks the factory to create the required burger. This makes the code clean, flexible, and easy to extend. If a new burger type is added in the future, only the factory needs to be updated, while the client code remains unchanged.

# 🎯 One-Line Interview Answer

# “The Factory Pattern provides a way to create objects without exposing the creation logic to the client and refers to newly created objects using a common interface.”

 