# Python Code (Abstract Factory Pattern – Burger Example)
# -------- Product Interface --------
class Burger:
    def prepare(self):
        raise NotImplementedError


# -------- Concrete Products (Normal Buns) --------
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


# -------- Concrete Products (Wheat Buns) --------
class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")


class StandardWheatBurger(Burger):
    def prepare(self):
        print(
            "Preparing Standard Wheat Burger with bun, patty, "
            "cheese, and lettuce!"
        )


class PremiumWheatBurger(Burger):
    def prepare(self):
        print(
            "Preparing Premium Wheat Burger with gourmet bun, premium patty, "
            "cheese, lettuce, and secret sauce!"
        )


# -------- Factory Interface --------
class BurgerFactory:
    def create_burger(self, burger_type):
        raise NotImplementedError


# -------- Concrete Factories --------
class SinghBurger(BurgerFactory):
    def create_burger(self, burger_type):
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError("Invalid burger type!")


class KingBurger(BurgerFactory):
    def create_burger(self, burger_type):
        if burger_type == "basic":
            return BasicWheatBurger()
        elif burger_type == "standard":
            return StandardWheatBurger()
        elif burger_type == "premium":
            return PremiumWheatBurger()
        else:
            raise ValueError("Invalid burger type!")


# -------- Client Code --------
if __name__ == "__main__":
    burger_type = "basic"

    factory = SinghBurger()   # Change to KingBurger() for wheat burgers
    burger = factory.create_burger(burger_type)
    burger.prepare()

# 🧠 What Pattern Is This? (Short Explanation)

# This is an example of the Abstract Factory Design Pattern.
# Here, BurgerFactory is an abstract factory that defines what kind of burger to create, but not how it is created. SinghBurger and KingBurger are concrete factories that produce families of related products. SinghBurger creates normal-bun burgers, while KingBurger creates wheat-bun burgers. The client code only talks to the factory interface and never directly creates burger objects. This makes the system flexible, scalable, and easy to extend.

# 🎯 Interview One-Liner

# “Abstract Factory Pattern provides an interface for creating families of related objects without specifying their concrete classes.”