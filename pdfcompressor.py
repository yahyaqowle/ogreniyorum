# # Import the necessary modules
# from PyPDF2 import PdfFileReader
#
# # Open the PDF file
# with open('test12.pdf', 'rb') as file:
#     # Create a PdfFileReader object
#     reader = PdfFileReader(file)
#
#     # Get the number of pages in the PDF file
#     num_pages = reader.getNumPages()
#
#     # Loop through all the pages and extract the text
#     for page in range(num_pages):
#         page_obj = reader.getPage(page)
#         text = page_obj.extractText()
#
#         # Print the text on the screen
#         print(text)
#
#         # Save the text to a file
#         with open('textfile2.txt', 'w') as outfile:
#             outfile.write(text)


# Import the necessary modules
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

# Open the PDF file
with open('hope.pdf', 'rb') as file:
    # Create a PDFResourceManager object
    resource_manager = PDFResourceManager()

    # Create a StringIO object
    string_io = StringIO()

    # Create a TextConverter object
    converter = TextConverter(resource_manager, string_io, codec='utf-8', laparams=LAParams())

    # Create a PDFPageInterpreter object
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    # Loop through all the pages and extract the text
    for page in PDFPage.get_pages(file):
        page_interpreter.process_page(page)

    # Close the converter
    converter.close()

    # Get the text from the StringIO object
    text = string_io.getvalue()

    # Print the text on the screen
    print(text)

    # Save the text to a file
    with open('hope.txt', 'w') as outfile:
        outfile.write(text)