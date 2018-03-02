from lxml import etree
import xml.etree.ElementTree as Et
from xml.dom import minidom 


#----------------------------------------------------------------------
def createXML(filename):
    """
    Create an example XML file
    """
    root = Et.Element("zAppointments")
    appt = Et.Element("appointment")
    root.append(appt)
 
    # add appointment children
    begin = Et.SubElement(appt, "begin")
    begin.text = "1181251680"
 
    uid = Et.SubElement(appt, "uid")
    uid.text = "040000008200E000"
 
    alarmTime = Et.SubElement(appt, "alarmTime")
    alarmTime.text = "1181572063"
 
    state = Et.SubElement(appt, "state")
 
    location = Et.SubElement(appt, "location")
 
    duration = Et.SubElement(appt, "duration")
    duration.text = "1700"
 
    subject = Et.SubElement(appt, "subject")

    return root



def write_xml_to_file(xml_filename,xml_root):

    tree = Et.ElementTree(xml_root)
    with open(xml_filename, "wb") as fh:
        tree.write(fh)


def get_pretty_xml(xml_filename):


    x = Et.parse(xml_filename)
    root_element = x.getroot()
    xml_string = Et.tostring(root_element,'utf-8')
    reparsed_string = minidom.parseString(xml_string)
    return reparsed_string.toprettyxml(indent="  ")


    #print(etree.tostring(x,pretty_print=True))
#    pretty_xml = Et.tostring(x, pretty_print=True, encoding="unicode")
#    return pretty_xml


def write_pretty_xml_to_file(pretty_xml,xml_filename):

    with open(xml_filename,"w") as f:
        f.write(pretty_xml)
 
#----------------------------------------------------------------------
if __name__ == "__main__":

    xml_filename = "appt.xml"

    xml_root = createXML(xml_filename )
    write_xml_to_file(xml_filename,xml_root)
    pretty_xml = get_pretty_xml(xml_filename)
    print(pretty_xml)
    write_pretty_xml_to_file(pretty_xml, xml_filename)


'''
    x = etree.parse("appt.xml")
    #print(etree.tostring(x,pretty_print=True))
    pretty_xml = etree.tostring(x, pretty_print=True, encoding="unicode")
    with open("appt.xml","w") as f:
        f.write(pretty_xml)
'''
