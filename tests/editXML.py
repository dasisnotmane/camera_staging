from lxml import etree
import sys



def etree_xml_obj(xml_file):
   root = etree.parse(xml_file)
   return root

def search_by_tag(xml_file,tag):
    
   root = etree_xml_obj(xml_file)
   #   print([appointment.tag for appointment in root.iterfind(".//appointment")])
   for element in root.getiterator():
       if element.tag == tag:
            print (element.tag,element.text)
            return element 

def edit_by_tag(element,value):
    
    element.text = value
    return element.getroottree()
#    pretty_xml = etree.tostring(x, pretty_print=True, encoding="unicode")
#    with open("appt2.xml","w") as f:
#        f.write(pretty_xml)

def write_tree_to_file(tree):

    pretty_xml = etree.tostring(tree, pretty_print=True )
    with open("appt.xml", "w") as f : 
        f.write(pretty_xml)


element = search_by_tag("appt.xml","duration")
new_val = edit_by_tag(element,"2000")


#et = etree.ElementTree(new_val)
#rint(et.write(sys.stdout,pretty_print=True))
#
write_tree_to_file(new_val)
pretty_xml = etree.tostring(new_val, pretty_print=True )
print(pretty_xml)

