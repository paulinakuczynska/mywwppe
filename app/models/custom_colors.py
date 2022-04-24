from app import app
from pathlib import Path
import xml.etree.cElementTree as ET
from app.models import manage_xml

file = Path(app.config['UPLOAD_FOLDER'], 'new', 'ppt', 'theme', 'theme1.xml')
tag = '{http://schemas.openxmlformats.org/drawingml/2006/main}custClrLst'

def set_custom_colors(names, values):
    manage_xml.register_all_namespaces(file)
    tree = ET.parse(file)
    root = tree.getroot()

    for element in root:
        if element.tag == tag:
            element.clear()
    if root.find(tag) is None:
        color_main_element = ET.Element(tag)
        root.insert(3, color_main_element)

    color_list = root.find(tag)
    for n, v in zip(names, values):
        color_name = ET.SubElement(color_list, 'a:custClr')
        color_value = ET.SubElement(color_name, 'a:srgbClr')
        color_name.set('name', n)
        color_value.set('val', v)

    tree.write(file,
            xml_declaration=True,
            encoding='utf-8',
            method='xml')