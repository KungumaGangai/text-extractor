from PIL import Image
import pytesseract
import jinja2
import webbrowser

title = "TxtExt"
definition = "<h2>Text extarctor is a simple application used to extract the desired text from the image!<h2>"
pics = [ ['E:/example.jpg','This is image 1'],
         ['E:/example_01.png','This is image 2'],
         ['E:/example_03.png','This is image 3'] ]

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image_path = r"E:/example_01.png"
image = Image.open(image_path)
txt_from_img = pytesseract.image_to_string(image)
txt = "<h3> Below is the text extracted from the given image  <h3>" + txt_from_img


outputfile = "E:/gitprojects/textextractor-conda/home.html"

subs = jinja2.Environment(
              loader=jinja2.FileSystemLoader('E:/gitprojects/textextractor-conda/')
              ).get_template('page1.html').render(title=title, content=definition, input_img=pics ,output=txt)

# lets write a substitution to a file
with open(outputfile,'w') as f: f.write(subs)

webbrowser.open_new_tab(outputfile)

