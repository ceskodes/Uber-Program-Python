from uberx import UberX
from uberpool import UberPool
from uberblack import UberBlack
from ubervan import UberVan
from user import User
from driver import Driver

if __name__ == "__main__":
    Car1 = UberX(1, "AMS321", Driver(1, "Carlos Silva", "V25643915", "Caensi95@gmail.com", 1234), 3, "Chery", "Arauca")
    print(Car1.get_driver())