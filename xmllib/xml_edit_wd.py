import editXML
editXML.edit_xml('./config_files/wdservice-module.xml','WD-upload_url','http://data.streetsoncloud.com/tcam/server/data')
editXML.edit_xml('./config_files/wdservice-module.xml','WD-alarm_url','http://data.streetsoncloud.com/tcam/server/setconfig')
editXML.edit_xml('./config_files/wdservice-module.xml','WD-event_url','http://data.streetsoncloud.com/tcam/server/event')
editXML.edit_xml('./config_files/wdservice-module.xml','WD-calibration_url','http://data.streetsoncloud.com/tcam/server/calibration')
