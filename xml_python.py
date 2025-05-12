import xml.etree.cElementTree as ET

xml_data = """
<person>
    <name> John Doe </name>
</person>
"""

root = ET.fromstring(xml_data)
print ("user_name:", root.find('name').text)