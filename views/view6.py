import flet as ft

class Tab1(ft.Tab):
    def __init__(self):
        super().__init__()        
        self.stateServiceText = ft.Text("Activo",color=ft.colors.LIGHT_GREEN_ACCENT_400)
        self.initDropDown = ft.Dropdown( width=300,
                            options=[
                                        ft.dropdown.Option("No iniciar"),
                                        ft.dropdown.Option("Iniciar durante el arranque"),
                                    ],
                            label="Accion",
                            hint_text="Elige una opcion")
        self.firewallCheckbox = ft.Checkbox(label="Puerto abierto en el cortafuegos",on_change = self.activateFirewallDetailsBtn)
        self.firewallDetailsBtn = ft.OutlinedButton(text="Detalles del cortafuegos...", disabled = True)

        self.text="Inicio"
        self.icon=ft.icons.RESTART_ALT
        self.content = ft.Column(
                  controls = [ft.Row(
                            controls = 
                            [ft.Column( controls = 
                               [ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Configuracion de Servicio"),
                                            ft.Row(
                                                controls = [
                                                    ft.Text("Estado de servicio: "),
                                                    self.stateServiceText
                                                ]),
                                            ft.Text("Despues de escribir sobre la configuracion:"),
                                            ft.Dropdown(
                                                    width=300,
                                                    options=[
                                                        ft.dropdown.Option("Iniciar"),
                                                        ft.dropdown.Option("Mantener el estado actual")
                                                    ],
                                                    label="Accion",
                                                    hint_text="Elige una opcion"
                                            ),
                                            ft.Text("Despues de Reiniciar el equipo:"),
                                            self.initDropDown
                                                ],
                                                horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                            ),
                                            width = 900,
                                            margin=2,
                                            padding=15,
                                ),
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                           ft.Text("Configuracion de firewall para FIREWALLD:"),
                                           ft.Row(controls=[
                                                self.firewallCheckbox,
                                                self.firewallDetailsBtn
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                           ft.Text("El firewall esta desabilitado") 
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    width = 900,
                                    margin=2,
                                    padding=15,
                                ),
                            )
                            ]),
                            ],
                            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment = ft.CrossAxisAlignment.START
                        )
                   ]
               )

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

    def activateFirewallDetailsBtn(self,e):
        if self.firewallCheckbox.value:
            self.firewallDetailsBtn.disabled = False
        else:
            self.firewallDetailsBtn.disabled = True    
        self.update()
