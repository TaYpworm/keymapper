import readline
import threading
#from FunctionMapper import FunctionMapper


class BufferedThread(threading.Thread):

    def __init__(self, funcMap):
        self.fm = funcMap
        threading.Thread.__init__(self)

    
    def run(self):
        self.fm.printMap()
        print "\nInput 'exit' to quit\n"

        while True:
            str = raw_input(">> ")
            self.fm.execFunc(str)
            if str == 'exit':
                break

