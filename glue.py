file = open("samples/Invoice.html",'r')
invoice = file.read()
from lxml import html
tree = html.fromstring(invoice)
items = tree.xpath('//div[@class="delete-wpr"]/text()')
re.match('\s*(.*)\s*',items[1]).group(1)

