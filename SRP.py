# Single Responsibility Principal
# Correct SRP Design (Separated Responsibilities)
# ✔ Step 1: Animal class → only animal data
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

# ✔ Step 2: Database responsibility moved to another class
class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

# ✅ Now responsibilities are clear:
# Class	Responsibility
# Animal	Animal properties
# AnimalDB	Database operations


# USING FACADE PATTERN
class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        return self.name

    def get(self, id):
        return self.db.get_animal(id)
    
    def save(self):
        self.db.save(animal=self)
"""How this solves everything

AnimalDB still handles database logic

Animal acts as a front layer (Facade)

Client only interacts with Animal

Internally, Animal delegates work to AnimalDB

👉 SRP is not broken, because:

Database logic is still separated

Animal class just uses it

🧠 Easy Interview Explanation (You can say this)

“Initially, the Animal class violated SRP because it handled both animal data and database logic.
To fix this, database operations were moved to a separate AnimalDB class.
To avoid exposing multiple classes to the client, the Facade pattern was applied, where the Animal class provides simple methods and internally delegates database operations.”

📝 One-Line Summary

❌ Mixing data + DB logic → SRP violation

✅ Separate responsibilities → SRP followed

⭐ Facade pattern → clean + user-friendly design"""