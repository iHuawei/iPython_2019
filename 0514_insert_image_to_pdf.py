import fitz                          # <-- PyMuPDF
doc = fitz.open("OFDM_tutorial.pdf")          # open the PDF
rect = fitz.Rect(0, 0, 100, 100)     # where to put image: use upper left corner

for page in doc:
    page.insertImage(rect, filename = "test.jpeg")

doc.saveIncr()                       # do an incremental save