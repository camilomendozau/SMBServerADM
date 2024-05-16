import flet as ft

class Tab2(ft.Tab):
    def __init__(self):
        super().__init__()
        self.addBtn = ft.OutlinedButton(text="Añadir...", icon = ft.icons.ADD)
        self.editBtn = ft.OutlinedButton(text="Editar...", disabled=True, icon = ft.icons.EDIT_ROUNDED)
        self.deleteBtn = ft.OutlinedButton(text="Suprimir", disabled=True, icon = ft.icons.DELETE)
        self.rowsSelected = 0

        self.text ="Compartidos"
        self.icon = ft.icons.FOLDER_SHARED
        self.content=ft.Column(
                    controls=[
                        ft.Row(
                            controls = [ft.Text("Recursos compartidos disponibles:"),
                                       ft.Dropdown(
                                                        width=300,
                                                        options=[
                                                            ft.dropdown.Option("Por nombre"),
                                                            ft.dropdown.Option("Por fecha"),
                                                        ],
                                                        label="Filtrar",
                                        )],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,            
                        ),
                        ft.Row(
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
                                        rows=[
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                                    ft.DataCell(ft.Text("Si")),
                                                    ft.DataCell(ft.Text("impresora")),
                                                    ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                                    ft.DataCell(ft.Text("No")),
                                                    ft.DataCell(ft.Text("Printer Drivers"))
                                                ],
                                                on_select_changed= self.unableBtnsControls
                                            ),
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                                    ft.DataCell(ft.Text("Si")),
                                                    ft.DataCell(ft.Text("Fotocopiadora")),
                                                    ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                                    ft.DataCell(ft.Text("No")),
                                                    ft.DataCell(ft.Text("Printer Drivers"))
                                                ],
                                                on_select_changed= self.unableBtnsControls
                                            ),
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text("Habilitado",color=ft.colors.LIGHT_GREEN_ACCENT_400)),
                                                    ft.DataCell(ft.Text("Si")),
                                                    ft.DataCell(ft.Text("Compartidos")),
                                                    ft.DataCell(ft.Text("/var/lib/samba/drivers")),
                                                    ft.DataCell(ft.Text("No")),
                                                    ft.DataCell(ft.Text("Printer Drivers")),
                                                ],
                                                on_select_changed= self.unableBtnsControls
                                            ),
                                        ]
                                    
                                    )
                                ],
                            alignment=ft.MainAxisAlignment.CENTER, 
                        ),    
                        ft.Row(
                            controls = [self.addBtn,self.editBtn,self.deleteBtn],
                            alignment=ft.MainAxisAlignment.START
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls= [
                                        ft.Text("Recursos compartidos por los usuarios"),
                                        ft.Checkbox(label="Permitir a los usuarios compartir sus directorios",value=True),
                                        ft.Checkbox(label="Permitir acceso de invitado"),
                                        ft.TextField(label="Grupo permitido",width=400,value="users"),
                                        ft.Text("Numero maximo de recursos compartidos:"),
                                        ft.Slider(min=0, max=10, divisions=1, label="{value}")
                                    ],
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER               
                                ),
                                padding=20
                            )
                        ) 
                    ], )  
            
    def unableBtnsControls(self,e):
        if not e.control.selected:
            if self.rowsSelected == 0:
                self.rowsSelected = self.rowsSelected + 1
                print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = True
                self.addBtn.disabled = True                    
                self.editBtn.disabled = False
                self.deleteBtn.disabled = False
                self.update()
            elif self.rowsSelected == 1:  
                self.rowsSelected = self.rowsSelected + 1
                print(e.control.cells[2].content.value,self.rowsSelected, sep='|')         
                e.control.selected = True  
                self.addBtn.disabled = True                    
                self.editBtn.disabled = True
                self.deleteBtn.disabled = False
                self.update()      
            elif self.rowsSelected > 1:
                self.rowsSelected = self.rowsSelected + 1
                print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = True       
                self.addBtn.disabled = True
                self.editBtn.disabled = True
                self.deleteBtn.disabled = False
                self.update()
        elif e.control.selected:
            if self.rowsSelected == 0:
                print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = True
                self.addBtn.disabled = False                    
                self.editBtn.disabled = True
                self.deleteBtn.disabled = True
                self.update()
            if self.rowsSelected == 1:
                self.rowsSelected = self.rowsSelected - 1
                print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = False 
                self.addBtn.disabled = False
                self.editBtn.disabled = True
                self.deleteBtn.disabled = True    
                self.update()
            elif self.rowsSelected > 1:
                self.rowsSelected = self.rowsSelected - 1
                print(e.control.cells[2].content.value,self.rowsSelected, sep='|')
                e.control.selected = False
                self.addBtn.disabled = True
                self.editBtn.disabled = False
                self.deleteBtn.disabled = False
                self.update()

            
            

        