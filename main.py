import PyPDF2

merger = PyPDF2.PdfMerger()
pdfiles = ["unit 1.pdf", "unit 2.pdf", "tut.pdf"]
for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')




