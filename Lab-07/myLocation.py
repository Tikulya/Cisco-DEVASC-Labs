
class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("salam aleykum, moe pogonyalo " + self.name +
              " i ya obitayou " + self.country + ".")


loc1 = Location("Kani", "zona 51")
loc2 = Location("Talip", "tyur'ma dlya nesovershenoletnih")
loc3 = Location("Dias", "podval")
your_loc = Location("Tiku", "Kyrgyz Repablic")

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()

class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

loc = Location("Tiku", "Kyrgyz Repablic")

print(loc.name)
print(loc.country)
print(type(loc))
