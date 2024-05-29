import configparser
import sh

optionsEnglishSpanish = {
            "Yes":True,
            "No":False,
            "Descripcion":"comment",
            "Ruta del recurso compartido":"path",
            "Solo Lectura":"read only",
            "Atributos DOS almacenados":"store dos attributes",
            "Crear Mascara":"create mask",
            "Mascara de Carpeta":"directory mask",
            "Heredar ACL":"inherit acls",
            "Navegable":"browseable",
            True:"Yes",
            False:"No"
        }

try:
    sh.sudo.cp("/etc/samba/smb.conf","smb.conf")
    print("Copia de archivo smb.conf, realizada exitosamente")
except sh.ErrorReturnCode as e:
    print(f"No se pudo relizar la copia: {e}")

config = configparser.ConfigParser()
config.read('smb.conf')



# print(config.sections())
