from PIL import Image


background_path = "D:\KULIAH\SEMESTER 5\FUNGSIONAL\PRAKTIKUM\Click Here\PRA-PRAKTIKUM\MODUL6/assets/bg_img.jpg"
overlay_path = "D:\KULIAH\SEMESTER 5\FUNGSIONAL\PRAKTIKUM\Click Here\PRA-PRAKTIKUM\MODUL6/assets/overlay.jpg"
background = Image.open(background_path)
overlay = Image.open(overlay_path)
overlay = overlay.convert("RGBA")
overlay = overlay.resize((100, 100))
x_position = 50
y_position = 50
background.paste(overlay, (x_position, y_position), overlay)
output_path = "output.jpg"
background.save(output_path)
background.show()
