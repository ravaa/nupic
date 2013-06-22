import sys, os, ConfigParser

conf = ConfigParser.ConfigParser()
with open('/nupic/predipic/console/settings.ini', 'r') as conf_file:
     conf.readfp(conf_file)

# set the source paths
sys.path.insert(0, conf.get('predipic', 'nta_home', 0))
sys.path.insert(0, conf.get('predipic', 'app_libs', 0))
sys.path.insert(0, conf.get('predipic', 'app_home', 0))

os.environ['DYLD_LIBRARY_PATH'] = conf.get('predipic', 'nta_home') + '/lib'
os.environ['LD_LIBRARY_PATH'] = conf.get('predipic', 'nta_home') + '/lib'
