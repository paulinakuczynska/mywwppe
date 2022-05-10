from os import listdir
from app import app
from pathlib import Path
import xml.etree.cElementTree as ET
from app.models import manage_xml

file_dir = Path(app.config['UPLOAD_FOLDER'], 'new', 'ppt', 'slideLayouts')
tag1 = '{http://schemas.openxmlformats.org/presentationml/2006/main}cSld'
tag2 = '{http://schemas.openxmlformats.org/presentationml/2006/main}spTree'
tag3 = '{http://schemas.openxmlformats.org/presentationml/2006/main}sp'
tag4 = '{http://schemas.openxmlformats.org/presentationml/2006/main}txBody'
tag5 = '{http://schemas.openxmlformats.org/drawingml/2006/main}bodyPr'

def set_custom_margins(left, right, top, bottom):
    for file in listdir(file_dir):
        if not file.endswith('.xml'): continue
        fullname = file_dir / Path(file)
        tree = ET.parse(fullname)
        root = tree.getroot()
    
        all_bodyPr = root.findall(f'{tag1}/{tag2}/{tag3}/{tag4}/{tag5}')
    
        for elem in all_bodyPr:
            elem.set('lIns', str(left))
            elem.set('tIns', str(right))
            elem.set('rIns', str(top))
            elem.set('bIns', str(bottom))
        
        manage_xml.write_xml(tree, fullname)