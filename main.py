from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

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