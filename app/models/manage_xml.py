import xml.etree.cElementTree as ET
from os import listdir
from pathlib import Path

class ManageXml:

    def register_all_namespaces(self, filename):
        namespaces = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
        for ns in namespaces:
            ET.register_namespace(ns, namespaces[ns])

    def remove_subtags(self, root, tag):
        for element in root:
            if element.tag == tag:
                element.clear()

    def add_main_tag(self, root, tag, position):
        if root.find(tag) is None:
            color_main_element = ET.Element(tag)
            root.insert(position, color_main_element)
    
    def collect_files(self, directory):
        files_list = []
        for file in listdir(directory):
            if not file.endswith('.xml'): continue
            files_list.append(directory / Path(file))
        return files_list

    def write_xml(self, tree, filename):
        tree.write(
            filename,
            xml_declaration=True,
            encoding='utf-8',
            method='xml'
            )