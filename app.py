from PIL import Image
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mats.lillas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def rename():
    os.walk('images')
    imgDir = os.listdir()
    imgDirLength = len(os.listdir())
    ix = 0
    for imgDir[ix] in range(imgDirLength):
        os.rename(str(imgDir[ix]), 'image'+str(ix)+'.png')
    os.walk('../')

rename()

num = 0
for num in range(len(os.listdir('images'))):
    im = Image.open('images/image'+str(num)+'.png')
    text = pytesseract.image_to_string(im)

    text = text.lower()
    list = text.split(" ")

    i = 0
    for i in range(len(list)):
        if(list[i].find("total") != -1):
            total = list[i]

    try:
        total = total.replace("total", "")
        total = total.replace("€", "")
        total = total.replace("$", "")
        total = total.replace(",", ".")
        total = total.replace("\n", "")
    except:
        print("epic fail")
    print(float(total))