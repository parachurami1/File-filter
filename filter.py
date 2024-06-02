import os
import shutil
import time
import subprocess

cmd = subprocess.Popen("set USERPROFILE", shell=True, stdout=subprocess.PIPE)
str = cmd.stdout.read().decode()
user = str.split("=")
user = user[1].strip()
dir = user+"\\Downloads"

vid_folder = user+'\\Downloads\\downloaded_vids'
exe_folder = user+'\\Downloads\\downloaded_exe'
pic_folder = user+'\\Downloads\\downloaded_pics'
office_folder = user+'\\Downloads\\office_documents'
pdf_folder = user+'\\Downloads\\pdf'
archive_folder = user+'\\Downloads\\archive'
webdoc_folder = user+'\\Downloads\\webdocs'
txt_folder = user+'\\Downloads\\texts'
audio_folder = user+'\\Downloads\\audio_folder'
torrent_folder = user+'\\Downloads\\torrent_folder'
dirs = [vid_folder,exe_folder,pic_folder,office_folder,pdf_folder,archive_folder,webdoc_folder,txt_folder,audio_folder,torrent_folder]
#unidentified = user+'\\Downloads\\unidentified'

for i in dirs:
    print(i)
    try:
        subprocess.call(f"mkdir {i}", shell=True)
    except Exception:
        print("pass")

def filter():
    while True:
        with os.scandir(dir) as entries:
            for i in entries:
        #        
                if i.name[-4:].lower() == '.mp4' or i.name[-4:].lower() == '.mkv' or i.name[-4:].lower() == '.srt':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,vid_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-4:].lower() == '.exe' or i.name[-4:].lower() == '.msi':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,exe_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-4:].lower() == '.png' or i.name[-4:].lower() == '.jpg' or i.name[-5:].lower() == '.jpeg':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,pic_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-4:].lower() == '.xls' or i.name[-4:].lower() == '.ppt' or i.name[-5:].lower() == '.pptx' or i.name[-4:].lower() == '.doc' or i.name[-5:].lower() == '.docx' or i.name[-5:].lower() == '.xlsx':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,office_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-4:].lower() == '.pdf':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,pdf_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-3:].lower() == '.7z' or i.name[-4:].lower() == '.zip' or i.name[-7:].lower() == '.tar.gz' or i.name[-4:].lower() == '.rar' or i.name[-4:] == '.iso':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,archive_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-5:].lower() == '.html' or i.name[-4:].lower() == '.htm' or i.name[-6:].lower() == '.mhtml' or i.name[-5:].lower() == '.webp':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,webdoc_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-4:].lower() == '.txt' or i.name[-3:].lower() == '.md':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,txt_folder)
                    except(PermissionError):
                        filter()
                    # except(shutil.Error):
                    #     os.remove(i)
                    #     filter()
                elif i.name[-4:].lower() == '.mp3':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,audio_folder)
                    except(PermissionError):
                        filter()

                elif i.name[-8:].lower() == '.torrent':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,torrent_folder)
                    except(PermissionError):
                        filter()

filter()