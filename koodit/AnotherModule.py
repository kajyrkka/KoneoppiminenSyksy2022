'''
And here we show how we can import from module.py
There are many ways to do it
1) One can just import whole module by name:                import module
2) Or one can import whole module but give it another name: import module as m
3) or one can import certain functions from module:         from module import subroutine1
4) and you can also give another name to that function:     from module import subroutine1 as sub1
'''

import module
module.subroutine1()
module.subroutine2()

import module as m
m.subroutine1()
m.subroutine2()

from module import subroutine1
subroutine1()


from module import subroutine1 as sub
sub()
