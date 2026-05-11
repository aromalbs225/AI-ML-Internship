from abc import ABC, abstractmethod

# -------------------- GLOBAL ID COUNTER --------------------
user_counter = 100

# -------------------- USER MANAGEMENT --------------------

class User(ABC):
    def __init__(self, name):
        global user_counter
        user_counter += 1
        self._name = name
        self._user_id = user_counter   # Simple ID

    @abstractmethod
    def display(self):
        pass

class Citizen(User):
    def display(self):
        print(f"Citizen | Name: {self._name}, ID: {self._user_id}")

class ServiceProvider(User):
    def display(self):
        print(f"Provider | Name: {self._name}, ID: {self._user_id}")

class Admin(User):
    def display(self):
        print(f"Admin | Name: {self._name}, ID: {self._user_id}")


# -------------------- HEALTHCARE --------------------

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Appointment:
    def __init__(self, citizen, doctor):
        self.citizen = citizen
        self.doctor = doctor

    def show(self):
        print(f"{self.citizen._name} booked with Dr.{self.doctor.name}")


# -------------------- TRANSPORT --------------------

class Vehicle:
    def __init__(self, number):
        self.number = number

class Bus(Vehicle):
    pass

class Taxi(Vehicle):
    pass


# -------------------- EVENT MANAGEMENT --------------------

class Event:
    def __init__(self, name):
        self.name = name

class Registration:
    def __init__(self, user, event):
        self.user = user
        self.event = event

    def show(self):
        print(f"{self.user._name} registered for {self.event.name}")


# -------------------- UTILITY SERVICES --------------------

class ElectricityBill:
    def __init__(self, units):
        self.units = units

    def calculate(self):
        return self.units * 5

class WaterBill:
    def __init__(self, liters):
        self.liters = liters

    def calculate(self):
        return self.liters * 2


# -------------------- FILE HANDLING (TEXT FILE) --------------------

def save_users(users):
    with open("users.txt", "w") as f:
        for u in users:
            f.write(f"{u._name},{u._user_id}\n")

def load_users():
    users = []
    try:
        with open("users.txt", "r") as f:
            for line in f:
                name, uid = line.strip().split(",")
                user = Citizen(name)
                user._user_id = int(uid)  # restore ID
                users.append(user)
    except FileNotFoundError:
        pass
    return users


# -------------------- SEARCH FUNCTION --------------------

def search_user(users, uid):
    for u in users:
        if str(u._user_id) == uid:
            u.display()
            return
    print("User not found!")


# -------------------- MAIN MENU --------------------

def main():
    users = load_users()

    while True:
        print("\n--- SMART CITY SYSTEM ---")
        print("1. Add Citizen")
        print("2. View Users")
        print("3. Search User")
        print("4. Electricity Bill")
        print("5. Save Users")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                user = Citizen(name)
                users.append(user)
                print("User added successfully!")

            elif choice == "2":
                if not users:
                    print("No users found!")
                for u in users:
                    u.display()

            elif choice == "3":
                uid = input("Enter user ID: ")
                search_user(users, uid)

            elif choice == "4":
                units = int(input("Enter units: "))
                bill = ElectricityBill(units)
                print("Bill Amount:", bill.calculate())

            elif choice == "5":
                save_users(users)
                print("Users saved to file!")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter correct data.")



main()