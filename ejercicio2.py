from lxml import etree
doc = etree.parse('radares.xml')

def cantidad_radares(doc):
	radares = doc.xpath('count(//RADAR)')
	radares = int(radares)
	return radares

print ("Cantidad de radares:",cantidad_radares(doc))