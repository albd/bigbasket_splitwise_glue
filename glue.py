from Tkinter import Tk	#importing library for html file selection dialog
from tkFileDialog import askopenfilename
import re	#importing library for regular expressions
from lxml import html	#importing library for lxml paths
import time	#importing library for sleep

Tk().withdraw()
path = askopenfilename()	#displays the file selection dialog to select invoice html file

file = open(path,'r')	#open the stream into html invoice file
invoice = file.read()	#read the content of invoice and stores in variable invoice
tree = html.fromstring(invoice)	#converts the html string into a tree data structure of nested tags
items = tree.xpath('//div[@class="delete-wpr"]/text()')	#xpath to extract content within tag for items. The result is a list of items with preceding and succeeding junk.
items_clean = [re.match('^[\s~^]*(.*?)\s*$',elem).group(1) for elem in items]	#cleans the item list by stripping whitespaces, ^ and ~. The cleanup has been a prudent in that it removes only known junk.
prices = tree.xpath('//td[@class="price" and @style="font-weight:bold;font-style:italic" or @style="font-weight:bold;"]/label/text()')	# xpath to extract content within tag for prices.
prices_clean = [re.match('^\D*(.*)$',elem).group(1) for elem in prices]	#cleaned the content in prices.
for i in zip(items_clean, prices_clean):	#while the keystrokes of items and prices could be simulated directly by using send_keys, it was found that the OS could not keep up with high rate of keystrokes. This led to some keystrokes being skipped. The workaround for this was to store the text in clipboard and then sending Ctrl+V keystrokes to paste the content. This would offload the job actually typing keystrokes to the kernel.
    clipboard.fill_clipboard(i[0])
    keyboard.send_keys("<ctrl>+v")
    time.sleep(0.1)
    keyboard.send_keys("<tab>")
    time.sleep(0.1)
    clipboard.fill_clipboard(i[1])
    keyboard.send_keys("<ctrl>+v")
    time.sleep(0.1)
    keyboard.send_keys("<tab><tab>")
    time.sleep(0.1)
