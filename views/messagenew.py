import flet as ft
newResourse = {
    "path":"",
    "name":"",
    "type":""
}


class AlertNewResourse(ft.AlertDialog):
    def __init__(self,pageActual):
        super().__init__()
        self.page = pageActual
        self.modal=True
        self.title=ft.Text("Crear nuevo recurso compartido")
        self.pick_files_dialog = ft.FilePicker(on_result=self.pickFilesResult)
        self.selectedFolderTF = ft.TextField(label="Ruta del recurso compartido")
        self.page.overlay.append(self.pick_files_dialog)
        self.cancelBtn = ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400)
        self.saveBtn = ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600, disabled = True)
        self.resourseNameTF = ft.TextField(label="Nombre del recurso", width=500,on_change=self.unableSaveBtn)
        self.descriptionTF = ft.TextField(label="Descripción", width=500,on_change=self.unableSaveBtn)
        self.textError = ft.Text("", color = ft.colors.RED_500)
        self.typeResourseRadioGroup = ft.RadioGroup(
                                        content=ft.Row([
                                            ft.Radio(value="0", label="Carpeta",focus_color=ft.colors.RED_500),
                                            ft.Icon(ft.icons.FOLDER),
                                            ft.Radio(value="1", label="Impresora"),
                                            ft.Icon(ft.icons.LOCAL_PRINT_SHOP),
                                            self.textError
                                        ],
                                        vertical_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    on_change = self.unableSaveBtn
                                )
        self.content=ft.Column(
            controls=[
                ft.Card(
                    content= ft.Container(
                        ft.Column(
                            controls=[
                                ft.Text("Identificacion"),
                                self.resourseNameTF,
                                self.descriptionTF
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
                                self.typeResourseRadioGroup,           
                                ft.Column(
                                    [
                                        self.selectedFolderTF,
                                        ft.ElevatedButton(
                                            "Seleccionar ubicacion",
                                            icon=ft.icons.SEARCH,
                                            on_click=lambda _: self.pick_files_dialog.get_directory_path()
                                        )    
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.END                      
                                ),
                                ft.Column(
                                    controls= [
                                        ft.Checkbox(label="Solo Lectura",on_change=self.unableSaveBtn),
                                        ft.Checkbox(label="Heredar las ACL",on_change=self.unableSaveBtn, value=True),
                                        # ft.Checkbox(label="Exponer instantaneas", disabled=True,on_change=self.unableSaveBtn),
                                        # ft.Checkbox(label="Utilizar caracteristicas de BtrFS",on_change=self.unableSaveBtn)
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
        self.actions = [self.cancelBtn,self.saveBtn]
        self.actions_alignment="end"

    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        if self.resourseNameTF.value == "":
            self.__textFieldEmpty__(self.resourseNameTF)
        elif self.selectedFolderTF.value == "":
            self.__textFieldEmpty__(self.selectedFolderTF)   
        elif self.typeResourseRadioGroup.value == None:
            self.textError.value = "Debe elegir una opcion"
            self.page.update()
        else:
            self.open = False
            self.page.update()

    def __textFieldEmpty__(self,textfield):
        textfield.focused_border_color = ft.colors.RED_500
        textfield.error_text = "Este campo no debe estar vacio"
        textfield.focus()
        self.page.update()

    def unableSaveBtn(self,e):
        self.saveBtn.disabled = False
        self.resourseNameTF.error_text = None
        self.resourseNameTF.focused_border_color = None
        self.selectedFolderTF.error_text = None
        self.selectedFolderTF.focused_border_color = None
        self.textError.value = ""
        self.page.update()      

    def pickFilesResult(self,e: ft.FilePickerResultEvent):
        if e.path:
            self.selectedFolderTF.value = e.path
            self.unableSaveBtn(e)
        else:  
            self.selectedFolderTF.error_text = "Debe seleccionar una carpeta"
        self.selectedFolderTF.update() 







class AlertEditResourse(ft.AlertDialog):
    def __init__(self,pageActual):
        super().__init__()
        self.page = pageActual
        #self.elementToedit = elementToEdit
        self.modal=True
        self.title=ft.Text("Editar recurso compartido")
        self.pick_files_dialog = ft.FilePicker(on_result=self.pickFilesResult)
        self.selectedFolderTF = ft.TextField(label="Ruta del recurso compartido")
        self.page.overlay.append(self.pick_files_dialog)
        self.cancelBtn = ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400)
        self.saveBtn = ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600, disabled=True)
        self.editMaskTable1 = EditMask()
        self.editMaskTable2 = EditMask()
        self.maskInputContainer = ft.Row(
                                    controls=[
                                        ft.TextField(label="Crear Mascara", width=500, on_change=self.unableSaveBtn, disabled=True),
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            icon_color = ft.colors.BLUE_500,
                                            tooltip = "Editar propiedad",
                                            on_click = self.showMaskTable
                                        )
                                ])
        
        self.content=ft.Column(
            controls=[
                ft.Card(
                    content= ft.Container(
                        ft.Column(
                            controls=[
                                ft.Text("Recurso a compartir:"),
                                ft.Column(
                                    [
                                        self.selectedFolderTF,
                                        ft.ElevatedButton(
                                            "Seleccionar ubicacion",
                                            icon=ft.icons.SEARCH,
                                            on_click=lambda _: self.pick_files_dialog.get_directory_path()
                                        )    
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.END                      
                                ),
                                self.maskInputContainer,
                                self.editMaskTable1,
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Mascara de carpeta", width=500, on_change=self.unableSaveBtn, disabled=True),
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            icon_color = ft.colors.BLUE_500,
                                            tooltip = "Editar propiedad",
                                            on_click = self.showMaskTable
                                        )
                                ]),
                                
                                # ft.Row(
                                #     controls=[
                                #         ft.TextField(label="Descripcion", width=500, on_change=self.unableSaveBtn, disabled=True),
                                #         ft.IconButton(
                                #             icon=ft.icons.EDIT,
                                #             icon_color = ft.colors.BLUE_500,
                                #             tooltip = "Editar propiedad"
                                #         )
                                # ]),
                                # ft.Row(
                                #     controls=[
                                #         ft.TextField(label="Solo lectura", width=500, on_change=self.unableSaveBtn, disabled=True),
                                #         ft.IconButton(
                                #             icon=ft.icons.EDIT,
                                #             icon_color = ft.colors.BLUE_500,
                                #             tooltip = "Editar propiedad"
                                #         )
                                # ]),
                                # ft.Row(
                                #     controls=[
                                #         ft.TextField(label="Heredar ACLs", width=500, on_change=self.unableSaveBtn, disabled=True),
                                #         ft.IconButton(
                                #             icon=ft.icons.EDIT,
                                #             icon_color = ft.colors.BLUE_500,
                                #             tooltip = "Editar propiedad"
                                #         )
                                # ]),
                            ],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER   
                        ),
                        padding=10
                    ),
                    width = 800,
                ),
            ],

        )
        self.actions=[self.cancelBtn,self.saveBtn]
        self.actions_alignment="end"
        
    def showMaskTable(self,e):
        # editMaskDialog = AlertEditMask(self.page,"Crear mascara")
        # self.page.dialog = editMaskDialog
        # editMaskDialog.open = True
        self.maskInputContainer.visible = False
        self.editMaskTable1.visible = True
        self.page.update()
                                       
    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        self.open = False
        self.page.update()  

    def unableSaveBtn(self,e):
        self.saveBtn.disabled = False
        self.page.update()  

    def pickFilesResult(self,e: ft.FilePickerResultEvent):
        if e.path:
            self.selectedFolderTF.value = e.path
            self.unableSaveBtn(e)
        else:  
            self.selectedFolderTF.error_text = "Debe seleccionar una carpeta"
        self.selectedFolderTF.update() 




class EditMask(ft.Row):
    def __init__(self):
        super().__init__()
        #self.elementToedit = elementToEdit
        self.modal=True
        self.title=ft.Text()
        self.cancelBtn = ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400)
        self.saveBtn = ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600, disabled=True)
        self.alignment=ft.MainAxisAlignment.CENTER, 
        self.visible = False
        self.controls = [ft.DataTable(                                    
                                                border=ft.border.all(2, "red"),
                                                border_radius=10,
                                                vertical_lines=ft.border.BorderSide(3, "blue"),
                                                horizontal_lines=ft.border.BorderSide(1, "green"),
                                                sort_column_index=2,
                                                sort_ascending=True,
                                                heading_row_color=ft.colors.BLACK12,
                                                #show_checkbox_column=True,
                                                data_row_color={"hovered": "0x30FF0000"},
                                                divider_thickness=0,
                                                columns=[
                                                    ft.DataColumn(ft.Text("")),
                                                    ft.DataColumn(ft.Text("Lectura (R)")),
                                                    ft.DataColumn(ft.Text("Escritura (W)")),
                                                    ft.DataColumn(ft.Text("Ejecucion (X)"))
                                                ],
                                                rows=[
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(ft.Text("Usuario")),
                                                            ft.DataCell(ft.Checkbox()),
                                                            ft.DataCell(ft.Checkbox()),
                                                            ft.DataCell(ft.Checkbox())
                                                        ]
                                                    ),
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(ft.Text("Grupo")),
                                                            ft.DataCell(ft.Checkbox()),
                                                            ft.DataCell(ft.Checkbox()),
                                                            ft.DataCell(ft.Checkbox())
                                                        ]
                                                    ),
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(ft.Text("Otros")),
                                                            ft.DataCell(ft.Checkbox()),
                                                            ft.DataCell(ft.Checkbox()),
                                                            ft.DataCell(ft.Checkbox())
                                                        ]
                                                    )
                                                ]
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.SAVE,
                                                icon_color = ft.colors.BLUE_500,
                                                tooltip = "Guardar propiedad"
                                            )
                                        ]

    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        self.open = False
        self.page.update()         

