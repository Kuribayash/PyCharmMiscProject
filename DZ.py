class Car:
    def __init__(self, make = 'Lamborgini', model='Hurakan', year= 2014):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print(self.make, self.model,self.year)
an1 = Car()
an1.info()
