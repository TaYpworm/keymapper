#!/usr/bin/python

import threading
from BufferedThread import BufferedThread
from FunctionMapper import FunctionMapper
from MapThread import MapThread
from optparse import OptionParser
from UnbufferedThread import UnbufferedThread


parser = OptionParser()
parser.add_option("-c", "--config", 
        dest="configfile", 
        default="default.yaml",
        action="store",
        help="Load config file in YAML format", 
        metavar="FILE")
parser.add_option("-m", "--map", 
        dest="map",
        action="store_true",
        default=False,
        help="Enable mapping mode")
parser.add_option("-b", "--buffer", 
        dest="buffer", 
        action="store_true",
        default=False,
        help="Enable buffered input mode")

(options, args) = parser.parse_args()

if options.configfile is None and options.map is False:
    raise Exception, "You must specify a configuration file in YAML format"

if options.map is True:
    MapThread(options.configfile).start()
elif options.buffer is True:
    fm = FunctionMapper(options.configfile)
    BufferedThread(fm).start()
else:
    fm = FunctionMapper(options.configfile)
    UnbufferedThread(fm).start() 

