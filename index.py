import PyPDF2

pdFiles=["Ash.pdf","be10x.pdf"]

merger=PyPDF2.PdfMerger()


for filename in pdFiles:
    pdfFile=open(filename,'rb')
    PdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(PdfReader)



pdfFile.close()
merger.write("merged.pdf")    
