from FunctionMapper import *

fm = FunctionMapper()

print len(fm.configMap)
print len(fm.funcMap)

fm.map('a', 'func')
fm.execFunc('a')
fm.execFunc('a', 'hello')
fm.execFunc('a', [0, 1, 2])

fm.saveYAMLFile('test.yaml')
fm = FunctionMapper('test.yaml')
print len(fm.configMap)
print len(fm.funcMap)
