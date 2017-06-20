import PyPDF2

fhand= open("SO questões arquivo.pdf", 'rb')

pdfreader = PyPDF2.PdfFileReader(fhand)

page = pdfreader.getPage(0)

print(page.extractText())
