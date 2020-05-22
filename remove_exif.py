# pip install pillow
import os
import sys
from PIL import Image


def strip_exif(images):
    global left
    left -= 1
    print("Removing EXIF of", images, "[" + str(left), "images left]"
          if left > 1 else "image left]" if left == 1 else "images left]")
    image = Image.open(images)
    data = list(image.getdata())
    no_exif = Image.new(image.mode, image.size)
    no_exif.putdata(data)
    no_exif.save(images)


files = [f for f in os.listdir('.') if os.path.isfile(f)]
allowed = {".JPG", ".jpg", "JPEG", "jpeg"}
for i in files:
    if i[-4:] not in allowed:
        files.remove(i)
left = len(files)
if left == 0:
    sys.exit()
for i in files:
    if i[-3:] != ".py":
        strip_exif(i)

print("\nDone.")
