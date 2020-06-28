# pdf_crop

This script splits scanned pdf pages, based on functions of a library called PyPDF2.
You might need this if you have scanned pdf books with 2 actual pages gathered in one (horizontally).
It returns a single new pdf file with the split pages placed in correct order.
This improves the file's readability in devices like kindle.

### Requirements: python 3 and PyPDF2 package INSTALLED*** (If this is new to you, go to the end of the page)

### croppdfpage.py Usage:
   1. Open your terminal.
   2. Install the PyPDF2 package. To do it, execute the following command:

python -m pip install pypdf2

   3. Download the "croppdfpage.py" file and copy the PATH of the folder where you placed it. In our example, this PATH will be C:\Users\Maria\Desktop\

   4. Execute the following command in your terminal, replacing the example names in capital letters for the ones that make sense to your environment/files

python C:\USERS\MARIA\DESKTOP\croppdfpage.py C:\USERS\MARIA\DOCUMENTS\BOOKS\CARROLL_Alice.pdf C:\USERS\MARIA\DOCUMENTS\BOOKS\CARROLL_Alice_CROP.pdf 

## Explaining the example:
-Suppose you have placed your "croppdfpage.py" in a local folder with the following path:
C:\Users\Maria\Desktop\

-And that your pdf file, i.e. your book, is in a local folder called Books, in you Documents folder such as:
C:\Users\Maria\Documents\Books\

-In this example, CARROLL_Alice.pdf is the existing file, and CARROLL_Alice_CROP.pdf is the new file you will create with the split pages.

## Make your life easier

As you might have noticed, it gets easier to use this script if the pdf files and the croppdfpage.py file are all in the same folder.

## Details for the ones who code:
"model page" is the one with the most frequent shape. The default set is 5, but you can change it, and even set it to ask the user to choose the page only by commenting and uncommenting the lines related to "model page". 
(setting it is necessary because many scanned books have the cover in distinct shape - usually portrait - than the rest of the book - usually landscape) 
 
Crops of different shapes can be made by changing the cropBox function parameters. 


@author: Ana de Angelo - sanchesdeangelo@gmail.com
telegram: @anadeangelo

Feel free to contact me if you have any doubts!


***
## Details for the ones who doesn't:

***If you are new to Python, it is strongly recommended that you access the following page:
https://opentechschool.github.io/python-beginners/en/getting_started.html#what-is-python-exactly

***To install Python:
https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe
