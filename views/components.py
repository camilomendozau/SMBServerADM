import flet as ft
class EditMask(ft.Row):
    def __init__(self,onClickSaveBtnMethodName):
        super().__init__()
        self.modal=True
        self.title=ft.Text()
        self.maskNumber = 0
        self.__userValues = ([],[])
        self.__groupValues = ([],[])
        self.__otherValues = ([],[])
        self.__selectedMatrix = [
                                 [False,True,False],
                                 [False,False,False],
                                 [True,False,True]
                                ]
        
        self.__valuesMatrix = [
                                 [2,1,0],
                                 [2,1,0],
                                 [2,1,0]
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
                                                        cells=[
                                                            ft.DataCell(ft.Text("Usuario")),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn)),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn)),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn))
                                                        ]
                                                    ),
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(ft.Text("Grupo")),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn)),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn)),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn))
                                                        ]
                                                    ),
                                                    ft.DataRow(
                                                        cells=[
                                                            ft.DataCell(ft.Text("Otros")),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn)),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn)),
                                                            ft.DataCell(ft.Checkbox(on_change=self.unableSavelIconBtn))
                                                        ]
                                                    )
                                                ]
                                            )                                         
        self.controls = [self.dataTableMask,self.saveBtn,self.messageTextBanner]
    # def buildTable(self):
    #     for i in range(len(self.__selectedMatrix)):
    #         self.dataTableMask.rows[i].cells[0] = ft.DataCell(ft.Text("Usuario")),
    #         for j in range(len(self.__selectedMatrix[i])):
    #             if self.__selectedMatrix[i][j] is True:
    #                self.__valuesMatrix[i][j] = 2 ** self.__valuesMatrix[i][j]
    #             else:
    #                self.__valuesMatrix[i][j] = 0      
    #     print(self.dataTableMask.rows[0].cells)               TRABAJAR EN ESTO

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
    def __init__(self,labelFieldText,onClickIconBtnMethodName):
        super().__init__()
        self.controls=[ ft.TextField(label=labelFieldText,
                                      width=500,
                                      disabled=True
                                    ),
                        ft.IconButton(
                                        icon=ft.icons.EDIT,
                                        icon_color = ft.colors.BLUE_500,
                                        tooltip = "Editar propiedad",
                                        on_click=onClickIconBtnMethodName
                        )
                    ]   
        
class MaskElement(ft.Row):
    def __init__(self,labelFieldText):
        super().__init__()
        self.tableEditContainer = EditMask(onClickSaveBtnMethodName=self.convertSaveNumberMask)
        self.textFieldContainer = FieldTextEdit(labelFieldText=labelFieldText,onClickIconBtnMethodName=self.showMaskTable)
        self.controls=[ self.textFieldContainer,
                       self.tableEditContainer
                    ]     
    def showMaskTable(self,e):
        self.tableEditContainer.visible = True
        self.textFieldContainer.visible = False
        self.page.update()

    def convertSaveNumberMask(self,e):
        self.tableEditContainer.buildTable()
        self.tableEditContainer.visible = False
        self.textFieldContainer.visible = True
        self.page.update()   

                                          
                                        
   


