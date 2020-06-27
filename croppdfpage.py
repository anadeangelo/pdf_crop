# -*- coding: utf-8 -*-
"""
This script splits scanned pdf pages with two actual pages gathered in one (horizontally).
It returns a single new pdf file with the split pages placed in correct order.
This can be usefull if you have pdf files of scanned old books and need to read them in an e-book reader like kindle.

"model page" is the one with the most frequent shape 
(setting it is important because many scanned books have the cover in distinct shape - usually portrait - than the rest of the book - usually landscape) 
 
Crops of different shapes can be made by changing the cropBox function parameters. 

Usage: yourpythonpath/python croppdfpage.py <pdffilename.pdf> <NEWpdffilename.pdf>

@author: Ana de Angelo - sanchesdeangelo@gmail.com
telegram: @anadeangelo
"""

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

file = str(sys.argv[1])
newfile = str(sys.argv[2])

with open(file, "rb") as pdf1:
    pdf = PdfFileReader(pdf1)
    output = PdfFileWriter()
    page1 =  pdf.getPage(int(input('insert the number of the model page: ')))
    ll = page1.trimBox.getLowerLeft()  #ll stands for lower left
    ur = page1.trimBox.getUpperRight()  #ur stands for upper right

    numpages = pdf.getNumPages()

    for i in range(numpages):
        page = pdf.getPage(i)
        if i % 2 == 0:        
            page.cropBox.lowerLeft = ll
            page.cropBox.upperRight = ((ur[0]/2)-5, ur[1])
            output.addPage(page)
        else:
            page.cropBox.lowerLeft = ((ur[0]/2)+5, ll[1])
            page.cropBox.upperRight = (ur[0], ur[1])
            output.addPage(page)
        
    with open(newfile, "wb") as newpdf:
        output.write(newpdf)