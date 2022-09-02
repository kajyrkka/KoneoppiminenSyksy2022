'''
This is a simple example how this module
can work as a main program or as a subroutine collection
'''

def subroutine1():
    print("This is subroutine 1 from module.py printing")


def subroutine2():
    print("This is subroutine 2 printing from module.py")


if __name__ == '__main__':
    # If these rows are executed, then
    # user started this file from command prompt like:
    # python module.py
    # And that initializes Python internal variable __name__ as __main__
    subroutine1()
    subroutine2()