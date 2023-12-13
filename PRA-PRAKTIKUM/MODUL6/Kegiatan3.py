from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance

image = Image.open("D:\KULIAH\SEMESTER 5\FUNGSIONAL\PRAKTIKUM\Click Here\PRA-PRAKTIKUM\MODUL6/assets/gyj.jpg")

enhancer = ImageEnhance.Brightness(image)
brightened = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened)
final = enhancer.enhance(1.2)

# final.save("gyjawaw.jpg")
final.show()