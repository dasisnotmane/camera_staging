import pytest
#from configobj import ConfigObj
import os 
from createXML import * 
from editXML import * 
import lxml
from lxml import etree


'''
@pytest.fixture(scope="function")
def configuration(tmpdir_factory):
# change form tmpdir to tmpdir_factory

    # create a temp directory 
    xml_filename = "test.xml"

    test_dir = tmpdir_factory.mktemp("testdir")
    test_config = test_dir.join(xml_filename)

    xml_root = createXML(xml_filename )
    write_xml_to_file(xml_filename,xml_root)
    pretty_xml = get_pretty_xml(xml_filename)
    
    test_config.write(pretty_xml)

    test_dir = tmpdir.mkdir("testdir")
    test_config = test_dir.join(xml_filename)

    xml_root = createXML(xml_filename )
    write_xml_to_file(xml_filename,xml_root)
    pretty_xml = get_pretty_xml(xml_filename)
    
    test_config.write(pretty_xml)
    return test_config
    # create a temp test config file
'''

@pytest.fixture(scope="function")
def test_xml_file(tmpdir_factory):


    xml_filename = "test.xml"

    test_dir = tmpdir_factory.mktemp("testdir")
    test_config = test_dir.join(xml_filename)


    xml_root = createXML(xml_filename )
    write_xml_to_file(xml_filename,xml_root)
    pretty_xml = get_pretty_xml(xml_filename)
    
    test_config.write(pretty_xml)

    return test_config 





def test_search_by_tag_success(test_xml_file):

# create functions to create files for our tmpdir fixture (configuration)
# which should be returning a tmpdir 



#    xml_file = test_xml_file.read() 
#    import pdb; pdb.set_trace()

    xml_file = os.path.basename(test_xml_file.strpath) 
    print(xml_file,"xml_file")
    assert search_by_tag(xml_file,"duration") != None

    #search_result = search_by_tag(xml_file,tag)
   # assert  search_result != None


# pass in the test_config_env 
def test_change_xml_config(test_xml_file):

    # open the file 
#    file = ConfigObj("/home/mclaptop/python_projects/raspi/tests/file/int")
#    import pdb;pdb.set_trace()
    assert True == True
#    assert address == "192.168.1.133"  
    
    # change the config 
    # write the changes 
    # assert that the value was changed properly by inspecting that
    # line specifically not just throught he library 


