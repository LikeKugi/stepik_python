from xml.etree import ElementTree

tree = ElementTree.parse('students_copy_modified.xml')
root = tree.getroot()
greg = root[0]


def modify_module():
    module1 = next(greg.iter('module1'))
    print(module1, module1.text)

    module1.text = str(float(module1.text) + 30)

    tree.write('students_copy_modified.xml')


def modify_certificate():
    certificate = greg[2]
    certificate.set('type', 'with distinction')

    tree.write('students_copy_modified.xml')


def create_element():
    description = ElementTree.Element('description')
    description.text = 'Showed excellent skills during the course'
    greg.append(description)

    tree.write('students_copy_modified.xml')


def remove_element():
    description = greg.find('description')
    greg.remove(description)

    tree.write('students_copy_modified.xml')

remove_element()