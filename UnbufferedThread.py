import curses
import threading
from FunctionMapper import FunctionMapper


class _GetchUnix:
    
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        oldSettings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)
        return ch

getch = _GetchUnix()


class UnbufferedThread(threading.Thread):
    
    def __init__(self, funcMap):
        self.fm = funcMap
        threading.Thread.__init__(self)

    
    def run(self):
        self.fm.printMap()
        print "\nPress 'q' to exit\n"
        while True:
            c = getch()
            if c == 'q':
                break
            self.fm.execFunc(c)
