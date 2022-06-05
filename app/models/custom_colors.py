from app import app
from pathlib import Path
import xml.etree.cElementTree as ET
from app.models.manage_xml import ManageXml

class CustomColors(ManageXml):
    
    filepath = Path(app.config['UPLOAD_FOLDER'], 'new', 'ppt', 'theme', 'theme1.xml')
    custom_color_tag = '{http://schemas.openxmlformats.org/drawingml/2006/main}custClrLst'
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def set_colors(self):
        super().register_all_namespaces(self.filepath)
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        super().remove_subtags(root, self.custom_color_tag)
        super().add_main_tag(root, self.custom_color_tag, 3)
        color_list = root.find(self.custom_color_tag)
        for n, v in zip(self.name, self.value):
            color_name = ET.SubElement(color_list, 'a:custClr')
            color_value = ET.SubElement(color_name, 'a:srgbClr')
            color_name.set('name', n)
            color_value.set('val', v)
        super().write_xml(tree, self.filepath)