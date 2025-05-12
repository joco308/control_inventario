import pandas as pd

data = pd.read_csv("farmacia_liam.csv")

class CarBuy:
    total_earnings = 0
    def __init__(self):
        self.list_buy = []
        self.total = 0

    def add_list_buy(self,obj,cantidad):
        if int(obj.loc["Cantidad"]) < cantidad:
            return 0
        self.list_buy.append([obj,cantidad])

    def calc_total(self):
        total = 0
        for i in self.list_buy:
            total+=(float(i[0].loc["Costo"])*i[1])
        self.total = total
    
    def buying(self):
        for i in self.list_buy:
            data.iloc[i[0].name]=int(i[0].loc["Cantidad"])-i[1]
        data.to_csv("farmacia_liam.csv",encoding="utf-8",index=False)
        self.total_earnings += self.total
        self.total = 0

    def cancel_buy(self):
        self.total = 0
        self.list_buy = []

cb = CarBuy()
cb.add_list_buy(data.loc[0],3)
cb.add_list_buy(data.loc[1],10)
cb.add_list_buy(data.loc[2],9)

print(cb.calc_total())
cb.cancel_buy()

