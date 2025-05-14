import flet as ft
import pandas as pd

data = pd.read_csv("farmacia_liam.csv")


#acciones importantes
def delate_car_buy(n):
    global cb
    global colum
    for i , name in enumerate(cb.list_buy):
        if name[2] == n:
            del cb.list_buy[i]



class CarBuy:
    total_earnings = 0
    def __init__(self):
        self.list_buy = []
        self.total = 0

    def add_list_buy(self,obj,cantidad):
        if int(obj["Cantidad"]) < cantidad:
            return 0
        self.list_buy.append([obj,cantidad,obj.iloc[0]])

    def calc_total(self):
        total = 0
        for i in self.list_buy:
            total+=(float(i[0].loc["Costo"])*i[1])
        self.total = total
        return self.total

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


cb.add_list_buy(data[data["Nombre"].str.contains("TAYPIREC")].iloc[0],2)
cb.add_list_buy(data[data["Nombre"].str.contains("COLGATE FAMILIAR 180 gr")].iloc[0],1)
#list_print_buy(cb.list_buy)

#print(cb.list_buy)
