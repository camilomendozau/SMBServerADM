import flet as ft
from config import config,optionsEnglishSpanish
from views.components import MaskElement,FieldTextEdit,CheckboxElement,FilePickerElement,BottomDialogElement

class AlertNewResourse(ft.AlertDialog):
    def __init__(self,pageActual):
        super().__init__()
        self.page = pageActual
        self.modal=True
        self.title=ft.Text("Crear nuevo recurso compartido")
        self.cancelBtn = ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400)
        self.saveBtn = ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600, disabled = True)
        self.resourseNameTF = ft.TextField(label="Nombre del recurso", width=500,on_change=self.enableSaveBtn)
        self.descriptionTF = ft.TextField(label="Descripción", width=500,on_change=self.enableSaveBtn)
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
                                    value = 0,
                                    on_change = self.enableAndDisabledElementsBecauseResourseType
                                )
        self.readOnlyCheckBox = ft.Checkbox(label="Solo Lectura",on_change=self.enableSaveBtn)
        self.inheritACLCheckBox = ft.Checkbox(label="Heredar las ACL",on_change=self.enableSaveBtn, value=True)
        self.btrfsCheckBox = ft.Checkbox(label="Utilizar caracteristicas de BtrFS",on_change=self.enableSaveBtn)
        self.filePicker = FilePickerElement(self.page,"/var/tmp")
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
                                self.filePicker,
                                ft.Column(
                                    controls= [
                                        self.readOnlyCheckBox,
                                        self.inheritACLCheckBox,
                                        # ft.Checkbox(label="Exponer instantaneas", disabled=True,on_change=self.enableSaveBtn),
                                        self.btrfsCheckBox
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

    def enableAndDisabledElementsBecauseResourseType(self,e):
        if self.typeResourseRadioGroup.value == "0":
            self.readOnlyCheckBox.disabled = False
            self.inheritACLCheckBox.disabled = False
            self.btrfsCheckBox.disabled = True
            self.filePicker.enable()
        else:
            self.readOnlyCheckBox.disabled = True
            self.inheritACLCheckBox.disabled = True
            self.btrfsCheckBox.disabled = False
            self.filePicker.disable()
        self.saveBtn.disabled = False
        self.page.update()    

    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        if self.resourseNameTF.value == "":
            self.__textFieldEmpty__(self.resourseNameTF)
        elif self.descriptionTF.value == "":
            self.__textFieldEmpty__(self.descriptionTF)    
        elif self.filePicker.selectedFolderTF.value == "":
            self.__textFieldEmpty__(self.filePicker.selectedFolderTF)   
        elif self.typeResourseRadioGroup.value == None:
            self.textError.value = "Debe elegir una opcion"
            self.page.update()
        else:
            try:
                if int(self.typeResourseRadioGroup.value) == 0:
                    # print("Recurso carpeta guadado")
                    config.add_section(str(self.resourseNameTF.value))
                    config.set(str(self.resourseNameTF.value),"comment",str(self.descriptionTF.value))
                    config.set(str(self.resourseNameTF.value),"inherit acls",optionsEnglishSpanish[self.inheritACLCheckBox.value])
                    config.set(str(self.resourseNameTF.value),"path",str(self.filePicker.selectedFolderTF.value))
                    config.set(str(self.resourseNameTF.value),"read only",optionsEnglishSpanish[self.readOnlyCheckBox.value])
                    if self.btrfsCheckBox.value == True:
                        config.set(str(self.resourseNameTF.value),"vfs objects","btfrs")
                    else:
                        config.set(str(self.resourseNameTF.value),"vfs objects","")    
                if int(self.typeResourseRadioGroup.value) == 1:
                    # print("Recurso impresora guardado")
                    config.add_section(str(self.resourseNameTF.value))
                    config.set(str(self.resourseNameTF.value),"comment",str(self.descriptionTF.value))
                    config.set(str(self.resourseNameTF.value),"path",str(self.filePicker.selectedFolderTF.value))
                    config.set(str(self.resourseNameTF.value),"printable","Yes")    
            except Exception as e:
                print("NO se pudo guardar:",e)

            print(config.sections())   
            self.open = False
            self.page.update()

    def __textFieldEmpty__(self,textfield):
        textfield.focused_border_color = ft.colors.RED_500
        textfield.error_text = "Este campo no debe estar vacio"
        textfield.focus()
        self.page.update()

    def getNameMethodOnDismiss(self,methodName):
        self.on_dismiss = methodName    

    def enableSaveBtn(self,e):
        self.saveBtn.disabled = False
        self.resourseNameTF.error_text = None
        self.resourseNameTF.focused_border_color = None
        self.descriptionTF.error_text = None
        self.descriptionTF.focused_border_color = None
        # self.filePicker.selectedFolderTF.error_text = None
        # self.filePicker.selectedFolderTF.focused_border_color = None
        self.textError.value = ""
        self.page.update()      

class AlertMessage(ft.AlertDialog):
    def __init__(self,pageActual,title,type,message):
        super().__init__()
        self.page = pageActual
        self.modal = True
        self.title = ft.Text(title)
        if type == "error":
            self.content = ft.Row(
                [ft.Icon(ft.icons.ERROR,color=ft.colors.RED_600,size=60),ft.Text(message)],
            )
        if type == "warning":
            self.content = ft.Row(
                [ft.Icon(ft.icons.WARNING,color=ft.colors.AMBER_600,size=60),ft.Text(message)],
            )
        if type == "success":
            self.content = ft.Row(
                [ft.Icon(ft.icons.CHECK_CIRCLE,color=ft.colors.GREEN_600,size=60),ft.Text(message)],
            )
        self.noBtn = ft.ElevatedButton(text="No",icon=ft.icons.CANCEL, color=ft.colors.RED_400, on_click=self.denyMessage)
        self.okBtn = ft.ElevatedButton(text="Si", icon=ft.icons.CHECK, color=ft.colors.GREEN_400, on_click=self.acceptMessage)  
          
        self.actions = [self.okBtn,self.noBtn]
        self.actions_alignment="end"

    def denyMessage(self,e):
        # print(e)
        self.open = False
        self.page.update()

    def acceptMessage(self,e):
        try:
            config.remove_section(self.title.value.split(': ')[1])
        except Exception as error:
            print("Error al eliminar recurso:",error)    
        self.open = False
        self.page.update()    

    def getNameMethodOnDismiss(self,methodName):
        self.on_dismiss = methodName

class AlertEditResourse(ft.AlertDialog):
    def __init__(self,pageActual,dataToEdit):
        super().__init__()
        self.page = pageActual
        self.resourceName = dataToEdit
        self.modal=True
        self.resourceNameElement = FieldTextEdit(self.resourceName,"",onClickIconBtnMethodName=None)
        self.resourceNameElement.setTextFieldWidth(200)
        self.title=ft.Row(
            [
                ft.Text("Editar recurso compartido: ", color=ft.colors.BLACK),
                self.resourceNameElement
                # ft.Text(self.resourceName, color=ft.colors.BLUE_500)
                
            ])
        self.cancelBtn = ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400)
        self.saveBtn = ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600)
        self.createNewPropertyBtn = ft.IconButton(
                                        icon=ft.icons.ADD,
                                        icon_color="blue400",
                                        icon_size=40,
                                        tooltip="Añadir nueva propiedad",
                                        on_click=self.openDialogToCreateNewProperty
                                    )
        
        self.content=ft.Column(
            controls=[
                ft.Card(
                    content= ft.Container(
                        ft.Column(
                            controls=[],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER   
                        ),
                        padding=10
                    ),
                    width = 800,
                ),
                self.createNewPropertyBtn
            ],
        )
        self.loadProperties()
        self.actions=[self.cancelBtn,self.saveBtn]
        self.actions_alignment="end"
        self.propertiesList = ["Crear Mascara","Mascara de Carpeta"]

    def getNameMethodOnDismiss(self,methodName):
        self.on_dismiss = methodName

        
    def loadProperties(self):
        for property in list(config[self.resourceName].keys()):
            propertyElementToInner = self.content.controls[0].content.content.controls
            if property in config[self.resourceName]:
            #print(property,config[self.resourceName][property],sep=':')
                if property == "comment": 
                    propertyElementToInner.append(FieldTextEdit(textFieldVal=config[self.resourceName]['comment'],labelFieldText="Descripcion",onClickIconBtnMethodName=None))
                if property == "path":
                    propertyElementToInner.append(FilePickerElement(self.page,config[self.resourceName]['path']))
                if property == "read only":    
                    propertyElementToInner.append(CheckboxElement(labelIn="Solo Lectura",ckeckboxInitValue=optionsEnglishSpanish[config[self.resourceName]['read only']]))   
                if property == "store dos attributes":
                    propertyElementToInner.append(CheckboxElement("Atributos DOS almacenados",ckeckboxInitValue=optionsEnglishSpanish[config[self.resourceName]['store dos attributes']]))
                if property == "create mask":
                    propertyElementToInner.append(MaskElement(labelFieldText="Crear Mascara", textFielValueIn=config[self.resourceName]['create mask']))
                if property == "directory mask":
                    propertyElementToInner.append(MaskElement(labelFieldText="Mascara de Carpeta",textFielValueIn=config[self.resourceName]['directory mask']))
                if property == "inherit acls":            
                    propertyElementToInner.append(CheckboxElement("Heredar ACL",optionsEnglishSpanish[config[self.resourceName]['inherit acls']])) 
                if property == "browsable":
                    propertyElementToInner.append(CheckboxElement("Navegable",optionsEnglishSpanish[config[self.resourceName]["browseable"]])) 
        self.page.update()

    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        resourseElementsShowing = self.content.controls[0].content.content.controls
        if self.resourceNameElement.getValue() == self.resourceName:
            for propertyElement in resourseElementsShowing:
                #print(self.optionsEnglishSpanish[propertyElement.getLabel()] ,propertyElement.getValue())
                try:
                    if optionsEnglishSpanish[propertyElement.getLabel()] in config[self.resourceName]:
                        #print("guardar valor existente:",self.resourceName,self.optionsEnglishSpanish[propertyElement.getLabel()],propertyElement.getValue(),sep='-')
                        if isinstance(propertyElement.getValue(),bool):
                            config[self.resourceName][optionsEnglishSpanish[propertyElement.getLabel()]] = optionsEnglishSpanish[propertyElement.getValue()]
                        else:
                            config.set(self.resourceName,optionsEnglishSpanish[propertyElement.getLabel()],propertyElement.getValue())
                    else:
                        #print("guardar nueva propiedad:",self.resourceName,self.optionsEnglishSpanish[propertyElement.getLabel()],propertyElement.getValue(),sep="-")
                        if isinstance(propertyElement.getValue(),bool):
                            config.set(self.resourceName,optionsEnglishSpanish[propertyElement.getLabel()],optionsEnglishSpanish[propertyElement.getValue()])
                        else:
                            config.set(self.resourceName,optionsEnglishSpanish[propertyElement.getLabel()],propertyElement.getValue())
                except Exception as error:
                    print("Error al guardar propiedades editadas:",error)     
        else:
            oldName = self.resourceName
            self.resourceName = self.resourceNameElement.getValue()
            config.add_section(self.resourceName)
            for propertyElement in resourseElementsShowing:
                try:
                    #print("guardar nueva propiedad:",self.resourceName,self.optionsEnglishSpanish[propertyElement.getLabel()],propertyElement.getValue(),sep="-")
                    if isinstance(propertyElement.getValue(),bool):
                        config.set(self.resourceName,optionsEnglishSpanish[propertyElement.getLabel()],optionsEnglishSpanish[propertyElement.getValue()])
                    else:
                        config.set(self.resourceName,optionsEnglishSpanish[propertyElement.getLabel()],propertyElement.getValue())
                except Exception as error:
                    print("Error al guardar nuevo nombre:",error)
            config.remove_section(oldName)        
        self.open = False
        self.page.update()    

    def insertNewProperty(self,e):
        propertyElementToInner = self.content.controls[0].content.content.controls
        propertyElementToInner.append(MaskElement(labelFieldText=self.newPropertyDialog.propertySelected,textFielValueIn="0000"))
        self.newPropertyDialog.open = False
        self.page.update()

    def openDialogToCreateNewProperty(self,e):
        self.newPropertyDialog = BottomDialogElement(self.page,"Elige la propiedad a insertar",self.propertiesList,self.resourceName)
        self.newPropertyDialog.setMethodOnClickAddBtn(self.insertNewProperty)
        self.page.overlay.append(self.newPropertyDialog)
        self.page.update()
