from lxml import etree
doc = etree.parse('radares.xml')

#print(doc)

def nombres(doc):
	provincias = doc.xpath('//PROVINCIA/NOMBRE/text()')
	return provincias

provincias = (nombres(doc))

for i in provincias:
	print ("Provincia:",i)