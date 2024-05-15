import flet as ft
from views.view1 import Tab1
from views.view2 import Tab2
from views.view3 import Tab3
# from views.view4 import tab4
# from views.view5 import tab5
# from views.view6 import SharedTab

def main(page: ft.Page):
    page.title = "Panel de Control SAMBA SERVER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = False

    tabsToRender = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[Tab1(),Tab2(),Tab3()],
        expand=1,
    )
    page.add(
        tabsToRender
    )

    page.add(ft.Row(
                    controls=[
                        ft.ElevatedButton("Cancelar",bgcolor=ft.colors.RED_800,disabled=True,icon=ft.icons.CANCEL),
                        ft.ElevatedButton("Guardar cambios",bgcolor=ft.colors.GREEN_800,disabled=True,icon=ft.icons.SAVE)
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment = ft.CrossAxisAlignment.END
                )
    )


ft.app(target=main)