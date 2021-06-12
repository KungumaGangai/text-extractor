from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"E:\example_01.png"
image = Image.open(image_path)
grabbed = pytesseract.image_to_string(image)
print(grabbed)

# write all the output to a text file instead of the terminal

doc = open('extracted.txt', 'w')
doc.write(grabbed)
doc.close()


wait = input("Press enter to exit")







