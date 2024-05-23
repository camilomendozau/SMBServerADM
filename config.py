import configparser
config = configparser.ConfigParser()
config.read('/etc/samba/smb.conf')

# config = {
#     "global": {
#         "workgroup": "WORKGROUP",
#         "passdb backend": "tdbsam",
#         "printing": "cups",
#         "printcap name": "cups",
#         "printcap cache time": "750",
#         "cups options": "raw",
#         "map to guest": "Bad User",
#         "logon path": "\\\\%L\\profiles\\.msprofile",
#         "logon home": "\\\\%L\\%U\\.9xprofile",
#         "logon drive": "P:",
#         "usershare allow guests": "Yes",
#         "usershare max shares": "250",
#         "wins support":"No",
#         "wins server" : ""
#     },
#     "homes": {
#         "comment": "Home Directories",
#         "valid users": "%S, %D%w%S",
#         "browseable": "No",
#         "read only": "No",
#         "inherit acls": "Yes"
#     },
#     "profiles": {
#         "comment": "Network Profiles Service",
#         "path": "%H",
#         "read only": "No",
#         "store dos attributes": "Yes",
#         "create mask": "0600",
#         "directory mask": "0700"
#     },
#     "users": {
#         "comment": "All users",
#         "path": "/home",
#         "read only": "No",
#         "inherit acls": "Yes",
#         "veto files": "/aquota.user/groups/shares/"
#     },
#     "groups": {
#         "comment": "All groups",
#         "path": "/home/groups",
#         "read only": "No",
#         "inherit acls": "Yes"
#     },
#     "printers": {
#         "comment": "All Printers",
#         "path": "/var/tmp",
#         "printable": "Yes",
#         "create mask": "0600",
#         "browseable": "No"
#     },
#     "print$": {
#         "comment": "Printer Drivers",
#         "path": "/var/lib/samba/drivers",
#         "write list": "@ntadmin root",
#         "force group": "ntadmin",
#         "create mask": "0664",
#         "directory mask": "0775"
#     }
# }