import xml.dom.minidom
from xml_sax import XMLHandler
import xml.sax


def change_tag(xml_file, tag, new_tag, element=0):
    parsed_xml = xml.dom.minidom.parse(xml_file)
    collection = parsed_xml.documentElement
    _xml = collection.getElementsByTagName(tag)[element]
    _xml.tagName = new_tag

    with open(f"changed_{xml_file}", "wb") as f:
        f.write(collection.toxml("utf-8"))


if __name__ == '__main__':
    change_tag("sample_xml.xml", "food", "food2", 2)


