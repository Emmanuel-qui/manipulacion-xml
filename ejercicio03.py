from pathlib import Path
from lxml import etree

path = "cfdi.xml"

# Leer nuestro XML 
xml_string = open(path, "rb").read()



BASE_DIR = Path(__file__).resolve().parent.parent


XSD_PATH = str(Path(BASE_DIR, '/home/jquiroz/Documentos/entorno/script_xml/'))
INVOICE_XSD_NAME = '/home/jquiroz/Documentos/entorno/script_xml/cfdv40.xsd'
INVOICE_XSD_FILE = Path(BASE_DIR, INVOICE_XSD_NAME)
if INVOICE_XSD_FILE.exists():
    INVOICE_XSD_STRING = INVOICE_XSD_FILE.read_bytes()
    INVOICE_XSD_STRING = INVOICE_XSD_STRING.decode()
    INVOICE_XSD_SCHEMA_ROOT = etree.XML(INVOICE_XSD_STRING)
    INVOICE_XSD_SCHEMA = etree.XMLSchema(INVOICE_XSD_SCHEMA_ROOT)
    INVOICE_XSD_PARSER = etree.XMLParser(schema=INVOICE_XSD_SCHEMA)
root = etree.fromstring(xml_string, INVOICE_XSD_PARSER)

