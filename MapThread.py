import readline
import threading
from FunctionMapper import FunctionMapper


class MapThread(threading.Thread):
    
    def __init__(self, filename):
        self.filename = filename
        try:
            self.fm = FunctionMapper(self.filename)
        except IOError:
            self.fm = FunctionMapper()
        threading.Thread.__init__(self)


    def run(self):
        print '''\nTo map a string to a function input the string\nand function name in the format <String> : <Function>\nthen press enter.  Please input only one mapping per line.\nTo exit terminate the interpreter (Ctrl+D).\n\n'''

        while True:
            print "Map: ",
            self.fm.printMap()
            try:
                str = raw_input("INPUT >> ").split(':', 1)
                if len(str) != 2:
                    print "Input parse error.  Please try again."
                else:
                    str = [s.strip(' ') for s in str]
                    try:
                        self.fm.map(str[0], str[1])
                    except ImportError:
                        print "Module does not exist.  Please check spelling and case."
            except EOFError:
                self.fm.saveYAMLFile(self.filename)
                print "\n"
                break


