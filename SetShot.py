#!~/conda3/bin/python
# -*- coding: cp949 -*-
#   Type     : Executable
#   Filename : SetShot.py
#   Author   : Jihyun Nam
#   Version  : 1.0
############################

import sys, os
from SetShotCore import SetShot

core = SetShot()

env_filename = '{}/{}'.format(os.getenv("HOME")
                     , ".envs")

env_json = '{}/{}'.format(os.getenv("HOME")
                     , "env.json")

show_json = '{}/{}'.format(os.getenv("HOME")
                     , "show.json")

 
if __name__ == "__main__":
    # Some    
    show = core.setData("Show", core.getShow(show_json))
    seq = core.setData("Sequence", core.getSeq(show_json, show))
    shot = core.setData("Shot", core.getShot(show_json, show, seq))
    core.exportShow(env_json, show, seq, shot)
    
    print("")
    print("")
    print("###############################")
    print("Shortcut: ", '{}:{}:{}'.format(show,seq,shot))
    print('{}'.format("Shot Setup Done!"))
    print("###############################")

