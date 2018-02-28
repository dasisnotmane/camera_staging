
#! /usr/bin/env

from configobj import ConfigObj

file = ConfigObj("/etc/camera/gsm.xml")

file["gsm_apn_provider"] = "aer.aerisapn.net"
#file["PPP-Backup"] = "true"

file.write()
apn = file["gsm_apn_provider"] 
#ppp = file["PPP-Backup"] 

print("apn: {}".format(apn)}

