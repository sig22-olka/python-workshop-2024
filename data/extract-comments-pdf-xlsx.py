import fitz
doc = fitz.open("example.pdf")
for i in range(doc.pageCount):
  page = doc[i]
  for annot in page.annots():
    print(annot.info["content"])
