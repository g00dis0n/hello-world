# A demonstration of classes using the exercises from chapter 9 of Python Crash Course by Eric Matthes

class Restaurant:
    """simulate a restaurant"""

    def __init__(self, name, cuisine):
        """name of restaurant and food served"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """brief description of the restaurant"""
        print(f"{self.name} serves {self.cuisine}")

    def open_restaurant(self):
        """states if restaurant is open or closed"""
        print(f"{self.name} is open")

    def set_number_served(self, number_served):
        """customers served to date"""
        self.number_served = number_served

    def increment_customers_served(self, served):
        """increments numbers of customers served"""
        self.number_served += served


class IceCreamStand(Restaurant):
    """a subclass of Restaurant specific to ice cream stands"""
    def __init__(self, name, cuisine='ice cream'):
        super().__init__(name, cuisine)
        self.flavours = []

    def show_flavours(self):
        """display ice cream flavours"""
        print('The following flavours are available: ')
        for flavour in self.flavours:
            print(f'> {flavour}')


# instantiation
restaurant1 = Restaurant("Antonio's", "Italian food")
restaurant2 = Restaurant("Wong's", "Chinese food")
restaurant3 = Restaurant("Sanjay's", "Indian food")

# overview of restaurant 1
print(f"Restaurant Name: {restaurant1.name}\n"
      f"Serves: {restaurant1.cuisine}")

# call the open_restaurant
restaurant1.open_restaurant()

# set customers served to date
restaurant1.set_number_served(1000)
print(f'Customers served to date: {restaurant1.number_served}')

# increase customers served
print(f"Adding more customers..")
restaurant1.increment_customers_served(500)

# new total amount of customer served
print(f"Total customers served now: {restaurant1.number_served}")

# above lines repeated to ensure customer incrementation is correct
print(f"Adding more customers..")
restaurant1.increment_customers_served(25)
print(f"Total customers served now: {restaurant1.number_served}")
print("")

# test of ice cream subclass of restaurant
icecreamstand1 = IceCreamStand('Igloo Ice Cream')
icecreamstand1.flavours = ['strawberry', 'banana', 'chocolate']
icecreamstand1.describe_restaurant()
icecreamstand1.show_flavours()
icecreamstand1.set_number_served(245)
print(f'Customers served to date: {icecreamstand1.number_served}')
