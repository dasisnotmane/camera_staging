import re 
from os import fsync
import configs
import json 
#import wdconfig


########################## CAMERA OPTIONS ###############################
######################################################################### 

camera_options = {

        LeddarModel = None
        LensModel =  None 
        Lowcost_guardian =  None
        Enforcer =  None 
        Enforcer_Mobile = None
        wddata = None
        
        }

########################## DEFAULT SETTINGS #############################
######################################################################### 

filelocations = {

    "hostfile": './config_files/hostapd.conf',
    "gsmfile": './config_files/gsm.xml',
    "wdfile": './config_files/wdservice-module.xml',
    "cammodulefile" : './config_files/camera-module.xml',
    "leddarfile" : './config_files/leddar-module.xml',
    "lowcostfile" : './config_files/lowcost-camera.xml',
    "webfile" : './config_files/web.xml',
    "commonfile" : './config_files/common.xml'

    }
wdconfigs = {

    "WD-upload_url"  : "http://data.streetsoncloud.com/tcam/server/data",
    "WD-alarm_url"  : "http://data.streetsoncloud.com/tcam/server/setconfig",
    "WD-event_url"  : "http://data.streetsoncloud.com/tcam/server/event",
    "WD-calibration_url"  : "http://data.streetsoncloud.com/tcam/server/calibration",
    "GSM_Modem_SWReset" : 'true'
    }
gsm_configs = {

    "gsm_apn_provider" : "iot.aet.net"
    
    }

host_configs = {

    'ssid ' : None,
    'wpa_pairwise' : None,
    'wpa' : None,
    'wpa_passphrase' : None

    }

web_configs = {

        'WebMode' : None,
        'ShowFactorySettings': None,
        'EnforcerMobileVisible': None,
        'EnforcerMobileEnabled': None

    }
leddar_configs = {

    'LeddarModel' : None

    }
camera_configs = {
  
    'FocalLength' : '16.7'

    }
lowcostcam_configs = {
   
    'min_radar_trigger_signal' : '150',
    'units' : 'km/h'

    }


######################################################################### 
######################################################################### 

class camera (): 


    def __init__():
        self.LeddarModel  = None
        self.LensModel   = None 
        self.Lowcost_guardian   = None
        self.Enforcer   = None 
        self.Enforcer_Mobile  = None
        self.wddata  = None
    def update () : 
    
def config_update(filename,dico):

    RE = '^((^''|'.join(dico.keys())+')\s*=)[^\r\n]*?(\r?\n|\r)'
    pat = re.compile(RE,flags=re.MULTILINE)
    
    #This is a helper function that is used with regex sub()
    # wherenever a match occurs , this function is called
    # to substitute the string match 
    def jojo(match,dic = dico ):
        return dic[match.group(2)].join(match.group(1,3))

    with open(filename,'r') as f:
        content = f.read() 

    with open(filename,'w') as f:
        f.write(pat.sub(jojo,content))

def xml_edit_gsm(filename,dico):

    RE = '(<(gsm_apn_provider).*?>)(.*?)(<.*>)'
    pat = re.compile(RE,flags=re.MULTILINE)

    def sub(match,dic = dico):
        return dic[match.group(2)].join(match.group(1,4))
    with open(filename,'r') as f : 
        content = f.read()
    with open(filename,'w') as f:
#        import pdb; pdb.set_trace()
        f.write(pat.sub(sub,content))

def xml_edit_wd(filename,dico):

    RE_all = '(<(WD-upload_url|WD-alarm_url|WD-event_url|WD-calibration_url).*?>)(.*?)(<.*>)'
    pat_all = re.compile(RE_all ,flags=re.MULTILINE)

    with open(filename,'r') as f : 
        content = f.read()
    def sub(match,dic = dico):
        print(dic[match.group(2)].join(match.group(1,4)))
        return dic[match.group(2)].join(match.group(1,4))

    with open(filename,'w') as f : 
        f.write(pat_all.sub(sub,content))

def xml_edit_cam(filename,dico):

    RE_all = '(<(FocalLength).*?>)(.*?)(<.*>)'
    pat_all = re.compile(RE_all ,flags=re.MULTILINE)

    with open(filename,'r') as f : 
        content = f.read()
    def sub(match,dic = dico):
        print(dic[match.group(2)].join(match.group(1,4)))
        return dic[match.group(2)].join(match.group(1,4))

    with open(filename,'w') as f : 
        f.write(pat_all.sub(sub,content))

def xml_lowcost_cam(filename,dico):

    RE_all = '(<(min_radar_trigger_signal|units).*?>)(.*?)(<.*>)'
    pat_all = re.compile(RE_all ,flags=re.MULTILINE)

    with open(filename,'r') as f : 
        content = f.read()
    def sub(match,dic = dico):
        print(dic[match.group(2)].join(match.group(1,4)))
        return dic[match.group(2)].join(match.group(1,4))

    with open(filename,'w') as f : 
        f.write(pat_all.sub(sub,content))

def xml_edit_lowcostcam(filename,dico):

    RE_all = '(<(min_radar_trigger_signal|units).*?>)(.*?)(<.*>)'
    pat_all = re.compile(RE_all ,flags=re.MULTILINE)

    with open(filename,'r') as f : 
        content = f.read()
    def sub(match,dic = dico):
        print(dic[match.group(2)].join(match.group(1,4)))
        return dic[match.group(2)].join(match.group(1,4))

    with open(filename,'w') as f : 
        f.write(pat_all.sub(sub,content))

def xml_edit_leddar(filename,dico):

    RE_all = '(<(LeddarModel).*?>)(.*?)(<.*>)'
    pat_all = re.compile(RE_all ,flags=re.MULTILINE)

    

    with open(filename,'r') as f : 
        content = f.read()
    def sub(match,dic = dico):
        print(dic[match.group(2)].join(match.group(1,4)))
        return dic[match.group(2)].join(match.group(1,4))

    with open(filename,'w') as f : 
        f.write(pat_all.sub(sub,content))

def xml_edit_web(filename,dico):

    RE_all = '(<(WebMode|ShowFactorySettings|)EnforcerMobileVisible|EnforcerMobileEnabled.*?>)(.*?)(<.*>)'
    pat_all = re.compile(RE_all ,flags=re.MULTILINE)

    with open(filename,'r') as f : 
        content = f.read()
    def sub(match,dic = dico):
        print(dic[match.group(2)].join(match.group(1,4)))
        return dic[match.group(2)].join(match.group(1,4))

    with open(filename,'w') as f : 
        f.write(pat_all.sub(sub,content))




#wdconfig_dict = eval(open('wdconfig').read())  
#print(wdconfig_dict)

xml_edit_wd(filelocations['wdfile'],wdconfigs)
xml_edit_cam(filelocations['cammodulefile'],camera_configs)
xml_edit_lowcostcam(filelocations['lowcostfile'],lowcostcam_configs)
xml_edit_gsm(filelocations['gsmfile'],gsm_configs)
#xml_edit_leddar(filelocations['leddarfile'],leddar_configs )
#xml_edit_web(filelocations['webfile'],web_configs )


'''
config_variables = ['ssid','wpa_pairwise','wpa','wpa_passphrase']
config_values = ['SP_CAM_DF9C','CCMP','2','Password-TLDF9C-#!']
what_to_change = dict(zip(config_variables,config_values))

config_update(configs.hostfile,what_to_change)
'''
'''
gsm_configs = ['gsm_apn_provider']
gsm_values = ['iot.aer.net']
gsm_dic = dict(zip(gsm_configs,gsm_values))

xml_edit_gsm(configs.gsmfile,gsm_dic)


gsm_values = ['iot.aer.net']
gsm_dic = dict(zip(gsm_configs,gsm_values))

xml_edit_gsm(configs.gsmfile,gsm_dic)
'
