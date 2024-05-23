import flet as ft
from views.messagenew import AlertNewResourse,AlertEditResourse
from config import config

class Tab2(ft.Tab):
    def __init__(self,pageIn):
        super().__init__()
        self.text ="Compartidos"
        self.icon = ft.icons.FOLDER_SHARED
        self.page = pageIn
        self.addBtn = ft.OutlinedButton(text="Añadir...", icon = ft.icons.ADD, on_click=self.openDialogNewResourse)
        self.editBtn = ft.OutlinedButton(text="Editar...", disabled=True, icon = ft.icons.EDIT_ROUNDED, on_click=self.openDialogEditResourse)
        self.deleteBtn = ft.OutlinedButton(text="Suprimir", disabled=True, icon = ft.icons.DELETE)
        self.unableSharedDirectoriesCheckbox = ft.Checkbox(label="Permitir a los usuarios compartir sus directorios",value=True, on_change=self.unableOptionsShareDirectories)
        self.unableInvitedAccessCheckbox = ft.Checkbox(label="Permitir acceso de invitado")
        self.groupNameTextField = ft.TextField(label="Grupo permitido",width=400,value="users")
        self.sliderValue = ft.Text("0")
        self.currentRowToEdit = ""
        self.shareTable = ft.Row(
                            controls = [ft.DataTable(                                    
                                        border=ft.border.all(2, "red"),
                                        border_radius=10,
                                        vertical_lines=ft.border.BorderSide(3, "blue"),
                                        horizontal_lines=ft.border.BorderSide(1, "green"),
                                        sort_column_index=2,
                                        sort_ascending=True,
                                        heading_row_color=ft.colors.BLACK12,
                                        show_checkbox_column=True,
                                        data_row_color={"hovered": "0x30FF0000"},
                                        divider_thickness=0,
                                        columns=[
                                            ft.DataColumn(ft.Text("Estado"),tooltip="Estado del recurso"),
                                            ft.DataColumn(ft.Text("Solo Lectura")),
                                            ft.DataColumn(ft.Text("Nombre"),on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
                                            ft.DataColumn(ft.Text("Ruta de Recurso")),
                                            #ft.DataColumn(ft.Text("Acceso de invitado")),
                                            ft.DataColumn(ft.Text("Comentario")),
                                        ],
                                        rows=[
                                            # ft.DataRow(
                                            #     cells=[
                                            #         ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                            #         ft.DataCell(ft.Text("Si")),
                                            #         ft.DataCell(ft.Text("impresora")),
                                            #         ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                            #         ft.DataCell(ft.Text("No")),
                                            #         ft.DataCell(ft.Text("Printer Drivers"))
                                            #     ],
                                            #     on_select_changed= self.unableBtnsControls
                                            # ),
                                            # ft.DataRow(
                                            #     cells=[
                                            #         ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                            #         ft.DataCell(ft.Text("Si")),
                                            #         ft.DataCell(ft.Text("Fotocopiadora")),
                                            #         ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                            #         ft.DataCell(ft.Text("No")),
                                            #         ft.DataCell(ft.Text("Printer Drivers"))
                                            #     ],
                                            #     on_select_changed= self.unableBtnsControls
                                            # ),
                                            # ft.DataRow(
                                            #     cells=[
                                            #         ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                            #         ft.DataCell(ft.Text("Si")),
                                            #         ft.DataCell(ft.Text("Compartidos")),
                                            #         ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                            #         ft.DataCell(ft.Text("No")),
                                            #         ft.DataCell(ft.Text("Printer Drivers")),
                                            #     ],
                                            #     on_select_changed= self.unableBtnsControls
                                            # ),
                                        ]

                                    )
                                ],
                            alignment=ft.MainAxisAlignment.CENTER, 
                        )
        self.__generateShareTableData__()
        self.maxNumberShareResourcesSlider = ft.CupertinoSlider(
                                                    divisions=5,
                                                    max=100,
                                                    active_color=ft.colors.PURPLE,
                                                    thumb_color=ft.colors.PURPLE,
                                                    on_change=self.handle_change,
                                                    width=500,
                                                    value=30
                                                )
        
        self.rowsSelected = 0
        self.content=ft.Column(
                    controls=[
                        ft.Row(
                            controls = [ft.Text("Recursos compartidos disponibles:"),
                                    #    ft.Dropdown(
                                    #                     width=300,
                                    #                     options=[
                                    #                         ft.dropdown.Option("Por nombre"),
                                    #                         ft.dropdown.Option("Por fecha"),
                                    #                     ],
                                    #                     label="Filtrar",
                                    #     )
                                    ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND           
                        ),
                        self.shareTable,
                        ft.Row(
                            controls = [self.addBtn,self.editBtn,self.deleteBtn],
                            alignment=ft.MainAxisAlignment.START
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls= [
                                        ft.Text("Recursos compartidos por los usuarios"),
                                        self.unableSharedDirectoriesCheckbox,
                                        self.unableInvitedAccessCheckbox,
                                        ft.Row(
                                            [
                                                self.groupNameTextField,
                                                ft.Column([
                                                    self.sliderValue,
                                                    self.maxNumberShareResourcesSlider
                                                ])
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        )
                                    ],
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER               
                                ),
                                padding=20
                            )
                        ) 
                    ], )  
        
    def __generateShareTableData__(self):
        namesBaseList = ["homes","users","printers","groups","print$","profiles"]
        for i in range(len(namesBaseList)):
            rowToInner = ft.DataRow()
            rowToInner.cells.append(ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)))
            try:  
                rowToInner.cells.append(ft.DataCell(ft.Text(config[namesBaseList[i]]['read only'])))
            except:
                rowToInner.cells.append(ft.DataCell(ft.Text("No")))    
            try:  
                rowToInner.cells.append(ft.DataCell(ft.Text(namesBaseList[i])))
            except:
                rowToInner.cells.append(ft.DataCell(ft.Text("")))    
            try:  
                rowToInner.cells.append(ft.DataCell(ft.Text(config[namesBaseList[i]]['path'])))
            except:
                rowToInner.cells.append(ft.DataCell(ft.Text("")))    
            try:  
                rowToInner.cells.append(ft.DataCell(ft.Text(config[namesBaseList[i]]['comment'])))
            except:
                rowToInner.cells.append(ft.DataCell(ft.Text("")))    
            rowToInner.on_select_changed = self.unableBtnsControls
            self.shareTable.controls[0].rows.append(rowToInner)
            
                                            
    def openDialogNewResourse(self,e):
        newAlert = AlertNewResourse(self.page)
        self.page.dialog = newAlert
        newAlert.open = True
        self.page.update()

    def openDialogEditResourse(self,e):
        editAlert = AlertEditResourse(self.page,self.currentRowToEdit[2].content.value)
        self.page.dialog = editAlert
        editAlert.open = True
        self.page.update()

    def unableOptionsShareDirectories(self,e):
        if self.unableSharedDirectoriesCheckbox.value:
            self.unableInvitedAccessCheckbox.disabled = False
            self.groupNameTextField.disabled = False
            self.maxNumberShareResourcesSlider.disabled= False
            self.sliderValue.disabled = False
        else:
            self.unableInvitedAccessCheckbox.disabled = True
            self.groupNameTextField.disabled = True
            self.maxNumberShareResourcesSlider.disabled = True
            self.sliderValue.disabled = True
        self.update()    

    def handle_change(self,e):
        self.sliderValue.value = str(e.control.value)
        self.update()

    def unableBtnsControls(self,e):
        if not e.control.selected:
            if self.rowsSelected == 0:
                self.rowsSelected = self.rowsSelected + 1
                self.currentRowToEdit = e.control.cells
                e.control.selected = True
                self.addBtn.disabled = True                    
                self.editBtn.disabled = False
                self.deleteBtn.disabled = False
                self.update()
            elif self.rowsSelected == 1:  
                self.rowsSelected = self.rowsSelected + 1
                #print(e.control.cells[2].content.value,self.rowsSelected, sep='|')         
                e.control.selected = True  
                self.addBtn.disabled = True                    
                self.editBtn.disabled = True
                self.deleteBtn.disabled = False
                self.update()      
            elif self.rowsSelected > 1:
                self.rowsSelected = self.rowsSelected + 1
                #print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = True       
                self.addBtn.disabled = True
                self.editBtn.disabled = True
                self.deleteBtn.disabled = False
                self.update()
        elif e.control.selected:
            if self.rowsSelected == 0:
                #print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = True
                self.addBtn.disabled = False                    
                self.editBtn.disabled = True
                self.deleteBtn.disabled = True
                self.update()
            if self.rowsSelected == 1:
                self.rowsSelected = self.rowsSelected - 1
                #print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = False 
                self.addBtn.disabled = False
                self.editBtn.disabled = True
                self.deleteBtn.disabled = True    
                self.update()
            elif self.rowsSelected > 1:
                self.rowsSelected = self.rowsSelected - 1
                #print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = False
                self.addBtn.disabled = True
                self.editBtn.disabled = False
                self.deleteBtn.disabled = False
                self.update()

            
            

        