# Base class
class Pizza:
    def prepare(self):
        raise NotImplementedError("This method should be overridden")


# Concrete classes
class CheesePizza(Pizza):
    def prepare(self):
        return "Preparing Cheese Pizza"


class PepperoniPizza(Pizza):
    def prepare(self):
        return "Preparing Pepperoni Pizza"


class VeggiePizza(Pizza):
    def prepare(self):
        return "Preparing Veggie Pizza"


# Factory class
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        elif pizza_type == "veggie":
            return VeggiePizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")


# Main function
def main():
    pizza = PizzaFactory.create_pizza("cheese")
    print(pizza.prepare())


if __name__ == "__main__":
    main()
"""Interview Explanation (Simple)

Factory Pattern ek aisa design pattern hai jisme object creation ka logic ek separate factory class me hota hai. Client ko ye nahi pata hota kaunsa exact class ka object ban raha hai, bas type pass karta hai aur factory sahi object return kar deti hai.

🎯 When to Use Factory Pattern?

Jab object creation logic complex ho

Jab multiple subclasses ho

Jab loose coupling chahiye"""