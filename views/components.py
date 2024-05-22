import flet as ft
import time
class EditMask(ft.Row):
    def __init__(self,onClickSaveBtnMethodName):
        super().__init__()
        self.modal=True
        self.selectedMatrix = [
                                 [False,False,False],
                                 [False,False,False],
                                 [False,False,False]
                            ]
                                 
        self.saveBtn = ft.IconButton(
                                        icon=ft.icons.SAVE,
                                        icon_color = ft.colors.GREEN_700,
                                        tooltip = "Guardar propiedad",
                                        on_click=onClickSaveBtnMethodName,
                                        disabled=True,          
                                    )
        self.messageTextBanner = ft.Text("Debe modificar los valores", color=ft.colors.RED_500, visible=False)
        self.alignment = ft.MainAxisAlignment.CENTER
        self.visible = False
        self.dataTableMask = ft.DataTable(                                    
                                                border=ft.border.all(2, "red"),
                                                border_radius=10,
                                                vertical_lines=ft.border.BorderSide(3, "blue"),
                                                horizontal_lines=ft.border.BorderSide(1, "green"),
                                                sort_column_index=2,
                                                sort_ascending=True,
                                                heading_row_color=ft.colors.BLACK12,
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
                                                        cells=[]
                                                    ),
                                                    ft.DataRow(
                                                        cells=[]
                                                    ),
                                                    ft.DataRow(
                                                        cells=[]
                                                    )
                                                ]
                                            )                                         
        self.controls = [self.dataTableMask,self.saveBtn,self.messageTextBanner]

    def buildTable(self,numberMaskInput):
        numberMask = list(str(numberMaskInput))
        namesUsers = ["Usuario","Grupo","Otros"]
        for i in range(3):
            self.dataTableMask.rows[i].cells.append(ft.DataCell(ft.Text(namesUsers[i])))
            j = 0
            cociente = int(numberMask[i+1])
            if cociente < 4:
                self.selectedMatrix[i][2] = 0
            while cociente >= 0 and j < 3:
                bit = int(cociente%2)
                if  bit == 1:
                    self.selectedMatrix[i][j] = 1
                elif bit == 0:   
                    self.selectedMatrix[i][j] = 0
                cociente = cociente/2
                j = j + 1 
    
        for i in range(3):
            self.selectedMatrix[i] = self.selectedMatrix[i][::-1]
            for j in range(3):
                if self.selectedMatrix[i][j] == 1:
                    self.dataTableMask.rows[i].cells.append(ft.DataCell(ft.Checkbox(value=True,on_change=self.unableSavelIconBtn)))
                elif self.selectedMatrix[i][j] == 0:   
                    self.dataTableMask.rows[i].cells.append(ft.DataCell(ft.Checkbox(value=False, on_change=self.unableSavelIconBtn)))     
        self.page.update()                
        
    def generateNumberMask(self):
        numbersOwner = [0,0,0]
        for i in range(len(self.dataTableMask.rows)):
            potencia = 2
            for j in range(1,len(self.dataTableMask.rows[i].cells)):
                if self.dataTableMask.rows[i].cells[j].content.value is True:
                   numbersOwner[i] = 2 ** potencia + numbersOwner[i]
                potencia = potencia-1      
        return f'0{numbersOwner[0]}{numbersOwner[1]}{numbersOwner[2]}'       
                                        
    def unableSavelIconBtn(self,e):
        self.saveBtn.disabled = False
        self.page.update()

    # def saveDialog(self,e):
    #     if not self.saveBtn.disabled:
    #         self.buildTable()
    #         print("Guardando datos")
    #     else:
    #         self.messageTextBanner.visible = True    
    #     self.page.update()    

    def getMaskNumber(self):
        return 0
    
class FieldTextEdit(ft.Row):
    def __init__(self,textFieldVal,labelFieldText,onClickIconBtnMethodName):
        super().__init__()
        self.textField = ft.TextField(label=labelFieldText,
                                      width=500,
                                      disabled=True,
                                      value = textFieldVal,
                                      on_change=self.unableSaveBtn
                                    )
        self.iconBtn = ""
        self.saveBtn = ft.IconButton(
                                        icon=ft.icons.SAVE,
                                        icon_color = ft.colors.GREEN_700,
                                        tooltip = "Guardar propiedad",
                                        disabled=True,    
                                        visible = False,   
                                        on_click=self.saveTextValue
                                    )
        if onClickIconBtnMethodName == None:
            self.iconBtn = ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            icon_color = ft.colors.BLUE_500,
                                            tooltip = "Editar propiedad",
                                            on_click=self.unableSelfTextField
                            )
        else:
            self.iconBtn = ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            icon_color = ft.colors.BLUE_500,
                                            tooltip = "Editar propiedad",
                                            on_click=onClickIconBtnMethodName
                            )    
        self.controls=[self.textField,self.iconBtn,self.saveBtn]  
    def getValue(self):
        return self.textField.value
    def updateTextFieldValue(self,valueToUpdate):
        self.textField.value = str(valueToUpdate)
    def unableSaveBtn(self,e):
        self.saveBtn.disabled = False
        self.page.update()
    def unableSelfTextField(self,e):
        self.saveBtn.visible = True
        self.iconBtn.visible = False
        self.textField.disabled = False
        self.page.update()
    def saveTextValue(self,e):
        #self.textField.value = self.textField.value
        self.saveBtn.visible = False
        self.iconBtn.visible = True
        self.textField.disabled = True
        self.page.update()
        
class MaskElement(ft.Row):
    def __init__(self,labelFieldText):
        super().__init__()
        self.tableEditContainer = EditMask(onClickSaveBtnMethodName=self.convertSaveNumberMask)
        self.textFieldContainer = FieldTextEdit(textFieldVal="0000",labelFieldText=labelFieldText,onClickIconBtnMethodName=self.showMaskTable)
        self.controls=[self.textFieldContainer,self.tableEditContainer]    

    def showMaskTable(self,e):
        self.tableEditContainer.buildTable(str(self.textFieldContainer.getValue()))
        self.tableEditContainer.visible = True
        self.textFieldContainer.visible = False
        self.page.update()

    def convertSaveNumberMask(self,e):
        self.textFieldContainer.updateTextFieldValue(self.tableEditContainer.generateNumberMask())
        self.tableEditContainer.visible = False
        self.textFieldContainer.visible = True
        self.page.update()   

class MessageBanner (ft.Banner):
    def __init__(self,pageIn):
        super().__init__()
        self.page = pageIn
        self.textMessage = ft.Text("")
        self.content=self.textMessage
        self.actions=[
            ft.TextButton("Ok",on_click=self.closeBanner),
        ]
    def showSucessfulMessage(self,message):
        self.bgcolor=ft.colors.GREEN_100
        self.textMessage.value = message
        self.leading = ft.Icon(ft.icons.CHECK, color=ft.colors.GREEN_300, size=20)
        self.page.banner.open = True
        self.page.update()

    def showWarningMessage(self,message):
        self.bgcolor=ft.colors.AMBER_100
        self.textMessage.value = message
        self.leading = ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=20)
        self.page.banner.open = True
        self.page.update()   

    def closeBanner(self,e):
        self.page.banner.open = False
        self.page.update()    

class CheckboxElement(ft.Row):
    def __init__(self,labelIn):
        super().__init__()    
        self.saveBtn = ft.IconButton(
                                        icon=ft.icons.SAVE,
                                        icon_color = ft.colors.GREEN_700,
                                        tooltip = "Guardar propiedad",
                                        visible=False,
                                        disabled=True,       
                                        on_click=self.disableCheckBox   
                                    )  
        self.checkbox = ft.Checkbox(label=labelIn,disabled=True,on_change=self.enableSaveBtn)
        self.editBtn = ft.IconButton(
                        icon=ft.icons.EDIT,
                        icon_color = ft.colors.BLUE_500,
                        tooltip = "Editar propiedad",
                        on_click=self.enableCheckBox
                    )
        self.controls = [
            self.checkbox,
            self.saveBtn,
            self.editBtn
        ]  
    def enableSaveBtn(self,e):
        self.saveBtn.disabled = False
        self.page.update()    
    def enableCheckBox(self,e):
        self.saveBtn.visible = True
        self.editBtn.visible = False
        self.checkbox.disabled = False
        self.page.update()
    def disableCheckBox(self,e):
        self.saveBtn.visible = False
        self.editBtn.visible = True
        self.checkbox.disabled = True
        self.page.update()    

                                          
                                        
   