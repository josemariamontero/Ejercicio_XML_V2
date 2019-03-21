from lxml import etree
doc = etree.parse('radares.xml')

def carre_provincias(carretera,doc):
	carretera = doc.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()' % carretera)
	radares = doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)' % carretera)
	radares = int(radares)
	return carretera,radares

carretera = input("Dime el nombre de una carretera: ").upper()

carreteras,radares = carre_provincias(carretera,doc) 

for i in carreteras:
	print (i)
print ("Numero de radares:",radares)

#count(//CARRETERA[DENOMINACION="CM-3226"]/RADAR)