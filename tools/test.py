from PIL import Image
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

img = os.path.join(ROOT, "assets", "fruits", "01-eevee.webp")

print(img)

im = Image.open(img)

print("模式：", im.mode)
print("尺寸：", im.size)