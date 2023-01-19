import glob
import os
import shutil
import PySimpleGUI as sg

extensões = {

     "jpg": "imagens",
     "png": "imagens",
     "ico": "imagens",
     "gif": "imagens",
     "svg": "imagens",
     "sql": "Programação",
     "exe": "programas",
     "msi": "programas",
     "pdf": "Documento",
     "xlsx": "Documento",
     "csv": "Documento",
     "rar": "compactado",
     "zip": "compactado",
     "iso": "compactado",
     "gz": "compactado",
     "tar": "compactado",
     "docx": "Documento",
     "torrent": "torrent",
     "txt": "texto",
     "ipynb": "Programação",
     "py": "Programação",
     "pptx": "Documento",
     "ppt": "Documento",
     "mp3": "audio",
     "wav": "áudio",
     "mp4": "vídeo",
     "m3u8": "vídeo",
     "webm": "vídeo",
     "mkv": "vídeo",
     "ts": "vídeo",
     "json": "Programação",
     "css": "Programação",
     "js": "Programação",
     "html": "Programação",
     "apk": "apk",
     "sqlite3": "Programação",
     "bmp": "imagens",
     "jpeg": "imagens",
}
def caminho(path):
    #path = r"C:\Users\Kelven Cardoso\Downloads"
    window2 = sg.Window('Arquivos Organizados', icon='C:\www\pasta.ico')
    layout2 = [[sg.OK(pad=(210, 1))]]
    for extension, folder_name in extensões.items():
        # Pega todos os arquivos que terminam com a extensão
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        if len(files) > 0:
                               
            layout2.append([sg.Text(str(f"[*] Encontrados {len(files)} aquivos com extensão '{extension}', Movido  p/ pasta: {folder_name}"))])
        
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # Cria a pasta se não existir
            print(f"[+] Criado pasta de {folder_name}")
            os.mkdir(os.path.join(path, folder_name))
            
        for file in files:
            # Para cada arquivo, move para a pasta correspondente
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            
            print(f"[*] Movendo {file} para {dst}")
            shutil.move(file, dst)
    if len(layout2) > 1: 
        window.close()
        window2.layout(layout2)
        window2.read()
    else:
        sg.popup('Nenhum arquivo na pasta', icon=r'C:\www\404.ico')



sg.theme('DarkAmber')
layout = [ [sg.Menu(
        [
            ['Sobre', 'Sobre o programa']
        ],
        key='sobre'
    )],
    [sg.Text('Organizador de Pastas', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
      [sg.Text('Pasta dos Arquivos', size=(15, 1)), sg.InputText(), sg.FolderBrowse('Procurar')],
      [sg.Sizer(20,5), sg.OK(pad=8), sg.Cancel()]
      ]
window = sg.Window('Organizador de Pastas (Kelven)', layout, icon='C:\www\pasta.ico')
event, values = window.read()
if event == 'Sobre o programa':
    #sg.popup('Organizador de Pastas\nVersão 1.0\nKelven Cardoso', icon=r'C:\www\pasta.ico')
    sg.Window('1').layout([[sg.Text('Organizador de Pastas\nVersão 1.0\n Move as extensões abaixo')], 
    [sg.Multiline(str(list(extensões)).replace(",", "\n"), size=(15,15))]]).read(close=False)
   
if event == 'OK':
    if values[0] == '':
        sg.popup_error('Caminho vazio', icon=r'C:\www\404.ico')
    else:
         caminho(values[0])
if event in (sg.WIN_CLOSED, 'Cancel'):
    window.close()


