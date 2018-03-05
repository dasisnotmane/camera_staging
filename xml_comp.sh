xmllint --c14n ../camera_staging/camera/wdservice-module.xml  > 2.xml
xmllint --c14n ./config_files/wdservice-module.xml > 1.xml
diff 1.xml 2.xml
rm 1.xml ; rm 2.xml

