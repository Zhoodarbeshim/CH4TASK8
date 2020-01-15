class Dollarize():    
    def __init__(self, money):
        self.money = money

    def update(self, new_money):
        self.money = new_money
    
    def __repr__(self):
        self.currency = str(self.money)
    
    def __str__(self):
        self.money = self.currency


a = 123456.7890

print('${:,.3f}'.format(a))