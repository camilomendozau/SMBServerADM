import flet as ft
from config import config
from views.components import MaskElement,FieldTextEdit,CheckboxElement,FilePickerElement
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
    def __init__(self,pageActual,dataToEdit):
        super().__init__()
        self.page = pageActual
        self.resourceName = dataToEdit
        #print(dataToEdit)
        self.modal=True
        self.title=ft.Row(
            [
                ft.Text("Editar recurso compartido: ", color=ft.colors.BLACK),
                ft.Text(self.resourceName, color=ft.colors.BLUE_500)
            ])
        self.optionsEnglishSpanish = {
            "Yes":True,
            "No":False
        }
        self.cancelBtn = ft.ElevatedButton(text="Cancelar",on_click=self.cancelDialog, icon=ft.icons.CANCEL, color=ft.colors.RED_400)
        self.saveBtn = ft.ElevatedButton(text="Guardar",on_click=self.saveDialog, icon=ft.icons.SAVE, color=ft.colors.GREEN_600)
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
            ],
        )
        self.loadProperties()
        self.actions=[self.cancelBtn,self.saveBtn]
        self.actions_alignment="end"
        
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
                    propertyElementToInner.append(CheckboxElement(labelIn="Solo Lectura",ckeckboxInitValue=self.optionsEnglishSpanish[config[self.resourceName]['read only']]))   
                if property == "store dos attributes":
                    propertyElementToInner.append(CheckboxElement("Atributos DOS almacenados",ckeckboxInitValue=self.optionsEnglishSpanish[config[self.resourceName]['store dos attributes']]))
                if property == "create mask":
                    propertyElementToInner.append(MaskElement(labelFieldText="Crear Mascara", textFielValueIn=config[self.resourceName]['create mask']))
                if property == "directory mask":
                    propertyElementToInner.append(MaskElement(labelFieldText="Mascara de Carpeta",textFielValueIn=config[self.resourceName]['directory mask']))
                if property == "inherit acls":            
                    propertyElementToInner.append(CheckboxElement("Heredar ACL",self.optionsEnglishSpanish[config[self.resourceName]['inherit acls']])) 
                if property == "browsable":
                    propertyElementToInner.append(CheckboxElement("Navegable",self.optionsEnglishSpanish[config[self.resourceName]["browseable"]])) 
        self.page.update()

    def cancelDialog(self,e):
        self.open = False
        self.page.update()

    def saveDialog(self,e):
        self.open = False
        self.page.update()  