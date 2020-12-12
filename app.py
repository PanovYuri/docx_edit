import os
import zipfile

WORK_DIRECTORY = os.getcwd()
TEMP_FILE = os.path.join(WORK_DIRECTORY, 'temp.xml')
DOCS_FILE = os.path.join(WORK_DIRECTORY, 'docs', 'word', 'document.xml')

def createZip(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))
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
    print('=== Проверка путей по умолчанию ===')
    print(WORK_DIRECTORY)
    print(TEMP_FILE)
    print(DOCS_FILE)

    print('=== Редактирование файла ===')
    editValue('#ОРГАНИЗАЦИЯ#', 'ОАО ГАЗПРОМ')

    print('=== Архивирование ===')
    zipf = zipfile.ZipFile(os.path.join(WORK_DIRECTORY, 'org.docx'), 'w', zipfile.ZIP_DEFLATED)
    createZip('docs', zipf)
    zipf.close()