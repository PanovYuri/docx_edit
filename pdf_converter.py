from docx2pdf import convert
import os

doc_path = os.path.join(os.getcwd(), 'results')
pdf_path = os.path.join(os.getcwd(), 'pdf')

# convert(doc_path, doc_root)

files_arr = []
files_arr_pdf = []

for (dirpath, dirnames, files) in os.walk(os.path.join(os.getcwd(), 'results')):
    files_arr.extend(files)
    break

for (dirpath, dirnames, files) in os.walk(os.path.join(os.getcwd(), 'pdf')):
    files_arr_pdf.extend(files)
    break

for file in files_arr:
    path_d = os.path.join(doc_path, file)
    pdf_file = file[:-4] + 'pdf'
    if not pdf_file in files_arr_pdf:
        path_p = os.path.join(pdf_path, pdf_file)
        convert(path_d, path_p)