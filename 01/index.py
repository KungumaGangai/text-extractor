from PIL import Image
import pytesseract
import jinja2
import webbrowser

title = "TxtExt"
definition = "<h5>Text extarctor is a simple application used to extract the desired text from the image!<h5>"

# pics = 'E:/example_01.png'
pics = 'E:/opencraft.png'
       
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
# image_path = r"E:/example_01.png"
image_path = r"E:/opencraft.png"
image = Image.open(image_path)
txt_from_img = pytesseract.image_to_string(image)
txt = "<h6> Below is the text extracted from the given image  <h6>" + txt_from_img


outputfile = "E:/gitprojects/text-extractor/0.1/home.html"

subs = jinja2.Environment(
              loader=jinja2.FileSystemLoader('E:/gitprojects/text-extractor/0.1/')
              ).get_template('page1.html').render(title=title, content=definition, input_img=pics ,output=txt)

# lets write a substitution to a file
with open(outputfile,'w') as f: f.write(subs)

webbrowser.open_new_tab(outputfile)

