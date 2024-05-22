import flet as ft
from views.components import MessageBanner
class Tab4 (ft.Tab):
    def __init__(self,pageIn):
        super().__init__()
        self.page = pageIn
        self.bannerToShow = MessageBanner(self.page)
        self.page.banner = self.bannerToShow
        self.text="Usuarios"
        self.icon=ft.icons.PERM_IDENTITY 
        self.addNewUserSOBtn = ft.OutlinedButton(text="Agregar a S.O.", on_click=self.addUserSO,icon=ft.icons.SAVE,disabled=True)
        self.addNewUserSMBBtn = ft.OutlinedButton(text="Agregar a SAMBA", on_click=self.addUserSMB, icon=ft.icons.SAVE,disabled=True)  
        self.content= ft.Row(
                    controls = [
                            ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Agregar nuevo usuario al Sistema Operativo"),
                                            ft.TextField(label="Nombre de Usuario",on_change=self.unableAddUserSOBtn),
                                            ft.TextField(label="Contraseña",password=True, can_reveal_password=True,on_change=self.unableAddUserSOBtn),
                                            ft.TextField(label="Confirmar Contraseña",password=True, can_reveal_password=True),
                                            self.addNewUserSOBtn
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    width=550,
                                    height=350,
                                    margin=2,
                                    padding=15,
                                ),
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content = ft.Column(
                                        controls = [
                                            ft.Text("Agregar Usuario SAMBA"),
                                            ft.TextField(label="Nombre de Usuario",on_change=self.unableAddUserSMBBtn),
                                            ft.TextField(label="Contraseña",password=True, can_reveal_password=True,on_change=self.unableAddUserSMBBtn),
                                            ft.TextField(label="Confirmar Contraseña",password=True, can_reveal_password=True,on_change=self.unableAddUserSMBBtn),
                                            self.addNewUserSMBBtn
                                        ],
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER
                                    ),
                                    width=550,
                                    height=350,
                                    margin=2,
                                    padding=15,
                                ),
                            )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
        
    def unableAddUserSMBBtn(self,e):
        usernameTF = self.content.controls[1].content.content.controls[1]
        passwordTF = self.content.controls[1].content.content.controls[2]
        confirm_passwordTF = self.content.controls[1].content.content.controls[3]
        self.addNewUserSMBBtn.disabled = False
        usernameTF.error_text = None
        usernameTF.focused_border_color = None
        passwordTF.error_text = None
        passwordTF.focused_border_color = None
        confirm_passwordTF.error_text = None
        confirm_passwordTF.focused_border_color = None
        self.page.update()

    def unableAddUserSOBtn(self,e):
        usernameTF = self.content.controls[0].content.content.controls[1]
        passwordTF = self.content.controls[0].content.content.controls[2]
        confirm_passwordTF = self.content.controls[0].content.content.controls[3]
        self.addNewUserSOBtn.disabled = False
        usernameTF.error_text = None
        usernameTF.focused_border_color = None
        passwordTF.error_text = None
        passwordTF.focused_border_color = None
        confirm_passwordTF.error_text = None
        confirm_passwordTF.focused_border_color = None  
        self.page.update()   

    def addUserSO(self,e):
        usernameTF = self.content.controls[0].content.content.controls[1]
        passwordTF = self.content.controls[0].content.content.controls[2]
        confirm_passwordTF = self.content.controls[0].content.content.controls[3]

        if str(usernameTF.value) == "":
            self.__textFieldEmpty__(usernameTF)
        elif str(passwordTF.value) == "":
            self.__textFieldEmpty__(passwordTF)   
        elif str(confirm_passwordTF.value) == "":
            self.__textFieldEmpty__(confirm_passwordTF)   
        elif str(passwordTF.value) != str(confirm_passwordTF.value):
            self.__textFieldConfirmPswNoEqual__(confirm_passwordTF)
        else:
            self.bannerToShow.showWarningMessage("Guardando nuevo usuario en el Sistema Operativo")
            print('Guardando nuevo usuario SO')    
        
    def addUserSMB(self,e):
        usernameTF = self.content.controls[1].content.content.controls[1]
        passwordTF = self.content.controls[1].content.content.controls[2]
        confirm_passwordTF = self.content.controls[1].content.content.controls[3]

        if str(usernameTF.value) == "":
            self.__textFieldEmpty__(usernameTF)
        elif str(passwordTF.value) == "":
            self.__textFieldEmpty__(passwordTF)   
        elif str(confirm_passwordTF.value) == "":
            self.__textFieldEmpty__(confirm_passwordTF)
        elif str(passwordTF.value) != str(confirm_passwordTF.value):
            self.__textFieldConfirmPswNoEqual__(confirm_passwordTF)    
        else:
            self.bannerToShow.showWarningMessage('Guardando nuevo usuario SMB')
            print('Guardando nuevo usuario SMB')   

    def __textFieldEmpty__(self,textfield):
        textfield.focused_border_color = ft.colors.RED_500
        textfield.error_text = "Este campo no debe estar vacio"
        textfield.focus()
        self.page.update()

    def __textFieldConfirmPswNoEqual__(self,textfield):
        textfield.focused_border_color = ft.colors.RED_500
        textfield.error_text = "La contraseña no es igual"
        textfield.focus()
        self.page.update()   

    def saveUserSMB(self):
        self.bannerToShow.showSucessfulMessage("Uusario añadido satisfactoriamente")

            
        #print(self.content.controls[1].content.content.controls[2].value,self.content.controls[1].content.content.controls[3].value)
        


                