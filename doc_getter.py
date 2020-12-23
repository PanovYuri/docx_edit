from docxtpl import DocxTemplate
import os
import pandas as pd 

WORKING_DIRECTORY = os.getcwd()
SHEET_FILE = os.path.join(WORKING_DIRECTORY, 'data', 'data.xls')
DOCS_FILE = os.path.join(WORKING_DIRECTORY, 'data', 'maket.docx')

get_str_num = lambda num: f"{num:02d}"

# Получение данных из таблицы
def generate_docs(list_name):
    data = pd.read_excel(SHEET_FILE, list_name)
    for i in data.index:
        context = {
            'level' : data['Должность'][i],
            'org'   : data['Организация'][i],
            'fio'   : data['ФИО'][i].title().strip(),
            'num'   : get_str_num(data['Номер письма'][i]),
            'obl'   : 'Ханто-Мансийского АО',
            'io'    : data['ИО'][i].title(),
            'gender': 'Уважаемая' if str(data['ПОЛ'][i]) == '+' else 'Уважаемый'
        }
        doc = DocxTemplate(DOCS_FILE)
        doc.render(context)
        doc.save(os.path.join(os.getcwd(), 'results', '22.12 ХМАО {}.docx'.format(data['Организация'][i].replace('"', ''))))
        print("Выполнен документ номер: {}".format(i))

if __name__ == '__main__':
    generate_docs('Лист6')