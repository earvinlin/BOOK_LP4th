import sys
import os
from ch20 import myTimer as mt
from ch20 import myTimer2 as mt2
from ch20 import timeseqs as ts
from ch20 import inter2 as in2

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
"""
print(sys.version)
for test in (ts.forLoop, ts.listComp, ts.mapCall, ts.genExpr, ts.genFunc) :
    elapsed, result = mt.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s ... %s]' % (test.__name__, elapsed, result[0], result[-1]))
"""
# ============================== #
"""
print("=== timer2 ===")
for test in (ts.forLoop, ts.listComp, ts.mapCall, ts.genExpr, ts.genFunc) :
    elapsed, result = mt2.timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s ... %s]' % (test.__name__, elapsed, result[0], result[-1]))
"""
# (20230726) =================== #
"""
def func(*pargs) :
    print(pargs)

# return a tuple
func(*open('stockslist.txt'))

L = [1,2,3,4,5]
func(L)

D = {'a' : 1, 'b' : 2, 'c' : 3}
func(D)
"""

"""
inputfile = open('stockslist.txt')
for line in inputfile :
    print(line)
"""

"""
def func2(a, b=2, c=3, *d) :
    print(a,b,c,d)

# *vars : 會自動解包以對應呼叫函數的參數
func2(*L)

func2(*open('stockslist.txt'))


def func3(a, b, c, d) : print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func3(*args)
"""

#
"""
def func5(a, *b, **c) : print(a, b, c)

L = [1,2,3,4]
func5(func2(*L), L)
"""

# python學習手冊4th(中文版) p.465~p.466
L = ['a', 'b', 'c', 'z', 'h', 'a', 'i', 'b']
L = 'abcdegsah'
L1 = 'abdfeig'
L2 = 'dfeadfg'
L3 = 'opqij'
args = (L1,L2,L3)

R = in2.intersect(*args)
print(R)
#=======
R2 = in2.intersect(L1, L3)
print(R2)