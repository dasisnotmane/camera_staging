import xml.etree.ElementTree as Et
import sys


def Et_xml_obj(xml_file):
   root = Et.parse(xml_file)
   return root.getroot()
def search_by_tag(tree_xml_obj,tag):

   #   print([appointment.tag for appointment in root.iterfind(".//appointment")])
   for element in tree_xml_obj.iter():
#       import pdb;pdb.set_trace()
       if element.tag == tag:
            print (element.tag,element.text)
            return element 
   print("tag was not found")

   return None
def edit_by_tag(element,value):
   
    element.text = value
    return element
#    pretty_xml = Et.tostring(x, pretty_print=True, encoding="unicode")
#    with open("appt2.xml","w") as f:
#        f.write(pretty_xml)

def write_tree_to_file(tree):

#    pretty_xml = Et.tostring(tree, pretty_print=True )
    with open("appt.xml", "w") as f : 
        f.write(tree)


#root = Et.parse('appt.xml')
#root_elem = root.getroot()


root = Et_xml_obj('appt.xml')
element = search_by_tag(root,"duration")
edit_by_tag(element,"2000")

root_string = Et.tostring(root,'utf-8')
print(root_string)

#et = Et.ElementTree(new_val)
#rint(et.write(sys.stdout,pretty_print=True))
#
write_tree_to_file(root_string )
#pretty_xml = Et.tostring(new_val, pretty_print=True )
#print(pretty_xml)

