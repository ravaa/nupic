import sys, os, ConfigParser

conf = ConfigParser.ConfigParser()
with open('/nupic/predipic/console/settings.ini', 'r') as conf_file:
     conf.readfp(conf_file)

# envvars
os.environ['DYLD_LIBRARY_PATH'] =  '/home/vagrant/nta/eng/lib'
os.environ['LD_LIBRARY_PATH'] = '/home/vagrant/nta/eng/lib'
os.environ['NTA'] = '/home/vagrant/nta/eng'
os.environ['NTA_ROOTDIR'] = '/home/vagrant/nta/eng'
os.environ['NUPIC'] = '/nupic'
os.environ['NTA_BUILDDIR'] = '/tmp/nupic'

# set the source paths
sys.path.insert(0, os.path.abspath('/home/vagrant/nta/eng/lib/python2.6/site-packages/'))
sys.path.insert(0, os.path.abspath('/home/vagrant/nta/eng/lib/'))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from senz0rs import app as application
