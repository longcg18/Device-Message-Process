import textfsm as tf
import openpyxl

import os, sys
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
import ReadLogFile

if (__name__ == '__main__'):
    fileName = "VTU0009ASW01_172.16.32.248_5928E.txt"
    deviceInfos = fileName.split('_')
    deviceName = deviceInfos[0]
    deviceIP = deviceInfos[1]
    deviceModel = deviceInfos[2]

    with open(deviceName + ".template") as tpl:
        fsm = tf.TextFSM(tpl)
    
    start_marker = "Interface     AdminStatus  PhyStatus  Protocol  Description"
    end_marker = "@@BLOCK--"
    data = ReadLogFile.read_data(fileName, start_marker, end_marker)

    results = fsm.ParseText(data)
    for result in results: 
        print(result)