import PyPDF4
import math
from util import read_pdf, loop_pages, write_pdf, get_blank_page

base_path = '/mnt/c/Users/atlsve/Dropbox/Atle PHD/artikler/kappe/'

REPLACEMENTS = {
  "#PAPER 1#": 'Sveen - 2017 - The Open Geospatial Data Ecosystem.pdf',
  "#PAPER 2#": 'Sveen et al. - 2019 - Micro-tasking as a method for human assessment and.pdf',
  "#PAPER 3#": 'Sveen - 2019 - Efficient storage of heterogeneous geospatial data.pdf',
  "#PAPER 4#": 'Sveen - 2020 - GeomDiff — an algorithm for differential geospatia.pdf'
}

def round_up_to_even(f):
  return math.ceil(f / 2.) * 2

def is_odd(f):
  return f % 2 != 0

def contains(page, text):
  try: 
    page_content = page.extractText().replace("\n", "").replace(" ", "")
    return text.replace(" ", "") in page_content
  except KeyError:
    return False

def get_insertion_pdf(page):
  for key in REPLACEMENTS.keys():
    if contains(page, key):
      print(f"found key {key}, will insert file {REPLACEMENTS[key]}")
      return read_pdf(f"{base_path}{REPLACEMENTS[key]}")      
  return None


master_document = read_pdf(f"{base_path}kappe_v2.pdf")
pages = []

num_skip = 0
for page in loop_pages(master_document):
  insertion = get_insertion_pdf(page)

  if insertion is not None:
    num_pages = insertion.getNumPages()
    num_skip = round_up_to_even(num_pages) - 1
    print(f"skip {num_skip} pages from original")

    pages += list(loop_pages(insertion))

    if is_odd(num_pages):
      pages.append(get_blank_page())
  elif num_skip > 0:
    num_skip = num_skip -1
  else:
    pages.append(page)

write_pdf(pages, f'{base_path}merged3.pdf')
