from lxml import etree
doc = etree.parse('radares.xml')

def carre_provincias(carretera,doc):
	radares = doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)' % carretera)
	radares = int(radares)
	carretera = doc.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()' % carretera)
	return radares,carretera

carretera = input("Dime el nombre de una carretera: ").upper()

radares,carretera = carre_provincias(carretera,doc)

for i in carretera:
	print (i)
print ("Numero de radares:",radares)

