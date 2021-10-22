try:
    from PIL import Image
except ImportError:
    import Image

from re import search
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mats.lillas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

im = Image.open('images/test.png')
text = pytesseract.image_to_string(im)
text = text.lower()

list = text.split(" ")

i = 0
for i in range(len(list)):
    if(list[i].find("total") != -1):
        print(list[i])