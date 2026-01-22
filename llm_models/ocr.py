from PIL import Image
import pytesseract


image = Image.open("aadhya_birth_certificate.png")
text = pytesseract.image_to_string(image)

print(text)
