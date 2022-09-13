
from xml.etree.ElementTree import XMLParser
from lxml import etree
from pathlib import Path
path = "cfdi.xml"

# Leer nuestro XML 
xml_string = open(path, "rb").read()

xsd_path = '/home/jquiroz/Documentos/entorno/script_xml/cfdv40.xsd'

xsd_file = Path(xsd_path)

if xsd_file.exists:
    xsd_string = xsd_file.read_bytes()
    xsd_string = xsd_string.decode()
    xsd_schema_root = etree.XML(xsd_string)
    xsd_schema = etree.XMLSchema(xsd_schema_root)
    xsd_parser = etree.XMLParser(schema = xsd_schema)
    root = etree.fromstring(xml_string, xsd_parser)
    print(root)




