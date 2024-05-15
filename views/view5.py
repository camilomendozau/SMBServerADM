import flet as ft

tab5 = ft.Tab(
                text="Configuracion LDAP",
                icon=ft.icons.SETTINGS_SUGGEST,    
                content= ft.Column(
                  controls = [ft.Row(
                            controls = 
                            [ft.Column( controls = 
                               [ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Motor de base de datos de contraseñas"),
                                            ft.Checkbox(label = "Usar motor de contraseñas LDAP"),
                                            ft.TextField(label = "URL de servidor LDAP"),
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    width=550,
                                    height=200,
                                    margin=2,
                                    padding=15,
                                ),
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Motor de Idmap"),
                                            ft.Checkbox(label="Usar motor de Idmap de LDAP"),
                                            ft.TextField(label="URL de servidor LDAP"),
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    width=550,
                                    height=200,
                                    margin=2,
                                    padding=15,
                                ),
                            )
                            ]),
                            ft.Card(
                                content=ft.Container( 
                                    ft.Column(
                                        controls = [
                                            ft.Text("Autenticacion"),
                                            ft.TextField(label="DN de administracion"),
                                            ft.TextField(label="Contraseña de administracion"),
                                            ft.TextField(label="Contraseña de administracion (de nuevo)")
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    ),
                                    width=550,
                                    height=420,
                                    margin=2,
                                    padding=15,
                                )
                            )
                            ],
                            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment = ft.CrossAxisAlignment.START
                        ),
                        ft.Container(
                            ft.Column(
                                controls = [
                                    ft.TextField(label="DN de base de busqueda"),
                                    ft.Row(
                                        controls = [
                                           ft.FilledTonalButton("Probar conexion"), 
                                           ft.Dropdown(
                                                label="Configuracion avanzada...",
                                                options=[
                                                    ft.dropdown.Option("Configuracion avanzada de LDAP"),
                                                    ft.dropdown.Option("Valores predeterminados")
                                                ],                        
                                                autofocus=True,                         
                                            ) 
                                        ]
                                    )
                                ],
                                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            ),
                            width=500,
                            height=300,
                            margin=10,
                            padding=40,
                        )
                   ]
                )
        )