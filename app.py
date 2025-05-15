import flet as ft
import logic as lg


#clases de busqueda
class Search:
    def __init__(self,name):
        self.name = name
        self.date =  lg.dataCopy[lg.dataCopy["Nombre"]==name].iloc[0]
        self.catidad = 1

    def change_value(self,e):
        try:
            self.catidad = int(e.control.value)
            #print(type(self.catidad))
        except:
            self.catidad = 1
    
    def buton_acction(self,e):
        #print(lg.dataCopy.loc[lg.dataCopy["Nombre"]==self.name])
        date =  lg.dataCopy.loc[lg.dataCopy["Nombre"]==self.name].iloc[0]
        #print(date)
        lg.cb.add_list_buy(date,self.catidad)
        update_column()

    def text(self):
        return ft.Text(
            f"{str(self.date.iloc[0])}",

        )
    
    def cantidad(self):
        return ft.Text(
            f"{str(self.date.iloc[2])}"
        )
    
    def text_field(self):
        return ft.TextField(
            value=str(self.catidad),
            #input_filter =ft.InputFilter(allow=r"[0-9]"),
            width=40,
            on_change=self.change_value,
            border_radius=20,
            bgcolor="#2E2E3E",
            color="#E0E0E0",
            border_color="#3A3A4A"
        )
    
    def buton_add(self):
        return ft.ElevatedButton(
            text="Agregar",
            on_click=self.buton_acction,
            bgcolor="#4CAF50",
            color="#FFFFFF"
        )

class SearchInv(Search):
    def __init__(self, name):
        super().__init__(name)
        self.cantidadt = int(self.date.iloc[2])
    def fecha_ven(self):
        return ft.Text(
            f"{self.date.iloc[3]}"
        )
    
    def change_value(self, e):
        try:
            d = int(e.control.value)
        except:
            d = self.cantidadt
        finally:
            self.cantidadt = d
            print(self.cantidadt)

    def buton_acction(self, e):
        lg.dataCopy.loc[lg.dataCopy["Nombre"]==self.name, "Cantidad"] = self.cantidadt
        print(lg.dataCopy.loc[lg.dataCopy["Nombre"]==self.name])

    def text_field(self):
        return ft.TextField(
            value=str(self.cantidadt),
            #input_filter =ft.InputFilter(allow=r"[0-9]"),
            width=90,
            on_change=self.change_value,
            border_radius=20,
            bgcolor="#2E2E3E",
            color="#E0E0E0",
            border_color="#3A3A4A"
        )
    



#elementos que se actualizan
f_ref = ft.Ref[ft.Text]()

colum = ft.Column(controls=[ft.Text("Carrito de compra")])
columSearch = ft.Column(controls=[ft.Text("Busqueda")],scroll=ft.ScrollMode.AUTO)
columSearchInv = ft.Column(controls=[ft.Text("Busca para agregar o reducir inventario")],scroll=True,height=700)

#logic
def relizar_compra(e):
    global columSearch
    lg.cb.buying()
    update_column()
    columSearch.clean()
    columSearch.controls.extend(lis_print_search(search))
    columSearch.update()



def update_column(n=None):
    if n != None:
        lg.delate_car_buy(n[0].iloc[0])
        lg.dataCopy.loc[lg.dataCopy["Nombre"]==n[0].iloc[0],"Cantidad"] = n[0].iloc[2] + n[1]
    global f_ref, colum
    
    colum.controls.clear()
    colum.controls.extend(list_print_buy(lg.cb.list_buy))
    f_ref.current.value = f"{lg.cb.calc_total()} Bs."
    #print(lg.cb.calc_total())
    f_ref.current.update()
    colum.update()

def create_search_objet(n):
    return Search(n)
def create_serch_inv(n):
    return SearchInv(n)

#apratados que se actualizan
def buton_create(n):
    return ft.IconButton(
        icon=ft.Icons.CANCEL,
        icon_color="#D32F2F",
        on_click=lambda e: update_column(n)
    )
def list_print_buy(list):
    listPrint = []
    for x in list:
        listPrint.append(ft.Row(
            controls=[
                ft.Text(f"{x[0].iloc[0]}"),
                ft.Row(
                    controls=[
                        ft.Text(f"{x[1]}"),
                        ft.Text(f"{x[1]*x[0].iloc[1]} Bs."),
                        buton_create(x)
                    ],
                    spacing=30,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    width=200
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            width=600
            ))
    #print(listPrint)
    return listPrint
def lis_print_search(list):
    listf = []
    for i in list["Nombre"]:
        listf.append(create_search_objet(i))

    lPrint = []
    for i in listf:
        lPrint.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        i.text(),
                        i.cantidad(),
                        ft.Row(
                            controls=[
                                i.text_field(),
                                i.buton_add()                         
                            ]
                        )
                    ],
                    
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=20,
                    width=600
                ),
                bgcolor="#1A1A28",
                border_radius = ft.border_radius.all(10),
                padding=ft.padding.symmetric(horizontal=10)
            )
        )
    return lPrint
def list_print_inv(list):
    ls = []
    for i in list["Nombre"]:
        ls.append(create_serch_inv(i))

    lPrint = []
    for i in ls:
        lPrint.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        i.text(),
                        i.fecha_ven(),
                        ft.Row(
                            controls=[
                                i.text_field(),
                                i.buton_add()                         
                            ]
                        )
                    ],
                    
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=20,
                    width=600
                ),
                bgcolor="#1A1A28",
                border_radius = ft.border_radius.all(10),
                padding=ft.padding.symmetric(horizontal=10)
            )
        )
    return lPrint




colum.controls.clear()
colum.controls.extend(list_print_buy(lg.cb.list_buy))
""" columSearchInv.controls.clear()
columSearchInv.controls.extend(lis_print_search(search)) """


def app_bar(page :ft.Page):
    

    return ft.AppBar(
        title=ft.Row(
            [
                ft.Icon(ft.Icons.LOCAL_PHARMACY),
                ft.Text("Farmacia",color="#E0E0E0",weight="bold")
            ]
        ),
        center_title=True,
        bgcolor="#252536",
        actions=[
            ft.Row(
                [
                ft.ElevatedButton(
                    "Inicio",
                    on_click=lambda _: page.go("/"),
                    color="#FFFFFF",
                    bgcolor="#4CAF50"
                    ),
                ft.ElevatedButton(
                    "Inventario",
                    on_click=lambda _: page.go("/inventario"),
                    color="#FFFFFF",
                    bgcolor="#4CAF50"
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
                width=200
    )],
        toolbar_height=70
    )

def main(page:ft.Page):
    page.title = "Farmacia"
    page.window_width = 1200 
    page.window_height = 700
    page.window_min_width = 800  
    page.window_min_height = 600
    page.bgcolor = "#1E1E2E"

    global f_ref,columSearch

    f_ref.current = ft.Text(
        value= f"{lg.cb.calc_total()} Bs.",
        size=18,
        color="#E0E0E0"
        )


    #funciones de accion
    def busqueda(e):
        global columSearch
        search = lg.search_element(e.control.value.lower())
        columSearch.controls.clear()
        columSearch.controls.extend(lis_print_search(search))
        columSearch.update()
        
    def busqueda_inv(e):
        global columSearchInv
        search = lg.search_element(e.control.value.lower())
        columSearchInv.controls.clear()
        columSearchInv.controls.extend(list_print_inv(search))
        columSearchInv.update()
        

    def pagina_inicio():
        global f_ref,colum,columSearch
        return ft.View(
            "/",
            [
                app_bar(page),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                colum,
                                ft.Container(
                                    bgcolor="#242434",
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(
                                            "Total:",
                                            color="#E0E0E0",
                                            size=25,
                                            weight="bold"
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            ft.Text(
                                                                "Total a pagar",
                                                                size=10,
                                                                color="#E0E0E0"
                                                            ),
                                                            f_ref.current
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                        spacing=20
                                                    ),
                                                    ft.ElevatedButton(
                                                        text="Realizar compra",
                                                        icon=ft.Icons.CHECK_CIRCLE,
                                                        color="#FFFFFF",
                                                        bgcolor="#4CAF50",
                                                        icon_color="#FFFFFF",
                                                        on_click=relizar_compra
                                                    )
                                                ]
                                            )
                                        ],
                                        width=page.window_width/2,
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    hint_text="Busqueda...",
                                    helper_text="No es necesario apretar (enter) busqueda automatica",
                                    on_change=busqueda,
                                    width=page.window_width/2,
                                    bgcolor="#2E2E3E",
                                    color="#E0E0E0",
                                    border_color="#38384A"
                                ),
                                columSearch
                            ]
                        )
                    ],
                    expand=True,
                    width=page.window_width,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )

    def inventario():
        return ft.View(
            "/inventario",
            [
                app_bar(page),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.ADD_OUTLINED
                                ),
                                ft.ElevatedButton(
                                    text="Guardar",
                                    on_click=lg.save_changes
                                )
                            ]
                        ),
                        ft.TextField(
                                    hint_text="Busqueda...",
                                    helper_text="No es necesario apretar (enter) busqueda automatica",
                                    on_change=busqueda_inv,
                                    width=page.window_width/2,
                                    bgcolor="#2E2E3E",
                                    color="#E0E0E0",
                                    border_color="#38384A"
                                ),
                        columSearchInv
                    ],
                    width=1200,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ]
        )

    def route_change(route):
        page.views.clear()

        if page.route=="/":
            page.views.append(pagina_inicio())
        elif page.route == "/inventario":
            page.views.append(inventario())

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(
    target=main,
    view=ft.FLET_APP,
    assets_dir="assets"
)