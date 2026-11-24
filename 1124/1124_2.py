from PIL import Image, ImageDraw, ImageFont

# 1. 讀取原圖與 QR Code（★ 請在這裡填入你自己的檔名 ★）
original_img = Image.open("Ark.jpg")  # <-- 這裡改你的原圖檔名
qr_img = Image.open("qrcode.png")  # <-- 這裡改你的 QR Code 檔名

# 複製原圖來加工，確保不會動到原圖變數
img = original_img.copy()

# 3. 調整 QR Code 大小並貼到左上角 (座標 20, 20 留一點邊距比較好看)
qr_img = qr_img.resize((120, 120))  # 視需要調整 QR Code 大小，若剛好可刪掉這行
img.paste(qr_img, (20, 20))

# 4. 在圖片下方加上文字（沒有黑底）
draw = ImageDraw.Draw(img)
text = "b11413002 羅中廷"

try:
  font = ImageFont.truetype("C:/Windows/Fonts/msjh.ttc", size=32)
except OSError:
  font = ImageFont.load_default()

# 直接畫上文字（fill 為文字顏色，這裡設為白色 (255, 255, 255)）
draw.text((24, 550), text, fill=(255, 255, 0), font=font)

# 5. 另存新檔
img.save("postcard-2.jpg", quality=95)
print("完成！已另存為 postcard.jpg")
