import re 
from os import fsync
import configs

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

config_variables = ['ssid','wpa_pairwise','wpa','wpa_passphrase']
config_values = ['SP_CAM_DF9C','CCMP','2','Password-TLDF9C-#!']
what_to_change = dict(zip(config_variables,config_values))

config_update(configs.hostfile,what_to_change)
