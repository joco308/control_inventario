import flet as ft
import logic as lg

colum = ft.Column(controls=[ft.Text("Carrito de compra")])

#logic
def update_column(n):
    lg.delate_car_buy(n[0].iloc[0])
    global colum
    colum.controls.clear()
    colum.controls.extend(list_print_buy(lg.cb.list_buy))
    colum.update()
    

#elementos que se actualizan
f = ft.Text("cambio: ")

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
    print(listPrint)
    return listPrint

colum.controls.clear()
colum.controls.extend(list_print_buy(lg.cb.list_buy))


f = ft.Text("cambio: ")

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




    #funciones de accion
    def busqueda(e):
        global f
        f.value = f"cambio: {e.control.value}"
        print(f"cambio: {e.control.value}")
        f.update()




    def pagina_inicio():
        global colum
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
                                                            ft.Text(
                                                                f"{lg.cb.calc_total()} Bs.",
                                                            size=18,
                                                            color="#E0E0E0"
                                                            )
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
                                                        icon_color="#FFFFFF"
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
                                    width=page.window_width/2
                                ),
                                f
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
                ft.Text("inventario")
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