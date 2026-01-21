"""Factory Pattern is used to create a single object, while Abstract Factory Pattern is used to create families of related objects without specifying their concrete classes."""

# Python Code (Abstract Factory Pattern – Burger + Garlic Bread)
# ---------- Product 1: Burger ----------
class Burger:
    def prepare(self):
        raise NotImplementedError


class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")


class StandardBurger(Burger):
    def prepare(self):
        print(
            "Preparing Standard Burger with bun, patty, cheese, and lettuce!"
        )


class PremiumBurger(Burger):
    def prepare(self):
        print(
            "Preparing Premium Burger with gourmet bun, premium patty, "
            "cheese, lettuce, and secret sauce!"
        )


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


# ---------- Product 2: Garlic Bread ----------
class GarlicBread:
    def prepare(self):
        raise NotImplementedError


class BasicGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Basic Garlic Bread with butter and garlic!")


class CheeseGarlicBread(GarlicBread):
    def prepare(self):
        print(
            "Preparing Cheese Garlic Bread with extra cheese and butter!"
        )


class BasicWheatGarlicBread(GarlicBread):
    def prepare(self):
        print("Preparing Basic Wheat Garlic Bread with butter and garlic!")


class CheeseWheatGarlicBread(GarlicBread):
    def prepare(self):
        print(
            "Preparing Cheese Wheat Garlic Bread with extra cheese and butter!"
        )


# ---------- Abstract Factory ----------
class MealFactory:
    def create_burger(self, burger_type):
        raise NotImplementedError

    def create_garlic_bread(self, bread_type):
        raise NotImplementedError


# ---------- Concrete Factories ----------
class SinghBurger(MealFactory):
    def create_burger(self, burger_type):
        if burger_type == "basic":
            return BasicBurger()
        elif burger_type == "standard":
            return StandardBurger()
        elif burger_type == "premium":
            return PremiumBurger()
        else:
            raise ValueError("Invalid burger type!")

    def create_garlic_bread(self, bread_type):
        if bread_type == "basic":
            return BasicGarlicBread()
        elif bread_type == "cheese":
            return CheeseGarlicBread()
        else:
            raise ValueError("Invalid garlic bread type!")


class KingBurger(MealFactory):
    def create_burger(self, burger_type):
        if burger_type == "basic":
            return BasicWheatBurger()
        elif burger_type == "standard":
            return StandardWheatBurger()
        elif burger_type == "premium":
            return PremiumWheatBurger()
        else:
            raise ValueError("Invalid burger type!")

    def create_garlic_bread(self, bread_type):
        if bread_type == "basic":
            return BasicWheatGarlicBread()
        elif bread_type == "cheese":
            return CheeseWheatGarlicBread()
        else:
            raise ValueError("Invalid garlic bread type!")


# ---------- Client Code ----------
if __name__ == "__main__":
    burger_type = "basic"
    garlic_bread_type = "cheese"

    meal_factory = KingBurger()   # Change to SinghBurger() if needed

    burger = meal_factory.create_burger(burger_type)
    garlic_bread = meal_factory.create_garlic_bread(garlic_bread_type)

    burger.prepare()
    garlic_bread.prepare()

# 🧠 Short Explanation (Exam / Interview Ready)

# This code is an example of the Abstract Factory Design Pattern. The MealFactory defines methods for creating multiple related products such as Burger and GarlicBread. Concrete factories like SinghBurger and KingBurger produce families of related items. SinghBurger creates normal bun meals, while KingBurger creates wheat-based meals. The client interacts only with the factory interface, not with concrete product classes. This makes the system flexible, scalable, and compliant with Open-Closed Principle and Dependency Inversion Principle.

# 🎯 One-Line Interview Answer

# “Abstract Factory Pattern provides an interface to create families of related objects without specifying their concrete classes.”