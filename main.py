import pyttsx3
import PyPDF2


book_name = input("\nEnter pdf name : ")
page_no = int(input("\nEnter page number : "))
book = open(book_name, 'rb')
reader = PyPDF2.PdfFileReader(book)
engine = pyttsx3.init()
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
page = reader.getPage(page_no)
text = page.extractText()
print("\n\n")
engine.say(text)
engine.runAndWait()


