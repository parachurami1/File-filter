import os
import shutil
import time

dir = "C:\\Users\\USER\\Downloads"

vid_folder = 'C:\\Users\\USER\\Downloads\\downloaded vids'
exe_folder = 'C:\\Users\\USER\\Downloads\\downloaded exe'
pic_folder = 'C:\\Users\\USER\\Downloads\\downloaded pics'
office_folder = 'C:\\Users\\USER\\Downloads\\office documents'
pdf_folder = 'C:\\Users\\USER\\Downloads\\pdf'
archive_folder = 'C:\\Users\\USER\\Downloads\\archive'
webdoc_folder = 'C:\\Users\\USER\\Downloads\\webdocs'
txt_folder = 'C:\\Users\\USER\\Downloads\\texts'
#unidentified = 'C:\\Users\\USER\\Downloads\\unidentified'
def filter():
    while True:
        with os.scandir(dir) as entries:
            for i in entries:
        #        print(i.name)
                if i.name[-4:] == '.mp4' or i.name[-4:] == '.mkv' or i.name[-4:] == '.srt':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,vid_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-4:] == '.exe':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,exe_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-4:] == '.png' or i.name[-4:] == '.jpg' or i.name[-5:] == '.jpeg':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,pic_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-4:] == '.xls' or i.name[-4:] == '.ppt' or i.name[-5:] == '.pptx' or i.name[-4:] == '.doc' or i.name[-5:] == '.docx' or i.name[-5:] == '.xlsx':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,office_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-4:] == '.pdf':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,pdf_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-3:] == '.7z' or i.name[-4:] == '.zip' or i.name[-7:] == '.tar.gz' or i.name[-4:] == '.rar':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,archive_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-5:] == '.html' or i.name[-4:] == '.htm' or i.name[-6:] == '.mhtml' or i.name[-5:] == '.webp':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,webdoc_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()
                elif i.name[-4:] == '.txt' or i.name[-3:] == '.md':
                    try:
                        #time.sleep(3)
                        shutil.move(i.path,txt_folder)
                    except(PermissionError):
                        filter()
                    except(shutil.Error):
                        os.remove(i)
                        filter()

filter()