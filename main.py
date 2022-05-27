from uberx import UberX
from uberpool import UberPool
from uberblack import UberBlack
from ubervan import UberVan
from user import User
from driver import Driver

if __name__ == "__main__":
    Car1 = UberX(1, "AMS321", Driver(1, "Carlos Silva", "V25643915", "Caensi95@gmail.com", 1234), 4, "Chery", "Arauca")
    print(vars(Car1))

    Car2 = UberVan(2, "FTS123", Driver(2, "Luz Mar", "V5348227", "ramluzmar25@gmail.com", 5678), 6, "Daihatsu", "Terios")
    print(vars(Car2))