from lxml import etree

#----------------------------------------------------------------------
def createXML(filename):
    """
    Create an example XML file
    """
    root = etree.Element("zAppointments")
    appt = etree.Element("appointment")
    root.append(appt)
 
    # add appointment children
    begin = etree.SubElement(appt, "begin")
    begin.text = "1181251680"
 
    uid = etree.SubElement(appt, "uid")
    uid.text = "040000008200E000"
 
    alarmTime = etree.SubElement(appt, "alarmTime")
    alarmTime.text = "1181572063"
 
    state = etree.SubElement(appt, "state")
 
    location = etree.SubElement(appt, "location")
 
    duration = etree.SubElement(appt, "duration")
    duration.text = "1700"
 
    subject = etree.SubElement(appt, "subject")

    return root



def write_xml_to_file(xml_filename,xml_root):

    tree = etree.ElementTree(xml_root)
    with open(xml_filename, "wb") as fh:
        tree.write(fh)


def get_pretty_xml(xml_filename):

    x = etree.parse(xml_filename)
    #print(etree.tostring(x,pretty_print=True))
    pretty_xml = etree.tostring(x, pretty_print=True, encoding="unicode")
    return pretty_xml


def write_pretty_xml_to_file(pretty_xml,xml_filename):

    with open(xml_filename,"w") as f:
        f.write(pretty_xml)
 
#----------------------------------------------------------------------
if __name__ == "__main__":

    xml_filename = "appt.xml"

    xml_root = createXML(xml_filename )
    write_xml_to_file(xml_filename,xml_root)
    pretty_xml = pretty_xml(xml_filename)
    print(pretty_xml)
    write_pretty_xml_to_file(pretty_xml, xml_filename)


'''
    x = etree.parse("appt.xml")
    #print(etree.tostring(x,pretty_print=True))
    pretty_xml = etree.tostring(x, pretty_print=True, encoding="unicode")
    with open("appt.xml","w") as f:
        f.write(pretty_xml)
'''
