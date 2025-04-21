# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # The brand of the smartphone
        self.model = model  # The model of the smartphone
        self.battery_life = battery_life  # The battery life in percentage

    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")

    def send_message(self, phone_number, message):
        print(f"Sending message to {phone_number}: {message}")

    def charge(self):
        self.battery_life = 100  # Charging the phone to full
        print(f"Phone is now fully charged!")

    def display_info(self):
        print(f"Smartphone Info: {self.brand} {self.model} - Battery: {self.battery_life}%")

# Subclass: AndroidPhone (Inherits from Smartphone)
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, battery_life, os_version):
        super().__init__(brand, model, battery_life)  # Call the parent constructor
        self.os_version = os_version  # The Android OS version

    # Overriding the make_call method to demonstrate polymorphism
    def make_call(self, phone_number):
        print(f"Making a call using Android's VoLTE to {phone_number}...")

    # Adding a unique method to AndroidPhone
    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model}...")

    def display_info(self):
        # Calling the parent class method and then adding Android-specific info
        super().display_info()
        print(f"Operating System: Android {self.os_version}")

# Create an instance of the Smartphone class
phone1 = Smartphone("Apple", "iPhone 13", 85)
phone1.display_info()
phone1.make_call("123-456-7890")
phone1.send_message("123-456-7890", "Hello!")
phone1.charge()
phone1.display_info()

print("\n---\n")

# Create an instance of the AndroidPhone subclass
phone2 = AndroidPhone("Samsung", "Galaxy S21", 90, "12.0")
phone2.display_info()
phone2.make_call("987-654-3210")
phone2.send_message("987-654-3210", "Hi there!")
phone2.install_app("WhatsApp")
phone2.charge()
phone2.display_info()
