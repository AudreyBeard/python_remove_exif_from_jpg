# Removing EXIF data has never been this easy!
This Python3 script removes the EXIF data from all JPG files in its directory.

# Usage if you don't trust me:

1. Carefully go through the Python source code to see what happens.
2. Make sure that the pillow library is installed (Windows: pip install pillow, Ubuntu: sudo pip3 install pillow)
3. Put the Python script into the same directory that all your JPG files are in.
4. Run the Python script.


# Usage if you trust me:

1. Make sure that you run the 64-bit version of Windows 10.
2. Put the EXE file into the same directory that all your JPG files are in.
3. Open CMD in the correct path and use "certutil -hashfile remove_exif.exe SHA256" to calulate the SHA256 hash.
4. Make sure that the EXE has the following SHA256: b1daf1cff42182adb52010e86d8bf2eed364601e8be964c98b6fe7465f804bcf
5. Run the EXE file.


# Wait.. you are still reading? Do you want to know more?

I used "pyinstaller --onefile remove_exif.py" to convert the Python file into an EXE.
There is one known issue with the EXE (which is no problem AFAIK): 
If you run the exe file in a directory that does not contain any JPG files there will be 
split-second of some error shown before the CMD closes. IDK why that happens (it doesn't happen with the python script), I think it must be some kind of issue with pyinstaller. 

