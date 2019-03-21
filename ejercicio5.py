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

#for a,i,x in zip(provincia_radar,latitud,longitud):
	#print ("http://www.openstreetmap.org/search?query=%s#map=15/45.3325/-100.1207/%s/%s" % (a,i,x))

for i,x in zip(latitud,longitud):
	#print("https://www.openstreetmap.org/search?query=%s-1.50566#map=8/%s/%s" % (i,i,x))
	print ("http://www.openstreetmap.org/search?query=%s#map=15/45.3325/-100.1207/%s/%s" % (i,i,x))

#//CARRETERA[DENOMINACION="N-234"]/RADAR/PUNTO_INICIAL/LATITUD/text()
#//CARRETERA[DENOMINACION="N-234"]/RADAR/PUNTO_INICIAL/LONGITUD/text()
#print ("http://www.openstreetmap.org/search?query=akaska#map=15/45.3325/-100.1207/%s/%s" % (latitud,longitud))
#https://www.openstreetmap.org/search?query=41.84701532%2C-3.11377559#map=8/41.847/-3.115