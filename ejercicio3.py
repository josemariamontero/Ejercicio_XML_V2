from lxml import etree
doc = etree.parse('radares.xml')

def carre_radar(provincia,doc):
	carreteras = doc.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()' % provincia)
	radares = doc.xpath('count(//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR)' % provincia)
	radares = int(radares)
	return carreteras,radares

provincia = input("Dime el nombre de una provincia: ")

carreteras = carre_radar(provincia,doc)
radares = carre_radar(provincia,doc)


for i,x in zip(carreteras,radares):
	print ("Nombre Carretera:",i)
	print ("Numero de Radares:",x)
	
#//PROVINCIA/NOMBRE/../CARRETERA/DENOMINACION/text()