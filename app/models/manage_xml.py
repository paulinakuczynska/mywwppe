import xml.etree.cElementTree as ET

def register_all_namespaces(filename):
    namespaces = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
    for ns in namespaces:
        ET.register_namespace(ns, namespaces[ns])

def remove_subtags(root, tag):
    for element in root:
        if element.tag == tag:
            element.clear()

def add_main_tag(root, tag, position):
    if root.find(tag) is None:
        color_main_element = ET.Element(tag)
        root.insert(position, color_main_element)

def add_custom_color(root, tag, name, value):
    color_list = root.find(tag)
    for n, v in zip(name, value):
        color_name = ET.SubElement(color_list, 'a:custClr')
        color_value = ET.SubElement(color_name, 'a:srgbClr')
        color_name.set('name', n)
        color_value.set('val', v)

def write_xml(tree, filename):
    tree.write(
        filename,
        xml_declaration=True,
        encoding='utf-8',
        method='xml'
        )