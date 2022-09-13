import xml.etree.ElementTree as ET


tree = ET.parse('archivo.xml')
root = tree.getroot()

# iterando en los nodos.

# tag se refiere al nodo y attrib se refiere al atributo de ese nodo.
for item in root:
    print(item.tag, item.attrib)


print(root[2][2].text)

# permite iterar el contenido de un subarbol mostrando los atributos de ese subarbol.
for item in root.iter('country'):
    print(item.attrib)


# Element.findall()encuentra solo elementos con una etiqueta que son hijos directos del elemento actual. Element.find()encuentra el primer hijo con una etiqueta particular y Element.textaccede al contenido de texto del elemento. Element.get()accede a los atributos del elemento
for item in root.findall('country'):
    rank = item.find('rank').text
    name = item.get('name')
    print(name, rank)