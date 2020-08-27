import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'D:\TESSERACT\tesseract.exe'
img = Image.open('GenerateCaptcha.jpg')
img = img.convert('L')
img.save('final.jpg')
text = tess.image_to_string(img)
print(text)