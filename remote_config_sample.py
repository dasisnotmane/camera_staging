
#! /usr/bin/env

import xml.etree.ElementTree 

et = xml.etree.ElementTree.parse('/mnt/c/work/camera/camera_staging/config_files/gsm.xml')
root = et.getroot()
for element in root:
#    if element.tag == tag:
         print (element.tag,element.text)






