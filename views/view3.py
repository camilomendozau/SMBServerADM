import flet as ft
from config import config

class Tab3(ft.Tab):
    def __init__(self,pageIn):
        super().__init__()
        self.text="Identidad"
        self.icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED 
        self.page = pageIn
        self.winsRadioGroup = ft.RadioGroup(content=ft.Column([
                                                    ft.Radio(value="0", label="Compatibilidad con servidor WINS"),
                                                    ft.Radio(value="1", label="Servidor WINS remoto"),
                                                ]),
                                            on_change=self.onChangeWinsOptions    
                                        )
        self.nameWinsServer = ft.TextField(label="Nombre",value="",disabled=True)
        if config['global']['wins support'] == "Yes":
            self.winsRadioGroup.value = "0"
        else:
            self.nameWinsServer.value = config['global']['wins server']
            self.winsRadioGroup.value = "1"
            self.nameWinsServer.disabled = False
        self.page.update()
        self.content= ft.Column(
                  controls = [    
                        ft.Row(
                            controls = 
                            [ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Configuracion basica"),
                                                    ft.TextField(label="Nombre de grupo de trabajo o dominio",value=config['global']['workgroup']),
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
                                            self.winsRadioGroup,
                                            self.nameWinsServer,
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
    
    def onChangeWinsOptions(self,e):
        if self.winsRadioGroup.value == '1':
            self.nameWinsServer.disabled = False 
        else:
            self.nameWinsServer.disabled = True    
        self.page.update()    