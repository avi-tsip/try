import pyttsx3
import PyPDF2

# Create a pdf reader
book = open('python.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages

# Create a speaker
speaker = pyttsx3.init()
for num in range(3, pages): # Start to count from 3 to the end of the pages
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.say(f'finished reading page {num}. would you like to continue to next page? type y to continue or any other key to stop')
    speaker.runAndWait()
    result = input('Type y to continue or any other key to stop')
    if result == 'y':
        continue
    else:
        break
speaker.stop()
