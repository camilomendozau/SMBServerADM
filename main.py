import flet as ft
from views.view1 import Tab1
from views.view2 import Tab2
from views.view3 import Tab3
from views.view4 import Tab4
from views.components import MessageBanner
from config import config
import sh

def main(page: ft.Page):
    page.title = "Panel de Control SAMBA SERVER"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = False
    page.window_resizable = True
    page.auto_scroll = True
    # page.window_width = 1300
    # page.window_height = 850
    page.banner = MessageBanner(pageIn=page)

    def saveGeneralChanges(e):
        # print("Cambios generales realizados")
        tabsToRender.tabs[1].saveGeneralChanges()
        tabsToRender.tabs[2].saveGeneralChanges()
        try:
            sh.sudo.chmod("777","smb.conf")
            with open("smb.conf", 'w') as configfile:
                config.write(configfile)
            page.banner.showSucessfulMessage("Datos guardados satisfactoriamente")
            page.update()
        except PermissionError as e:
            page.banner.showErrorMessage("Error al guardar los cambios")
            print("No se pudo guardar el archivo:",e)
            page.update()

        # # Usar sudo para mover el archivo temporal a su ubicación final
        try:
            sh.sudo.cp("smb.conf", "/etc/samba/smb.conf")
            print("Copia de archivo de configuracion exitosa.")
        except sh.ErrorReturnCode as e:
            print(f"Error copiando el archivo de configuracion: {e}")

        # Verificar la configuración de Samba
        try:
            sh.sudo.testparm('-s')
            print("La configuracion Samba es valida.")
        except sh.ErrorReturnCode as e:
            print(f"Error verificando la configuracion Samba: {e}")

        # Reiniciar el servicio de Samba
        try:
            sh.sudo.systemctl('restart', 'smb')
            print("Servidor SAMBA reiniciado exitosamente.")
        except sh.ErrorReturnCode as e:
            print(f"Error reiniciando el servidor Samba: {e}")


    tabsToRender = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[Tab1(),Tab2(page),Tab3(page),Tab4(page)],
        expand=1,
    )
    page.add(tabsToRender)
    page.add(ft.Row(
                    controls=[
                        #ft.ElevatedButton("Cerar",bgcolor=ft.colors.RED_300,icon=ft.icons.CANCEL),
                        ft.ElevatedButton("Guardar cambios",bgcolor=ft.colors.GREEN_300,icon=ft.icons.SAVE,on_click=saveGeneralChanges)
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment = ft.CrossAxisAlignment.END
                )
    )    


ft.app(target=main)