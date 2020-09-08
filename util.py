import PyPDF4

def read_pdf(path):
  return PyPDF4.PdfFileReader(open(path, mode="rb"))

def loop_pages(pdf):
  for i in range(pdf.getNumPages()):
    yield(pdf.getPage(i))

def write_pdf(pages, filename):
  pdf_writer = PyPDF4.PdfFileWriter()
  for page in pages:
    pdf_writer.addPage(page)

  with open(filename, 'wb') as out:
    pdf_writer.write(out)

def get_blank_page():
  return PyPDF4.pdf.PageObject.createBlankPage(width=595.32, height=841.92)