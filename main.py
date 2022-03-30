from unicodedata import name
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import re

def pdfminer(file, output): 
    inFile = open(file, 'rb')
    rM = PDFResourceManager()
    data = io.StringIO()
    TxtConverter = TextConverter(rM, data,laparams = LAParams())
    interpreter = PDFPageInterpreter(rM, TxtConverter)
    
    for page in PDFPage.get_pages(inFile): 
        interpreter.process_page(page)
        
    txt = data.getvalue()
    with open(output, 'w') as f: 
         f.write(txt)


   
file = "test.pdf" 
output = "info.txt"
pdfminer(file, output)

text_file = open('info.txt','r')
stringData = text_file.read()
email='felix@google.com'
text_file.close()
print(stringData)

email_pattern = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
name_pattern = '[a-zA-Z]+ [a-zA-Z]+' 
phone_pattern = "\(?\d{3}[-.)]\d{3}[-.]\d{4}"

if(re.search(name_pattern,"sdada adadas")):
    print(re.search(phone_pattern,"123-234-2344"))
else:
    print('No')

name_list = re.findall(name_pattern, stringData)
phone_list = re.findall(phone_pattern,stringData)
# name_list = re.findall(name_pattern,stringData)
# phone_list = re.findall(phone_pattern,stringData)
print(phone_list)
# print(name_list)
# print(phone_list)