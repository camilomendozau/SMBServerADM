import flet as ft

tab2 = ft.Tab(
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
            )