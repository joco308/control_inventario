import flet as ft
import pandas as pd

data = pd.read_csv("farmacia_liam.csv")
dataCopy = data.copy()


#acciones importantes
def delate_car_buy(n):
    global cb
    for i , name in enumerate(cb.list_buy):
        if name[2] == n:
            del cb.list_buy[i]


def search_element(n):
    list_search = dataCopy[dataCopy["Nombre"].str.contains(n)]
    return list_search
def save_changes(e):
    data = dataCopy.copy()
    data.to_csv("farmacia_liam.csv",encoding="utf-8",index=False)
    


class CarBuy:
    total_earnings = 0
    def __init__(self):
        self.list_buy = []
        self.total = 0

    def add_list_buy(self,obj,cantidad):
        if int(obj["Cantidad"]) < cantidad:
            print("hola")
            return 0
        self.list_buy.append([obj,cantidad,obj.iloc[0]])
        dataCopy.loc[dataCopy["Nombre"]==obj["Nombre"],"Cantidad"]=obj["Cantidad"]-cantidad
        #print(dataCopy.loc[dataCopy["Nombre"]==obj["Nombre"]])

    def calc_total(self):
        total = 0
        for i in self.list_buy:
            total+=(float(i[0].loc["Costo"])*i[1])
        self.total = total
        return self.total

    def buying(self):
        data = dataCopy.copy()
        data.to_csv("farmacia_liam.csv",encoding="utf-8",index=False)
        self.list_buy = []
        self.total_earnings += self.total
        self.total = 0

    def cancel_buy(self):
        self.total = 0
        self.list_buy = []




cb = CarBuy()



""" cb.add_list_buy(dataCopy[dataCopy["Nombre"].str.contains("taypirec")].iloc[0],2)
cb.add_list_buy(dataCopy[dataCopy["Nombre"].str.contains("COLGATE FAMILIAR 180 gr".lower())].iloc[0],1) """
#list_print_buy(cb.list_buy)

#print(data[data["Nombre"]=="taypirec"].iloc[0].loc["Nombre"])
