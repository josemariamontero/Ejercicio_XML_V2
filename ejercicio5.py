from lxml import etree
doc = etree.parse('radares.xml')

def coordenadas(carretera,doc):
	radares = doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)' % carretera)
	radares = int(radares)
	coordenadas =
	return radares

carretera = input("Dime el nombre de una carretera: ").upper()

radares = coordenadas(carretera,doc) 

print ("Numero de radares:",radares)

#//CARRETERA[DENOMINACION="N-234"]/RADAR/PUNTO_INICIAL/LATITUD/text()
#//CARRETERA[DENOMINACION="N-234"]/RADAR/PUNTO_INICIAL/LONGITUD/text()