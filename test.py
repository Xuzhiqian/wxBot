#!/usr/bin/env python
# coding: utf-8
#

import threading

def f():
    print("haha")
    global timer
    timer = threading.Timer(5,f)
    timer.start()
    
def main():
    timer = threading.Timer(5,f)
    timer.start()
    print("immi!")


if __name__ == '__main__':
    main()
