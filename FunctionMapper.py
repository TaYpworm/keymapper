import yaml
import ThreadPool
import pprint

class FunctionMapper(object):

    
    def __init__(self, filename=None):
        self.configMap = {}
        self.funcMap = {}
        self.pp = pprint.PrettyPrinter(indent=4)
        #self.pool = ThreadPool.ThreadPool(3)

        if filename is not None:
            self.loadYAMLFile(filename)


    #def __del__(self):
    #    self.shutdown()

    
    #def shutdown(self):
    #    self.pool.joinAll()
    
    
    def map(self, key, func):
        try:
            self.funcMap[key] = self.dynLoadModule(func)
            self.configMap[key] = func
        except ImportError:
            raise

    
    def dynLoadModule(self, func):
        try:
            exec "from %s import %s as fn" %(func, func)
        except ImportError:
            raise ImportError, 'Transfer function %s does not exist' %func
	return fn


    def loadYAMLFile(self, filename):
        try:
            fin = open(filename, 'r')
            self.configMap = yaml.load(fin)
            fin.close()

            for k, v in self.configMap.iteritems():
                self.funcMap[k] = self.dynLoadModule(v)

        except IOError:
            raise IOError, 'YAML file %s does not exist' %filename

    
    def saveYAMLFile(self, filename):
        try:
            fout = open(filename, 'w')
            yaml.dump(self.configMap, fout)
            fout.close()

        except IOError:
            raise IOError, 'Saving YAML file failed'


    def execFunc(self, key, param=None):
        if self.funcMap.has_key(key):
            self.funcMap[key](param)
        #else:
        #    print 'Key %s is not bound' %key

    
    def printMap(self):
        self.pp.pprint(self.configMap)


