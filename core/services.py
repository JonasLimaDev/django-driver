import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def logar_drive():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    return drive

def upload_drive(local):
    drive = logar_drive()
    
    file = open(local)
    fn = os.path.basename(file.name)
    file_drive = drive.CreateFile({'title': fn, 'mimeType': 'application/pdf' })
    file_drive.SetContentFile(local)
    file_drive.Upload()
    permission = file_drive.InsertPermission({
                            'type': 'anyone',
                            'value': 'anyone',
                            'role': 'reader'})
    return file_drive['alternateLink']


