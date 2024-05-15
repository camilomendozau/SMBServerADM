import flet as ft

tab4 = ft.Tab(
                text="Dominios Confiables",
                icon=ft.icons.DOMAIN_VERIFICATION_SHARP,
                content= ft.Column(
                    controls = [
                        ft.Text("Dominios de confianza"),
                        ft.TextField(
                            label="Lista de Dominios",
                            multiline=True,
                            max_lines = 10,
                            min_lines = 10
                        ),
                        ft.Row(
                            controls = [
                                        ft.OutlinedButton(text="Añadir..."),
                                        ft.OutlinedButton(text="Suprimir")
                            ] 
                        )
                    ]
                )
        )