from lxml import etree
doc = etree.parse('radares.xml')

def coordenadas(carretera,doc):
	radares = doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)' % carretera)
	radares = int(radares)
	provincia_radar = doc.xpath('//CARRETERA[DENOMINACION="%s"]/../NOMBRE/text()' % carretera)
	latitud = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()' % carretera)
	longitud = doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()' % carretera)
	return radares,latitud,longitud,provincia_radar 

carretera = input("Dime el nombre de una carretera: ").upper()

radares,latitud,longitud,provincia_radar = coordenadas(carretera,doc) 

print ("Numero de radares:",radares)

for i,x in zip(latitud,longitud):
	print("https://www.openstreetmap.org/search?query=%s,%s#map=19/%s/%s" % (i,x,i,x))

#//CARRETERA[DENOMINACION="N-234"]/RADAR/PUNTO_INICIAL/LATITUD/text()
#//CARRETERA[DENOMINACION="N-234"]/RADAR/PUNTO_INICIAL/LONGITUD/text()
