from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from io import StringIO
from collections import namedtuple

Key = namedtuple('Key', ['page', 'paragraph', 'word', 'character'])
message = [
    (188, 2, 5, 3),
    (64, 1, 3, 2),
    (8, 5, 5, 2),
    (205, 3, 8, 3),
    (175, 3, 1, 1),
    (198, 2, 1, 1),
    (26, 2, 1, 5),
    (207, 1, 3, 1),
    (115, 2, 5, 1),
    (181, 4, 5, 2),
    (215, 1, 5, 3),
    (135, 5, 7, 5),
    (71, 2, 3, 1),
    (142, 1, 6, 4),
    (25, 2, 2, 6),
    (61, 2, 4, 4),
    (222, 3, 2, 3),
    (124, 3, 4, 4),
    (144, 4, 3, 1),
    (213, 1, 1, 1),
    (34, 1, 2, 2),
    (181, 2, 2, 1),
    (211, 2, 8, 1),
    (209, 2, 3, 2),
    (37, 2, 1, 1),
    (190, 1, 1, 1),
    (107, 3, 1, 1),
    (195, 3, 3, 2),
    (6, 4, 3, 1),
    (167, 4, 4, 4),
    (168, 3, 6, 6),
    (205, 4, 4, 1),
    (230, 1, 1, 2),
    (188, 4, 6, 1),
    (57, 1, 3, 1),
    (219, 3, 4, 2),
    (45, 2, 11, 4),
    (53, 2, 3, 2),
    (184, 2, 3, 1),
    (164, 1, 3, 5),
    (207, 3, 6, 2),
    (221, 2, 11, 1),
    (21, 2, 2, 2),
    (133, 2, 1, 1),
    (210, 2, 2, 2),
    (76, 2, 4, 1),
    (190, 3, 2, 1),
    (161, 1, 3, 8),
    (42, 2, 4, 2),
    (20, 1, 14, 4),
    (17, 1, 1, 1)
]

# Open a PDF file.
fp = open('2591-pdf.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, TextConverter(rsrcmgr, StringIO(), laparams=LAParams()))
# Process each page contained in the document.

pages = list(PDFPage.create_pages(document))
for key in message:
    key = Key(*key)
    interpreter.device.outfp = StringIO()
    interpreter.process_page(pages[key.page - 1])
    page = interpreter.device.outfp.getvalue()
    paragraphs = page.split('\n\n')

    print(paragraphs[key.paragraph - 1].split()[key.word - 1][key.character - 1], end='')
print()
