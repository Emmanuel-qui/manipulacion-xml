from argparse import Namespace
from io import StringIO
import xml.etree.ElementTree as ET

from lxml import etree

# tree = ET.parse('CFDI40.xml')
# root = tree.getroot()

# obtenemos nuestro archivo XML.
path = "CFDI40.xml"

# Leemos nuestro archivo XML
xml_string = open(path, "rb").read()
root = etree.fromstring(xml_string)

# for item in root.iter():
#     print(item.tag, item.attrib)


#print(ET.tostring(root, encoding='utf8').decode('utf8'))

# for item in root.iter('{http://www.sat.gob.mx/cfd/4}Comprobante'):
#     print(item.tag, item.attrib)

namespace = {'cfdi':"http://www.sat.gob.mx/cfd/4"}
print(root)
print(root.get('Fecha'))

#emisor = root.find('cfdi:Emisor')
emisor = root.xpath('.//cfdi:Emisor', namespaces = namespace)[0]
print(emisor)
print(emisor.get("Rfc"))


conceptos = root.xpath('.//cfdi:Conceptos/cfdi:Concepto', namespaces = namespace)
print(conceptos)
for concepto in conceptos:
    print(concepto.get("Descripcion"))

print("*****************************************\r\n")

print(root.tag)

print("*****************************************\r\n")



