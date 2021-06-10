from PIL import Image
from googletrans import Translator
import pytesseract

translator = Translator()
translator.translate('안녕하세요.', dest='en')
# gt = googletrans.Translator()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"E:\example_01.png"
image = Image.open(image_path)

grabbed = pytesseract.image_to_string(image)

print(grabbed)

processed = translator.translate(grabbed, dest='ja', src='auto')
 
print(processed)




