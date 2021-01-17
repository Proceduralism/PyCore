# Wrapper to run Houdini with custom environment
import os, subprocess, sys, json

#sys.path.append("C:/Program Files/Side Effects Software/Houdini 18.0.287/houdini/python2.7libs")

houdini = 'C:/Program Files/Side Effects Software/Houdini 18.5.351/bin/houdini.exe'

os.environ['HOME'] = '{}'.format("J:/HOU")

def loadJson(json_file):
    with open(json_file) as data_file:
        data = json.load(data_file)
        #data = [s.encode('utf-8') for s in data_file]        
    return data

env_json = '{}/{}'.format(os.getenv("HOME")
                     , "env.json")


#os.environ['HOUDINI_OTLSCAN_PATH'] = '{}'.format("J:/HOU/houdini18.5/packages/Pype\otls")


os.environ['PROJ'] = '{}'.format("//fx8/hq/proj")
os.environ['SHOW'] = '{}'.format(loadJson(env_json)["envs"][0])
os.environ['SEQ'] = '{}'.format(loadJson(env_json)["envs"][1])
os.environ['SHOT'] = '{}'.format(loadJson(env_json)["envs"][2])

# Add Arnold to Path
os.environ['PATH'] = '$PATH;{}'.format("C:/htoa/htoa-5.0.1_r5e954ab_houdini-18.0.287/htoa-5.0.1_r5e954ab_houdini-18.0.287/scripts/bin")
os.environ['HOUDINI_PATH'] = '{};&'.format("C:/htoa/htoa-5.0.1_r5e954ab_houdini-18.0.287/htoa-5.0.1_r5e954ab_houdini-18.0.287")


if __name__ == "__main__":
    
    # Run Houdini
    subprocess.Popen(houdini)


