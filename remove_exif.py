# pip install pillow
import os
import sys
from PIL import Image


def strip_exif(image):
    global left
    left -= 1
    directory, filename = os.path.split(image)
    print("Removing EXIF of", filename, "[" + str(left), "images left]"
          if left > 1 else "image left]" if left == 1 else "images left]")
    image = Image.open(image)
    data = list(image.getdata())
    no_exif = Image.new(image.mode, image.size)
    no_exif.putdata(data)
    no_exif.save(filename)


path = os.path.dirname(os.path.realpath(__file__))
files = [f for f in os.listdir('.') if os.path.isfile(f)]
allowed = {".JPG", ".jpg", "JPEG", "jpeg"}
for i in files:
    # for some reason i manually need to filter the py script itself
    if i[-4:] not in allowed or i[-3] == ".py":
        files.remove(i)
left = len(files)
for i in files:
    strip_exif(i)
print("\nDone.")
