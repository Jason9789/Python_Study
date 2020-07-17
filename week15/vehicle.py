
class Vehicle:
    def __init__(self, maker, model, color, price):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price

    def set_maker(self, maker):
        self.maker = maker

    def get_maker(self):
        return self.maker

    def get_desc(self):
        return '차량 = (' + \
            str(self.maker) + ', ' + \
            str(self.model) + ', ' + \
            str(self.color) + ', ' + \
            str(self.price) + ')'


class Truck(Vehicle):
    def __init__(self, maker, model, color, price, payload):
        super().__init__(maker, model, color, price)
        self.payload = payload

    def set_payload(self, payload):
        self.payload = payload

    def get_payload(self):
        return self.payload

    def get_desc(self):
        return '차량 = (' + \
            str(self.maker) + ', ' + \
            str(self.model) + ', ' + \
            str(self.color) + ', ' + \
            str(self.price) + ', ' + \
            str(self.payload) + ')'


def main():
    my_truck = Truck('Tesla', 'Model S', 'white', 10000, 2000)
    print(my_truck.get_desc())
    my_truck.set_maker('Hyundai')
    my_truck.set_payload(1000)
    print(my_truck.get_desc())


main()
