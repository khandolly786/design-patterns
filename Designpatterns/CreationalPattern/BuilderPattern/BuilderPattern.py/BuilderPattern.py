# Builder Pattern Solution
# Step 1️⃣: Product (Car)
class Car:
    def __init__(self):
        self.engine = None
        self.ac = False
        self.sunroof = False
        self.music_system = False

    def show(self):
        print("Engine:", self.engine)
        print("AC:", self.ac)
        print("Sunroof:", self.sunroof)
        print("Music System:", self.music_system)

# Step 2️⃣: Builder
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self, engine):
        self.car.engine = engine
        return self

    def add_ac(self):
        self.car.ac = True
        return self

    def add_sunroof(self):
        self.car.sunroof = True
        return self

    def add_music_system(self):
        self.car.music_system = True
        return self

    def build(self):
        return self.car

# Step 3️⃣: Client Code
builder = CarBuilder()

car = (
    builder
    .add_engine("Petrol")
    .add_ac()
    .add_music_system()
    .build()
)

car.show()

# 🎯 Output (Conceptually)
# Engine: Petrol
# AC: True
# Sunroof: False
# Music System: True

"""Why Builder Pattern is Good?

✅ No constructor overload
✅ Readable & clean code
✅ Optional features easy
✅ Same building process → different results"""
"""Builder vs Factory (Common Confusion)
Builder	Factory
Step-by-step creation	One-shot creation
Complex object	Simple object
Many optional fields	Few variations
Focus: how to build	Focus: what to build
🎯 Interview One-Liner

“Builder Pattern is used to construct complex objects step by step and allows different representations using the same construction process.”

🧠 Yaad rakhne ka Trick

❌ Constructor me bohot parameters → Builder

✅ Object step-by-step banana → Builder"""