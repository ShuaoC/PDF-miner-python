import PyPDF2

file = open("sample.pdf","rb")
menu = open("Menu.pdf","rb")

reader = PyPDF2.PdfFileReader(file)
menuReader = PyPDF2.PdfFileReader(menu)

print(reader.numPages)

print(menuReader.numPages)