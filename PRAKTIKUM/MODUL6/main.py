from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from rembg import remove 

background = Image.open("D:\\KULIAH\\SEMESTER 5\\FUNGSIONAL\\PRAKTIKUM\\Click Here\\PRAKTIKUM\\MODUL6\\umm.jpg")
overlay = Image.open("D:\\KULIAH\\SEMESTER 5\\FUNGSIONAL\\PRAKTIKUM\\Click Here\\PRAKTIKUM\\MODUL6\\umm_overlay.png")

font = "D:\KULIAH\SEMESTER 5\FUNGSIONAL\PRAKTIKUM\Click Here/font\ARIBL0.ttf"

background = background.resize((1920,1080))
bg_copy = ImageOps.grayscale(background.copy())
rotated = bg_copy.rotate(30)
final_bg = rotated.filter(ImageFilter.BLUR)



#NIM 402
enhancer = ImageEnhance.Brightness(overlay.copy())
brightened = enhancer.enhance(1.2)

enhancer = ImageEnhance.Contrast(brightened)
effect = enhancer.enhance(1.2)
# model = effect.rotate(30)
final = effect.resize((600,600))


 


padding = 40

customFont = ImageFont.truetype(font, 24)
draw = ImageDraw.Draw(final)
text = "INFORMATIKA JOSSS"
bg_width, bg_height = final.size
text_width, text_height = draw.textsize(text, font=customFont)
text_position = ((bg_width - text_width) // 2, bg_height - text_height - padding)
draw.text(text_position,text, font = customFont, fill="black")
final_bg.paste(final, (600,300))

final_bg.show()






