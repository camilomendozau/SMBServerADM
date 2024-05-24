import flet as ft
from views.view1 import Tab1
from views.view2 import Tab2
from views.view3 import Tab3
from views.view4 import Tab4
from config import config

# print(config)

def main(page: ft.Page):
    page.title = "Panel de Control SAMBA SERVER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = False
    page.window_resizable = False
    page.window_width = 1300
    page.window_height = 850

    tabsToRender = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[Tab1(),Tab2(page),Tab3(page),Tab4(page)],
        expand=1,
    )
    page.add(tabsToRender)
    page.add(ft.Row(
                    controls=[
                        ft.ElevatedButton("Cancelar",bgcolor=ft.colors.RED_300,icon=ft.icons.CANCEL),
                        ft.ElevatedButton("Guardar cambios",bgcolor=ft.colors.GREEN_300,icon=ft.icons.SAVE)
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment = ft.CrossAxisAlignment.END
                )
    )


ft.app(target=main)