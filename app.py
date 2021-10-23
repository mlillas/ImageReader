from PIL import Image
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mats.lillas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

folder = r'images\\'
totalSum = 0.0

def rename():
    count = 0
    for file_name in os.listdir(folder):
        source = folder + file_name
        destination = folder + str(count) + '.png'
        os.rename(source, destination)
        count+=1

rename()

num = 0
for num in range(len(os.listdir('images'))):
    im = Image.open(folder+str(num)+'.png')
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
    totalSum += float(total)

print('The total sum of your spendings is: '+str(round(totalSum, 2)))