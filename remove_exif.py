import os
import sys
from PIL import Image


def count(images, left):
    print("Removing EXIF of", images, "[" + str(left), "image left]"
          if left == 1 else "images left]")


def strip_exif(images, left):
    # inform user about progress
    count(images, left)

    # strip EXIF and overwrite image
    image = Image.open(images)
    data = list(image.getdata())
    no_exif = Image.new(image.mode, image.size)
    no_exif.putdata(data)
    no_exif.save(images)


def main():
    # get all files in the scripts directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    jpg_files = []

    # add all JPG files into a new list
    for i in files:
        if i.upper().endswith(".JPG") or i.upper().endswith(".JPEG"):
            jpg_files.append(i)

    # determine how many JPGs EXIF will be stripped
    left = len(jpg_files)

    # abort if no JPG file is found
    if left == 0:
        print("No JPG files found.")
        return

    # go through every JPG and strip EXIF data
    for i in jpg_files:
        left -= 1
        strip_exif(i, left)

    print("\nDone.")


main()
