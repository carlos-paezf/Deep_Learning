# pip install PyMuPDF
# https: // pymupdf.readthedocs.io/en/latest/
import fitz


file_pdf = 'LasMinasDelReySalomon.pdf'
document = fitz.open(file_pdf)


# Extraer información básica del documento
print('Número de páginas: ', document.pageCount)
print('Metadatos: ', document.metadata)


# Extraer el texto de una página en específico
page = document.loadPage(5)
text = page.getText('text')
print(text)


# Extraer todo el texto del documento
name_file = 'LasMinasDelReySalomon'
doc = fitz.open(file_pdf)
file_txt = open(name_file + '.txt', 'wb')
for page in doc:
    text = page.getText().encode('utf-8')
    file_txt.write(text)
    file_txt.write(b'\n-----\n')
file_txt.close()