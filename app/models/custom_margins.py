from os import listdir
from select import select
from app import app
from pathlib import Path
import xml.etree.cElementTree as ET
from app.models.manage_xml import ManageXml

class CustomMargins(ManageXml):

    file_dir = Path(app.config['UPLOAD_FOLDER'], 'new', 'ppt', 'slideLayouts')
    tag1 = '{http://schemas.openxmlformats.org/presentationml/2006/main}cSld'
    tag2 = '{http://schemas.openxmlformats.org/presentationml/2006/main}spTree'
    tag3 = '{http://schemas.openxmlformats.org/presentationml/2006/main}sp'
    tag4 = '{http://schemas.openxmlformats.org/presentationml/2006/main}txBody'
    tag5 = '{http://schemas.openxmlformats.org/drawingml/2006/main}bodyPr'

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def set_margins(self):
        for file in super().collect_files(self.file_dir):
            tree = ET.parse(file)
            root = tree.getroot()
        
            all_bodyPr = root.findall(f'{self.tag1}/{self.tag2}/{self.tag3}/{self.tag4}/{self.tag5}')
        
            for elem in all_bodyPr:
                elem.set('lIns', str(self.left))
                elem.set('tIns', str(self.right))
                elem.set('rIns', str(self.top))
                elem.set('bIns', str(self.bottom))
            
            super().write_xml(tree, file)