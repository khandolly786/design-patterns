# Galat design (DIP violate)

# Socho:

class WiredKeyboard:
    def type(self):
        print("Typing with wired keyboard")


class Computer:
    def __init__(self):
        self.keyboard = WiredKeyboard()

    def work(self):
        self.keyboard.type()


# 🗣️ Problem suno:

# Computer bol raha hai:
# 👉 “Mujhe sirf wired keyboard chahiye”

# Kal kya hoga?

# Bluetooth keyboard lana hai ❌

# Testing ke liye fake keyboard chahiye ❌

# 👉 Computer class modify karni padegi
# 👉 Tight coupling
# 👉 DIP violate ❌

# Sahi DIP design (simple)
# Step 1️⃣: Rule / Interface banao
class Keyboard:
    def type(self):
        pass


# 🗣️ Matlab:

# “Jo bhi keyboard hoga, type kar sakta hoga”

# Step 2️⃣: Real keyboards rule follow karein
class WiredKeyboard(Keyboard):
    def type(self):
        print("Typing with wired keyboard")

class BluetoothKeyboard(Keyboard):
    def type(self):
        print("Typing with bluetooth keyboard")

# Step 3️⃣: Computer rule pe depend kare
class Computer:
    def __init__(self, keyboard: Keyboard):
        self.keyboard = keyboard

    def work(self):
        self.keyboard.type()


# 🧠 Ab dekho magic:

# Computer ko farak nahi padta:

# wired hai

# bluetooth hai

# fake hai

# Bas ek baat pata:
# 👉 “keyboard type kar sakta hai”

# 🎯 Use karke dekho
computer = Computer(WiredKeyboard())
computer.work()

computer = Computer(BluetoothKeyboard())
computer.work()


# ✔ Computer ka code same
# ✔ Keyboard change
# ✔ DIP follow

# 🔁 Ye kya hua?

# High-level class → Computer

# Low-level class → WiredKeyboard / BluetoothKeyboard

# Abstraction → Keyboard interface

# 👉 Sab abstraction pe depend kar rahe hain

# 🧠 Ab HTTP example ko easy banao

# HTTP example me:

# Computer = Http

# Keyboard = Connection

# WiredKeyboard = XMLHttpService

# BluetoothKeyboard = MockHttpService

# Bas itna hi hai 😄

# ❌ HTTP me galti kya thi?
class Http:
    def __init__(self):
        self.service = XMLHttpService()  # hard dependency


# 👉 Same wired keyboard wali problem

# ✅ HTTP ka simple version
class Connection:
    def request(self):
        pass

class Http:
    def __init__(self, connection: Connection):
        self.connection = connection


# 👉 Ab Http free ho gaya 🎉

# 🧠 DIP ko yaad rakhne ka SUPER TRICK

# 🧠 Never do this ❌

# self.obj = ConcreteClass()


# 🧠 Always do this ✅

# self.obj = InterfaceType

# 🧠 Interview me kaise bolna (simple)

# “DIP means high-level classes should not depend on low-level classes directly. They should depend on interfaces so that implementations can be easily changed without modifying existing code.”
"""
Dependency Inversion Principle

Dependency should be on abstractions not concretions A. High-level modules
should not depend upon low-level modules. Both should depend upon abstractions.
B. Abstractions should not depend on details. Details should depend upon
abstractions.

There comes a point in software development where our app will be largely
composed of modules.  When this happens, we have to clear things up by using
dependency injection.  High-level components depending on low-level components
to function.
"""

class XMLHttpService(XMLHttpRequestService): #type: ignore
    pass

class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.xml_http_service.request(url, 'POST')

"""
Here, Http is the high-level component whereas XMLHttpService is the low-level
component.  This design violates DIP A: High-level modules should not depend on
low-level modules. It should depend upon its abstraction.

Ths Http class is forced to depend upon the XMLHttpService class.  If we were to
change the Http connection service, maybe we want to connect to the internet
through cURL or even Mock the http service.  We will painstakingly have to move
through all the instances of Http to edit the code and this violates the OCP
principle.

The Http class should care less the type of Http service you are using. We make
a Connection interface:
"""

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

"""
The Connection interface has a request method. With this, we pass in an argument
of type Connection to our Http class:
"""

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.http_connection.request(url, 'POST')

"""
So now, no matter the type of Http connection service passed to Http it can
easily connect to a network without bothering to know the type of network
connection.

We can now re-implement our XMLHttpService class to implement the Connection
interface:
"""

class XMLHttpService(Connection):
    xhr = XMLHttpRequest()#type: ignore

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()

"""
We can create many Http Connection types and pass it to our Http class without
any fuss about errors.
"""
class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

class MockHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

"""
Now, we can see that both high-level modules and low-level modules depend on
abstractions.  Http class(high level module) depends on the Connection
interface(abstraction) and the Http service types(low level modules) in turn,
depends on the Connection interface(abstraction).

Also, this DIP will force us not to violate the Liskov Substitution Principle:
The Connection types Node-XML-MockHttpService are substitutable for their parent
type Connection.
"""