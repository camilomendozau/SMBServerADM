import flet as ft
from views.messagenew import AlertNewResourse,AlertEditResourse,AlertMessage
from config import config,optionsEnglishSpanish

class Tab2(ft.Tab):
    def __init__(self,pageIn):
        super().__init__()
        self.text ="Compartidos"
        self.icon = ft.icons.FOLDER_SHARED
        self.page = pageIn
        self.addBtn = ft.OutlinedButton(text="Añadir...", icon = ft.icons.ADD, on_click=self.openDialogNewResourse)
        self.editBtn = ft.OutlinedButton(text="Editar...", disabled=True, icon = ft.icons.EDIT_ROUNDED, on_click=self.openDialogEditResourse)
        self.deleteBtn = ft.OutlinedButton(text="Suprimir", disabled=True, icon = ft.icons.DELETE, on_click=self.deleteSelectedItem)
        self.guestAccessBtn = ft.OutlinedButton(text="Acceso de Invitado", disabled=True, icon = ft.icons.IOS_SHARE, on_click=self.enableGuestAccess)
        self.toggleStatusBtn = ft.OutlinedButton(text="Cambiar estado", disabled=True, icon = ft.icons.POWER_SETTINGS_NEW, on_click=self.enableResourse)
        self.loadProperties()
        # self.sliderValue = ft.Text("0")
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
                                            ft.DataColumn(ft.Text("Acceso de invitado")),
                                            ft.DataColumn(ft.Text("Comentario")),
                                        ],
                                        rows=[]
                                    )
                                ],
                            alignment=ft.MainAxisAlignment.CENTER, 
                        )
        self.__generateShareTableData__()
        self.rowsSelected = 0
        self.content=ft.Column(
                    controls=[
                        ft.Row(
                            controls = [ft.Text("Recursos compartidos disponibles:")],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND           
                        ),
                        self.shareTable,
                        ft.Row(
                            controls = [
                                ft.Row(
                                    [
                                        self.addBtn,
                                        self.editBtn,
                                        self.deleteBtn
                                    ]
                                ),
                                ft.Row(
                                    [
                                        self.guestAccessBtn,
                                        self.toggleStatusBtn
                                    ]
                                ) 
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls= [
                                        ft.Text("Recursos compartidos por los usuarios"),
                                        self.enableSharedDirectoriesCheckbox,
                                        self.enableInvitedAccessCheckbox,
                                        ft.Row(
                                            [
                                                self.groupNameTextField,
                                                self.maxNumberShareResourcesTF
                                            ],
                                            alignment=ft.MainAxisAlignment.SPACE_AROUND
                                        )
                                    ],
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER               
                                ),
                                padding=20
                            )
                        ) 
                    ], )  
    def loadProperties(self):
        self.enableInvitedAccessCheckbox = ft.Checkbox(label="Permitir acceso de invitado", value=False)
        self.groupNameTextField = ft.TextField(label="Grupo permitido",width=400,value = "users")
        self.enableSharedDirectoriesCheckbox = ft.Checkbox(label="Permitir a los usuarios compartir sus directorios", on_change=self.enableOptionsShareDirectories)
        self.maxNumberShareResourcesTF = ft.TextField(label="Numero maximo de recursos compartidos")
        if config.has_option("global","usershare allow guests"):
            if config['global']['usershare allow guests'] == "Yes":
                self.enableSharedDirectoriesCheckbox.value = True
                self.maxNumberShareResourcesTF.value = config["global"]["usershare max shares"]
                self.enableInvitedAccessCheckbox.disabled = False
                self.enableInvitedAccessCheckbox.value = True
                self.groupNameTextField.disabled = False
                self.maxNumberShareResourcesTF.disabled= False
            else:
                self.enableSharedDirectoriesCheckbox.value = False
                self.maxNumberShareResourcesTF.value = 100
                self.enableInvitedAccessCheckbox.disabled = True
                self.groupNameTextField.disabled = True
                self.maxNumberShareResourcesTF.disabled = True

    def __generateShareTableData__(self):
        self.shareTable.controls[0].rows.clear()
        namesBaseList = config.sections()[1:]
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
                rowToInner.cells.append(ft.DataCell(ft.Text(config[namesBaseList[i]]['guest ok'])))
            except:
                rowToInner.cells.append(ft.DataCell(ft.Text("No")))
            try:  
                rowToInner.cells.append(ft.DataCell(ft.Text(config[namesBaseList[i]]['comment'])))
            except:
                rowToInner.cells.append(ft.DataCell(ft.Text("")))    
            rowToInner.selected = False    
            rowToInner.on_select_changed = self.enableBtnsControls
            self.shareTable.controls[0].rows.append(rowToInner)
    def enableGuestAccess(self,e):
        resourseName = self.currentRowToEdit[2].content.value
        if "guest ok" in config[resourseName]:
            if config[resourseName]["guest ok"] == "Yes":
                config[resourseName]["guest ok"] = "No"
                self.currentRowToEdit[4].content.value = "No"
            else:
                config[resourseName]["guest ok"] = "Yes"
                self.currentRowToEdit[4].content.value = "Yes"
        else:    
            config.set(resourseName,"guest ok","Yes")
        self.page.update()    
            
    def enableResourse(self,e):
        if self.currentRowToEdit[0].content.value == "Habilitado":
            self.currentRowToEdit[0].content.value = "Inhabilitado"
            self.currentRowToEdit[0].content.color= ft.colors.RED_300
        else:
            self.currentRowToEdit[0].content.value = "Habilitado"
            self.currentRowToEdit[0].content.color = ft.colors.LIGHT_GREEN_ACCENT_400
        self.page.update()

    def openDialogNewResourse(self,e):
        newAlert = AlertNewResourse(self.page)
        self.page.dialog = newAlert
        newAlert.open = True
        newAlert.getNameMethodOnDismiss(self.updateChangesOnTable)
        self.page.update()

    def deleteSelectedItem(self,e):
        resourseName = self.currentRowToEdit[2].content.value
        #print("Recurso a eliminar",resourseName)   
        newAlert = AlertMessage(self.page,f"Eliminar Recurso: {resourseName}","warning","Si suprime el recurso compartido, se perderan todos sus ajustes.\n ¿Seguro de que desea suprimirlo?")
        newAlert.getNameMethodOnDismiss(self.updateChangesOnTable)
        self.page.dialog = newAlert
        newAlert.open = True
        self.page.update()

    def openDialogEditResourse(self,e):
        editAlert = AlertEditResourse(self.page,self.currentRowToEdit[2].content.value)
        self.page.dialog = editAlert
        editAlert.open = True
        editAlert.getNameMethodOnDismiss(self.updateChangesOnTable)
        self.page.update()

    def updateChangesOnTable(self,e):
        # print("Dialogo cerrado")  
        self.rowsSelected = 0  
        #print(self.rowsSelected)
        self.currentRowToEdit = ""
        self.__generateShareTableData__()
        self.addBtn.disabled = False
        self.editBtn.disabled = True
        self.deleteBtn.disabled = True
        self.page.update()

    def enableOptionsShareDirectories(self,e):
        if self.enableSharedDirectoriesCheckbox.value:
            self.enableInvitedAccessCheckbox.disabled = False
            self.groupNameTextField.disabled = False
            self.maxNumberShareResourcesTF.disabled= False
            #self.sliderValue.disabled = False
        else:
            self.enableInvitedAccessCheckbox.disabled = True
            self.groupNameTextField.disabled = True
            self.maxNumberShareResourcesTF.disabled = True
            #self.sliderValue.disabled = True
        self.update()    

    def enableBtnsControls(self,e):
        if not e.control.selected:
            #print("Evento seleccionado no")
            if self.rowsSelected == 0:
                self.rowsSelected = self.rowsSelected + 1
                self.currentRowToEdit = e.control.cells
                e.control.selected = True
                self.addBtn.disabled = True                    
                self.editBtn.disabled = False
                self.deleteBtn.disabled = False
                self.guestAccessBtn.disabled = False
                self.toggleStatusBtn.disabled = False
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
                self.deleteBtn.disabled = True
                self.update()
        elif e.control.selected:
            #print("Evento seleccionado ok")
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
                self.editBtn.disabled = True
                self.deleteBtn.disabled = True
                self.update()     

    def saveGeneralChanges(self):
        if self.winsRadioGroup.value == '0':
            config['global']['wins support'] = "Yes"
            if config.has_option('global','wins server'):
                config.remove_option('global','wins server')
        if self.winsRadioGroup.value == '1':
            config['global']['wins support'] = "No"   
            config.set('global','wins server',str(self.nameWinsServer.value))                   

            
            

        