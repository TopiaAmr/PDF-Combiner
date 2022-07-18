import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir('./pdfs'):

    # PDF Files only

    if file.endswith('.pdf'):
        print(file)
        merger.append(f'./pdfs/{file}')
    merger.write('./output/combinedPDFs.pdf')
