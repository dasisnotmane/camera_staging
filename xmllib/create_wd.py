import xml.etree.ElementTree as Et
from subprocess import Popen


file_location = "./config_files/wdservice-module.xml.bak"
et = Et.parse(file_location)
root = et.getroot()
xml_string = Et.tostring(root,encoding="US-ASCII",method='xml')

xml_declaration = '<?xml version="1.0"?>\n'
new_xml = xml_declaration + xml_string
print(new_xml)
#editXML.edit_xml("./config_files/gsm.xml","WD-upload_url","http://data.streetsoncloud.com/tcam/server/data")
'''
for element in root:
#    print(element.tag,element.text)
    if "WD" and "url" in element.tag: 
        print("editXML.edit_xml('{}','{}','{}')".format(file_location,element.tag,element.text))
'''
