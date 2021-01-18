# =============================================================================
# IMPORTS
# =============================================================================

import os, subprocess, sys, json
from SetShotCore import SetShot

Ss = SetShot()


# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================
def hou(ver="18.5.408"):
    houdini = 'C:/Program Files/Side Effects Software/Houdini 18.5.408/bin/houdini.exe'
    houdini = 'C:/Program Files/Side Effects Software/Houdini {}/bin/houdini.exe'.format(ver)
    return houdini

#os.environ['HOME'] = '{}'.format("J:/HOU")

env_json = '{}/{}'.format(os.getenv("HOME")
                     , "env.json")

# TODO
os.environ['PROJ'] = '{}'.format("//fx8/hq/proj")
os.environ['SHOW'] = '{}'.format(Ss.loadJson(env_json)["envs"][0])
os.environ['SEQ'] = '{}'.format(Ss.loadJson(env_json)["envs"][1])
os.environ['SHOT'] = '{}'.format(Ss.loadJson(env_json)["envs"][2])

# =============================================================================
# ARNOLD ENVIRONMENT SETUP
# =============================================================================
os.environ['PATH'] = '$PATH;{}'.format("C:/htoa/htoa-5.0.1_r5e954ab_houdini-18.0.287/htoa-5.0.1_r5e954ab_houdini-18.0.287/scripts/bin")
os.environ['HOUDINI_PATH'] = '{};&'.format("C:/htoa/htoa-5.0.1_r5e954ab_houdini-18.0.287/htoa-5.0.1_r5e954ab_houdini-18.0.287")

# =============================================================================
# EXECUTE
# =============================================================================

if __name__ == "__main__":
    
    # Run Houdini
    ver = Ss.selHou("Run Houdini", ["18.5.351", "18.5.408"])
    subprocess.Popen(hou(ver))

