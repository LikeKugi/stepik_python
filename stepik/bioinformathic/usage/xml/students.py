from xml.etree import ElementTree

tree = ElementTree.parse('students.xml')
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

for child in root:
    print(child.tag, child.attrib)


print(root[0][0].text)

for el in root.iter('scores'):
    print(el)
    score_sum = 0
    for ch in el:
        score_sum += float(ch.text)
    print(score_sum)

tree.write('students_copy.xml')