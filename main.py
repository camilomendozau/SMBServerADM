import flet as ft


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

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Permisos",
                content=ft.Row(
                                [
                                    ft.Checkbox(label="Read"),
                                    ft.Checkbox(label="Write"),
                                    ft.Checkbox(label="Execute")
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Configuraciones",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3",color=ft.colors.BLUE_50)
            ),
        ],
        expand=1,
    )
    page.add(t)
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
