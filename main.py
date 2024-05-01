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

    def items(count):
        result = []
        itemsList = []
        for i in range(1, count + 1):
            items.append(
                ft.Checkbox()
            )

        ft.Row(
                controls=itemsList,
                alignment=ft.MainAxisAlignment.CENTER,
              )  
        return items    

    tabsToRender = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Arranque",
                icon=ft.icons.RESTART_ALT,
                content=ft.Column(
                            controls=[ft.Text("Configuracion de Servicio"),
                                      ft.Row(controls = [ft.Text("Estado de servicio: "),ft.Text("Activo",color=ft.colors.LIGHT_GREEN_ACCENT_400)]),
                                      ft.Text("Despues de escribir sobre la configuracion:"),
                                      ft.Dropdown(
                                            width=200,
                                            options=[
                                                ft.dropdown.Option("Iniciar"),
                                                ft.dropdown.Option("Mantener el estado actual")
                                            ],
                                            label="Accion",
                                            hint_text="Elige una opcion"),
                                      ft.Text("Despues de Reiniciar el equipo:"),
                                      ft.Dropdown(
                                            width=200,
                                            options=[
                                                ft.dropdown.Option("No iniciar"),
                                                ft.dropdown.Option("Iniciar durante el arranque"),
                                            ],
                                            label="Accion",
                                            hint_text="Elige una opcion"),
                                      
                                      ft.Text("Configuracion de firewall para FIREWALLD:"),
                                      ft.Row(controls=[ft.Checkbox(label="Puerto abierto en el cortafuegos"),ft.FilledButton(text="Detalles del cortafuegos...")],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                      ft.Text("El firewall esta desabilitado")
                            ], 
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        )
            ),
            ft.Tab(
                text ="Compartidos",
                icon = ft.icons.FOLDER_SHARED,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls = [ft.Text("Recursos compartidos disponibles:"),
                                       ft.Dropdown(
                                                        width=100,
                                                        options=[
                                                            ft.dropdown.Option("Por nombre"),
                                                            ft.dropdown.Option("Por fecha"),
                                                        ],
                                                        label="Filtrar",
                                        )],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,            
                        ),
                        ft.Row(
                            controls = [ft.DataTable(
                                        columns=[
                                            ft.DataColumn(ft.Text("Estado")),
                                            ft.DataColumn(ft.Text("Solo Lectura")),
                                            ft.DataColumn(ft.Text("Nombre")),
                                            ft.DataColumn(ft.Text("Ruta de Recurso")),
                                            ft.DataColumn(ft.Text("Acceso de invitado")),
                                            ft.DataColumn(ft.Text("Comentario")),
                                        ],
                                        rows=[
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                                    ft.DataCell(ft.Text("Si")),
                                                    ft.DataCell(ft.Text("impresora")),
                                                    ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                                    ft.DataCell(ft.Text("No")),
                                                    ft.DataCell(ft.Text("Printer Drivers"))
                                                ],
                                            ),
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                                    ft.DataCell(ft.Text("Si")),
                                                    ft.DataCell(ft.Text("impresora")),
                                                    ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                                    ft.DataCell(ft.Text("No")),
                                                    ft.DataCell(ft.Text("Printer Drivers"))
                                                ],
                                            ),
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                                    ft.DataCell(ft.Text("Si")),
                                                    ft.DataCell(ft.Text("impresora")),
                                                    ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                                    ft.DataCell(ft.Text("No")),
                                                    ft.DataCell(ft.Text("Printer Drivers"))
                                                ],
                                            ),
                                        ]
                                    
                                    )
                                ],
                            alignment=ft.MainAxisAlignment.CENTER, 
                        ),    
                        ft.Row(
                            controls = [
                                ft.Row(
                                    controls = [
                                        ft.OutlinedButton(text="Añadir..."),
                                        ft.OutlinedButton(text="Editar..."),
                                        ft.OutlinedButton(text="Suprimir")
                                    ]
                                ),
                                ft.Row(
                                    controls = [
                                        ft.OutlinedButton(text="Renombrar..."),
                                        ft.OutlinedButton(text="Acceso de invitado"),
                                        ft.OutlinedButton(text="Cambiar estado")
                                    ]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN 
                        ),
                        ft.Row(
                            controls=[
                              ft.Text("Recursos compartidos por los usuarios")      
                            ]
                        ),  
                        ft.Column(
                            controls=[
                              ft.Checkbox(label="Permitir a los usuarios compartir sus directorios"),
                              ft.Checkbox(label="Permitir acceso de invitado")      
                            ]
                        ),  
                        ft.Column(
                            controls=[
                               ft.TextField(label="Grupo permitido"),
                               ft.Text("Numero maximo de recursos compartidos:"),
                               ft.Slider(min=0, max=10, divisions=1, label="{value}")
                            ]
                        ),                 
                     ]
                )
            ),

            ft.Tab(
                text="Identidad",
                icon=ft.icons.PERM_IDENTITY,
                content=ft.Text("This is Tab 3",color=ft.colors.BLUE_50)
            ),
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