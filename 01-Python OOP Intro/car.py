class Car:
    # dunder: double underscore
    # 어떤 항목이 들어가야 하는지 적기
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Identical for each car object
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
