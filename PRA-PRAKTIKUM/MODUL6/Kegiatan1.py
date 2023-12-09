from PIL import Image, ImageOps, ImageDraw, ImageFont

img = Image.open("D:\\KULIAH\\SEMESTER 5\\FUNGSIONAL\\PRAKTIKUM\\Click Here\\PRA-PRAKTIKUM\\MODUL6\\kucing.jpg")

fontPath = "D:\\KULIAH\\SEMESTER 5\\FUNGSIONAL\\PRAKTIKUM\\Click Here\\static\\Montserrat-Regular.ttf"
customFont = ImageFont.truetype(fontPath, 24)


imgAfter = ImageOps.grayscale(img.copy())
draw = ImageDraw.Draw(imgAfter)
text = "Hello Rafli Kharisma Akbar, 202110370311402"
image_width, image_height = img.size
text_width, text_height = draw.textsize(text, font=customFont)
text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
draw.text(text_position, text, font=customFont, fill="black")


imgAfter.save("output_image.jpg")
imgAfter.show()
