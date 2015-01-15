import re
from lxml import html

file = open("samples/Invoice.html",'r')
invoice = file.read()
tree = html.fromstring(invoice)
items = tree.xpath('//div[@class="delete-wpr"]/text()')
items_clean = [re.match('^[\s~^]*(.*?)\s*$',elem).group(1) for elem in items]
prices = tree.xpath('//td[@class="price" and @style="font-weight:bold;font-style:italic" or @style="font-weight:bold;"]/label/text()')
