import flet as ft
from views.view1 import tab1
from views.view2 import tab2
from views.view3 import tab3


def main(page: ft.Page):
    page.title = "Panel de Control SAMBA SERVER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()


    tabsToRender = ft.Tabs(
        selected_index=2,
        animation_duration=300,
        tabs=[tab1,tab2,tab3,
            ft.Tab(
                text="Dominios Confiables",
                icon=ft.icons.DOMAIN_VERIFICATION_SHARP,
                content=ft.Text("This is Tab 3",color=ft.colors.BLUE_50)
            ),
            ft.Tab(
                text="Configuraciones LDAP",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3",color=ft.colors.BLUE_50)
            ),
            
        ],
        expand=1,
    )
    page.add(tabsToRender)
    page.add(ft.Row(
                    controls=[
                        ft.ElevatedButton("Cancelar",bgcolor=ft.colors.RED_800,disabled=False,icon=ft.icons.CANCEL),
                        ft.ElevatedButton("Guardar cambios",bgcolor=ft.colors.GREEN_800,disabled=False,icon=ft.icons.SAVE)
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment = ft.CrossAxisAlignment.END
                )
            )

ft.app(target=main)