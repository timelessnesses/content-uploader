from requests import post
from base64 import b64encode
from PIL import ImageGrab
from sys import exit
from os import remove
from os.path import splitext
while True:
	choices = input("Screenshot (s) or File (f) or Clipboard Text(ct) or Text (t) or Quit (q)\n")
	if "s" in a or "S" in choices:
		screen = ImageGrab.grabclipboard()
		screen.save("pic.jpg")
		print("Your screenshot is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=b64encode(open("pic.jpg","rb").read()),headers={"extension":splitext("./pic.jpg")[1]}).text)
		remove("pic.jpg")
	elif "f" in a or "F" in choices:
		path = input("Your file path\n")
		print("Your file is at is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=b64encode(open(path,"rb").read()),headers={"extension":splitext(path)[1]}).text)
	elif choices.startswith("ct") or choices.startswith("CT"):
		from clipboard import paste
		print("Your file is at is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=b64encode(paste()),headers={"extension":"txt"}).text)
	elif choices.startswith("T") or choices.startswith("t"):
		print("Your file is at is at https://content.biomooping.tk/" + post("https://content.biomooping.tk/save",data=b64encode(bytes(input("Text\n\a"),encoding="utf-8")),headers={"extension":"txt"}).text)
	elif "q" in a or "Q" in choices:
		exit("See you next time!")
	else:
		continue
