# pdf_crop


This script splits scanned pdf pages with two actual pages gathered in one (horizontally).
It returns a single new pdf file with the split pages placed in correct order.

This can be usefull if you have pdf files of scanned old books and need to read them in an e-book reader like kindle.


"model page" is the one with the most frequent shape 
(setting it is important because many scanned books have the cover in distinct shape - usually portrait - than the rest of the book - usually landscape) 
 
Crops of different shapes can be made by changing the cropBox function parameters. 

Usage: 
yourpythonpath/python croppdfpage.py <pdffilename.pdf> <NEWpdffilename.pdf>


@author: Ana de Angelo - sanchesdeangelo@gmail.com
telegram: @anadeangelo


Feel free to contact me if you have any doubts!
