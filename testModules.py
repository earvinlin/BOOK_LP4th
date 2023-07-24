import sys
import os
from ch20 import myTimer as mt
from ch20 import myTimer2 as mt2
from ch20 import timeseqs as ts

def testFun(n) :
    i = 0
    j = range(n)
    for i in range(n) :
        i+= i
#        print(i)
    return i

mt.reps = 10000
mt.repslist = range(mt.reps)
print(mt.timer(testFun, 100))

# ============================== #

print(sys.version)
for test in (ts.forLoop, ts.listComp, ts.mapCall, ts.genExpr, ts.genFunc) :
    elapsed, result = mt.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s ... %s]' % (test.__name__, elapsed, result[0], result[-1]))

# ============================== #

print("=== timer2 ===")
for test in (ts.forLoop, ts.listComp, ts.mapCall, ts.genExpr, ts.genFunc) :
    elapsed, result = mt2.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s ... %s]' % (test.__name__, elapsed, result[0], result[-1]))
