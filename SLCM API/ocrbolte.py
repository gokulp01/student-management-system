import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\TESSERACT\tesseract.exe"

# Load image, grayscale, Otsu's threshold
image = cv2.imread('GenerateCaptcha.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Blur and perform text extraction
thresh = cv2.GaussianBlur(thresh, (3,3), 0)
data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
print(data)

cv2.imshow('thresh', thresh)
cv2.waitKey()