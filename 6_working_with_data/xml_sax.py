import xml.sax


class XMLHandler(xml.sax.ContentHandler):

    """
    Class that parses XML to a nice format to display
    """

    def __init__(self):
        self.current = ""
        self.name = ""
        self.price = ""
        self.description = ""
        self.calories = ""

    def startElement(self, name, attrs):
        self.current = name
        if name == "food":
            num = int(attrs['id'])
            print(f"\n{num} breakfast: ")

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "price":
            self.price = content
        elif self.current == "description":
            self.description = content
        elif self.current == "calories":
            self.calories = content

    def endElement(self, attrs):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "price":
            print(f"Price: {self.price}")
        elif self.current == "description":
            print(f"Description: {self.description}")
        elif self.current == "calories":
            print(f"Calories: {self.calories}")
        self.current = ""


if __name__ == "__main__":
    # basic parser for xml sax
    parser = xml.sax.make_parser()
    # make object of our own xml handler
    xml_handler = XMLHandler()
    # set content handler for xml.sax parser, giving our XMLHandler class
    parser.setContentHandler(xml_handler)
    parser.parse("sample_xml.xml")
