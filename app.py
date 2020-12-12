import os
import zipfile
import shutil

WORK_DIRECTORY = os.getcwd()
TEMP_FILE = os.path.join(WORK_DIRECTORY, 'data', 'document.xml')
DOCS_FILE = os.path.join(WORK_DIRECTORY, 'docs', 'word', 'document.xml')

def createZip(path, zip):
    for root, dirs, files in os.walk(path):
        print(root)
        for file in files:
            print(file)
            zip.write(os.path.join(root, file), arcname=file)
    print('Архивирование завершено')

def editValue(regex, val):
    with open(TEMP_FILE, 'r') as f:
        docs = f.read()
    print(docs.index(regex))
    docs = docs.replace(regex, val)
    print(docs.index(val))
    with open(DOCS_FILE, 'w') as f:
        f.write(docs)
    print('Запись завершена')

if __name__ in '__main__':
    editValue('#ОРГАНИЗАЦИЯ#', 'ОАО ГАЗПРОМ')
    file_name = os.path.join(WORK_DIRECTORY, 'results', "Петров")
    shutil.make_archive(file_name, 'zip', 'docs')
    os.rename(file_name+'.zip', file_name+'.docx')