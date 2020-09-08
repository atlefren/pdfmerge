import PyPDF4
from util import read_pdf, loop_pages, write_pdf, get_blank_page

def to_a4(page):
  blank = get_blank_page()
  blank.mergePage(page)
  return blank


base_path = '~/'
pdf = read_pdf(f"{base_path}not_a4.pdf")

pages = []
for p in loop_pages(pdf):
  pages.append(to_a4(p))

write_pdf(pages, 'a4_pdf.pdf')
