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
    manage_xml.remove_subtags(root, tag)
    manage_xml.add_main_tag(root, tag, 3)
    manage_xml.add_custom_color(root, tag, names, values)    
    manage_xml.write_xml(tree, file)