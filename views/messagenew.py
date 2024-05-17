import flet as ft

class AlertNewResourse(ft.AlertDialog):
    def __init__(self,pageActual):
        super().__init__()
        self.page = pageActual
        self.modal=True
        self.title=ft.Text("Crear nuevo recurso compartido")
        self.pick_files_dialog = ft.FilePicker(on_result=self.pickFilesResult)
        self.selected_files = ft.TextField(label="Ruta del recurso compartido")
        self.page.overlay.append(self.pick_files_dialog)
        self.content=ft.Column(
            controls=[
                ft.Card(
                    content= ft.Container(
                        ft.Column(
                            controls=[
                                ft.Text("Identificacion"),
                                ft.TextField(label="Nombre del recurso", width=500),
                                ft.TextField(label="Descripción", width=500)
                            ],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER   
                        ),
                        padding=10
                    ),
                    width = 800,
                ),
                ft.Card(
                    content= ft.Container(
                        ft.Column(
                            controls=[
                                ft.Text("Tipo de recurso compartido"),
                                ft.RadioGroup(
                                    content=ft.Row([
                                                        ft.Radio(value="0", label="Carpeta"),
                                                        ft.Radio(value="1", label="Impresora"),
                                    ],
                                    vertical_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                ),             
                                ft.Column(
                                    [
                                        self.selected_files,
                                        ft.ElevatedButton(
                                            "Seleccionar ubicacion",
                                            icon=ft.icons.SEARCH,
                                            on_click=lambda _: self.pick_files_dialog.get_directory_path(initial_directory="C:")
                                        )    
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.END                      
                                ),
                                ft.Column(
                                    controls= [
                                        ft.Checkbox(label="Solo Lectura"),
                                        ft.Checkbox(label="Heredar las ACL"),
                                        ft.Checkbox(label="Exponer instantaneas", disabled=True),
                                        ft.Checkbox(label="Utilizar caracteristicas de BtrFS")
                                    ]
                                )
                            ],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=10
                    ),
                    width = 800,
                )
  
            ],

        )
        self.actions=[ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400),
                      ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600)
                      ]
        self.actions_alignment="end"

    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        self.open = False
        self.page.update()   

    def pickFilesResult(self,e: ft.FilePickerResultEvent):
        if e.path:
            self.selected_files.value = e.path
        else:
            self.selected_files.value = "No se seleccionó ningún archivo"            
        self.selected_files.update() 



