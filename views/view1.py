import flet as ft

tab1 =  ft.Tab(
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
        )