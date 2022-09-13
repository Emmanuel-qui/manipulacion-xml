#Importando libreria para la manipulacion de XML.

from lxml import etree

#Obteniendo la ruta o el archivo XML
path = "cfdi.xml"

# Leer nuestro XML 
xml_string = open(path, "rb").read()

# Convertimos nuestro XML a cadena.
root = etree.fromstring(xml_string)

namespace = {'cfdi':"http://www.sat.gob.mx/cfd/4"}




print(root)
print(root.get('LugarExpedicion'))
print(root.get('Total'))
print(root.get('SubTotal'))
print(root.get('FormaPago'))

print(root.get('MetodoPago'))
print(root.get('Fecha'))
print("\r\n")

emisor = root.xpath('.//cfdi:Emisor', namespaces = namespace)[0]
print(emisor)
print("Nombre "+emisor.get('Nombre'))
print("Rfc "+emisor.get('Rfc'))

print("\r\n")
receptor = root.xpath('.//cfdi:Receptor', namespaces = namespace)[0]
print(receptor)
print("Nombre "+receptor.get('Nombre'))
print("Rfc "+receptor.get('Rfc'))

print("\r\n")
conceptos = root.xpath('.//cfdi:Conceptos/cfdi:Concepto', namespaces = namespace)
print(conceptos)
for concepto in conceptos:
    print(concepto.get('ClaveProdServ'))
    print(concepto.get('Descripcion'))
    print(concepto.get('Importe'))




