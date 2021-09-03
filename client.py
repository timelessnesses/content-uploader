from requests import post
from base64 import b64encode
from PIL import ImageGrab
from sys import exit
from os import remove
from os.path import splitext
import math
import os
import sys


class ProgressUpload:
    def __init__(self, filename,desiredtext, chunk_size=1250,):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file_size = os.path.getsize(filename)
        self.size_read = 0
        self.divisor = min(math.floor(math.log(self.file_size, 1000)) * 3, 12)  # cap unit at a GB
        self.unit = {0: 'B', 3: 'KB', 6: 'MB', 9: 'GB', }[self.divisor]
        self.divisor = 10 ** self.divisor;self.text = desiredtext


    def __iter__(self):
        progress_str = f'0 / {self.file_size / self.divisor:.2f} {self.unit} (0 %)'
        sys.stderr.write(f'\rUploading {self.text}: {progress_str}')
        with open(self.filename, 'rb') as f:
            for chunk in iter(lambda: f.read(self.chunk_size), b''):
                self.size_read += len(chunk)
                yield chunk
                sys.stderr.write('\b' * len(progress_str))
                percentage = self.size_read / self.file_size * 100
                completed_str = f'{self.size_read / self.divisor:.2f}'
                to_complete_str = f'{self.file_size / self.divisor:.2f} {self.unit}'
                progress_str = f'{completed_str} / {to_complete_str} ({percentage:.2f} %)'
                sys.stderr.write(progress_str)
        sys.stderr.write('\n')

    def __len__(self):
        return self.file_size
while True:
	choices = input("Screenshot (s) or File (f) or Clipboard Text(ct) or Text (t) or Quit (q)\n")
	if "s" in a or "S" in choices:
		screen = ImageGrab.grabclipboard()
		screen.save("pic.jpg")
		print("Your screenshot is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=ProgressUpload("pic.jpg","your screenshot"),headers={"extension":splitext("./pic.jpg",)[1]}).text)
		remove("pic.jpg")
	elif "f" in a or "F" in choices:
		path = input("Your file path\n")

		filename,ext = splitext(path)
		print("Your file is at is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=ProgressUpload(path,filename),headers={"extension":ext}).text)
	elif a.startswith("ct") or a.startswith("CT"):
		from clipboard import paste
		a = open("text.txt","w")
		a.write(paste())
		a.close()
		print("Your file is at is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=ProgressUpload("text.txt","your clipboard text"),headers={"extension":".txt"}).text)
		remove("text.txt")
	elif a.startswith("T") or a.startswith("t"):
		a = open("text.txt","w")
		a.write(input("Text\n\a"))
		a.close()

		print("Your file is at is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=ProgressUpload("text.txt","your text"),headers={"extension":".txt"}).text)
		remove("text.txt")
	elif "q" in a or "Q" in a:
		exit("See you next time!")
	else:
		continue
