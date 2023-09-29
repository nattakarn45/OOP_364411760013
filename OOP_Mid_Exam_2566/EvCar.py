class ThaiEvCar:
    my_thaiEvCar = []

    def __init__(self, carid ,model, brand,  acelerationrate, HP, range, price):
        self.carid = carid
        self.model = model
        self.brand = brand
        self.acelerationrate = acelerationrate
        self.HP = HP
        self.range = range
        self.price = price

    def ThaiEvCar_detail(self):
        print(f'carid:{self.carid} '
              f'model:{self.model} '
              f'brand:{self.brand} '
              f'acelerationrate:{self.acelerationrate} '
              f'HP:{self.HP} '
              f'range:{self.range} '
              f'price:{self.price} ')

    def delete_ThaiEvCar(self,index):
        self.my_thaiEvCar.pop(index)

    def edit_ThaiEvCar_price(self,index,new_price):
        self.my_thaiEvCar[index].price = new_price