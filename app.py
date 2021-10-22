try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mats.lillas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

im = Image.open('images/test.png')
text = pytesseract.image_to_string(im)

print(text)
