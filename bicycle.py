class Bicycle(object): #spec
    def __init__(self, name, weight, cost): 
        self.name = name
        self.weight = weight
        self.cost = cost

class BikeShop(object):
    def __init__(self, name, inventory, margin, profit):
        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
    
class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund

fashionable = Bicycle("high-society", 15, 450)
road = Bicycle("road-trip", 25, 750)
cyclocross = Bicycle("crosscycle", 30, 500)
touring = Bicycle("tourlefrance", 28, 800)
triathlon = Bicycle("seriousspeed", 20, 1000)
flat = Bicycle("flatbard", 18, 750)

shop1_inventory = [fashionable, road, cyclocross, touring, triathlon, flat]
shop1 = BikeShop("Bathurst", shop1_inventory, 20, 3000)
customer1 = Customer("Andrea", 450)
customer2 = Customer("Beatrice", 1000)
customer3 = Customer("Sylvia", 850)


