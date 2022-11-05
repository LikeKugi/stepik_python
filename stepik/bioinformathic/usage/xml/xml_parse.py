from xml.etree.ElementTree import XMLParser


class MaxDepth:  # The target object of the parser
    maxDepth = 0
    depth = 0
    cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
        print(attrib)
        print(self.depth)
        self.cubes[attrib.get('color')] += self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self):
        print(self.cubes.get('red'), self.cubes.get('green'), self.cubes.get('blue'))  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return self.maxDepth


target = MaxDepth()
parser = XMLParser(target=target)
exampleXml = input()
parser.feed(exampleXml)
parser.close()
target.data()
