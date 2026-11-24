# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFilter, ImageFont

img = Image.open("Ark.jpg")

img = img.resize((800, 600))

img = img.filter(ImageFilter.GaussianBlur(radius=1))
img = img.filter(ImageFilter.SHARPEN)

draw = ImageDraw.Draw(img)
text = "B11413002 羅中廷"

# Windows 常見中文字型路徑範例，若無字型可改用 ImageFont.load_default()
try:
  font = ImageFont.truetype("C:/Windows/Fonts/msjh.ttc", size=32)
except OSError:
  font = ImageFont.load_default()

draw.text((24, 550), text, fill=(255, 255, 0), font=font)

img.save("postcard.jpg", quality=95)
print("完成！已儲存")
