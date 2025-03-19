
# import fitz
import logging
logging.getLogger("ppocr").setLevel(logging.ERROR)
# pdffile = "images.pdf"
# doc = fitz.open(pdffile)
# page = doc.load_page(0)  # number of page
# pix = page.get_pixmap()
# output = "outfile.png"
# pix.save(output)
# doc.close()
from paddleocr import PaddleOCR

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")  # Use English model

# Run OCR on an image
results = ocr.ocr("hand1.jpg", cls=True)

# Extract and print only the recognized text
extracted_text = "\n".join([line[1][0] for line in results[0]])  # Extract text from the results
print(extracted_text)
# from PIL import Image
# import pytesseract
# import cv2
# pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
# image = cv2.imread("outfile.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
# text = pytesseract.image_to_string(Image.open('outfile.png'))
# print(text)

# from paddleocr import PaddleOCR

# ocr = PaddleOCR()
# result = ocr.ocr('images.png', cls=True)
# for line in result:
#     print(line)


# import easyocr

# reader = easyocr.Reader(['en'])  # Load English model
# text = reader.readtext('hand1.jpg', detail=0)
# print(text)