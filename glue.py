from Tkinter import Tk
from tkFileDialog import askopenfilename
import re
from lxml import html
import time

Tk().withdraw()
path = askopenfilename()

file = open(path,'r')
invoice = file.read()
tree = html.fromstring(invoice)
items = tree.xpath('//div[@class="delete-wpr"]/text()')
items_clean = [re.match('^[\s~^]*(.*?)\s*$',elem).group(1) for elem in items]
prices = tree.xpath('//td[@class="price" and @style="font-weight:bold;font-style:italic" or @style="font-weight:bold;"]/label/text()')
prices_clean = [re.match('^\D*(.*)$',elem).group(1) for elem in prices]
for i in zip(items_clean, prices_clean):
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
