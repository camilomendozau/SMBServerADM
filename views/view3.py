import flet as ft

class Tab3(ft.Tab):
    def __init__(self):
        super().__init__()
        self.text="Identidad"
        self.icon=ft.icons.PERM_IDENTITY   
        self.content= ft.Column(
                  controls = [    
                        ft.Row(
                            controls = 
                            [ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Configuracion basica"),
                                                    ft.TextField(label="Nombre de grupo de trabajo o dominio",value="WORKGROUP"),
                                                    ft.Dropdown(
                                                        label="Controlador de dominio",
                                                        options=[
                                                            ft.dropdown.Option("No es un controlador de dominio"),
                                                            ft.dropdown.Option("Primario (PDC)"),
                                                            ft.dropdown.Option("Copia de seguridad (BDC)"),
                                                        ],
                                                        autofocus=True,
                                                    )
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    width=550,
                                    height=300,
                                    margin=2,
                                    padding=15,
                                ),
                            ),
                            ft.Card(
                                content=ft.Container( 
                                    ft.Column(
                                        controls = [
                                            ft.Text("WINS"),
                                            ft.RadioGroup(content=ft.Column([
                                                    ft.Radio(value="0", label="Compatibilidad con servidor WINS"),
                                                    ft.Radio(value="1", label="Servidor WINS remoto"),
                                                ])
                                            ),
                                            ft.TextField(label="Nombre"),
                                            ft.Checkbox(label="Obtener servidor WINS mediante DHCP"),
                                            ft.Checkbox(label="Utilizar WINS para resolucion de nombres de host")
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    ),
                                    width=550,
                                    height=300,
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
                                ft.TextField(label="Nombre de host de NetBIOS"),
                                ft.Dropdown(
                                    label="Configuracion avanzada",
                                    options=[
                                                ft.dropdown.Option("Configuracion global modo experto"),
                                                ft.dropdown.Option("Fuentes de autenticacion de usuario")
                                            ],                        
                                    autofocus=True,                         
                                )],
                                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            ),
                            width=500,
                            height=300,
                            margin=10,
                            padding=40,
                        )
                   ]
                )