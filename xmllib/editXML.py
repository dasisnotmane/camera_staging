import xml.etree.ElementTree as Et
import sys
import logging 

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
#logger.debug('debug message')
#logger.info('info message')
#logger.warn('warn message')
#logger.error('error message')
#logger.critical('critical message')



#takes a xml file and returns a tree obj
def Et_xml_obj(xml_file):
   logger.info("Parsing xml file into...")
   root = Et.parse(xml_file)
   return root.getroot()

# takes a tree obj and xml tag 
# looks if that tag is present in the xml tree 

def search_by_tag(tree_xml_obj,tag):

   logger.info("finding tag...")
   for element in tree_xml_obj.iter():
           if element.tag == tag:
                logger.info("found tag...returning tag")
                logger.debug("tag: {} -- value: {}".format(element.tag,element.text))
                return element 

   logger.error("tag was not found")
   raise ValueError("{} is not a valid tag ".format(tag)) 
   return None

# using the specific tree element 
# edit that value for that element
def edit_by_tag(element,value):
   
    logger.info("editing value of element...")
    element.text = value
    logger.debug("tag: {} -- new_value: {}".format(element.tag,element.text))
    logger.info("done editing value...")
    return element

# write the string to the file 
def write_tree_to_file(xml_file,tree_str):

    logger.info("writing tree string to file...")
    try: 
        with open(xml_file, "wb") as f : 
#            import pdb; pdb.set_trace()
            f.write(tree_str)
        logger.debug("SUCCESS") 

    except Exception as e  : 
        logger.debug("failed to edit,,,{}".format(xml_file))
        sys.strout.write(e)
    
    logger.info("done writting to file...")

#takes a xml file , tag and value 
#edit the file and rewrite it  
def edit_xml(xml_file,tag,value):
    logger.info("begin editing file...")
    root = Et_xml_obj(xml_file)
    element = search_by_tag(root,tag)
    edit_by_tag(element,value)

    root_string = Et.tostring(root,encoding='utf8')
    logger.debug("{}....editing..{} to {}".format(xml_file,tag,value) )
    write_tree_to_file(xml_file,root_string )
    logger.info("done editing file...")

    
edit_xml("./config_files/gsm.xml","gsm_apn_provider","shit")
'''
root = Et_xml_obj('appt.xml')
element = search_by_tag(root,"duration")
edit_by_tag(element,"2000")

root_string = Et.tostring(root,'utf-8')
print(root_string)

write_tree_to_file(root_string )
'''
