from docxtpl import DocxTemplate
import os
doc = DocxTemplate("maket2.docx")
context = {
    'level': 'Генеральному директору\n',
    'org'  : 'ООО "Приморская ГРЭС"',
    'fio'  : 'Леонову Андрею Николаевичу',
    'obl'  : 'Приморского края',
    'num'  : '01',
    'io'   : 'Андрей Николаевич'
}
doc.render(context)
doc.save(os.path.join(os.getcwd(), 'results', 'maket-new.docx'))