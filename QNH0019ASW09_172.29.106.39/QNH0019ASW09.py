import textfsm as tf
import openpyxl

import os, sys
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
import ReadLogFile

if (__name__ == '__main__'):
    fileName = "QNH0019ASW09_172.29.106.39_S2309.txt"
    deviceInfos = fileName.split('_')
    deviceName = deviceInfos[0]
    deviceIP = deviceInfos[1]
    deviceModel = deviceInfos[2]

    # 
    with open (deviceName + "_interface.template") as int_tpl:
        int_fsm = tf.TextFSM(int_tpl)
    
    with open (deviceName + "_description.template") as des_tpl:
        des_fsm = tf.TextFSM(des_tpl)

    start_marker = "Interface                   PHY   Protocol InUti OutUti   inErrors  outErrors"
    end_marker = "@@BLOCK--"
    int_data = ReadLogFile.read_data(fileName, start_marker, end_marker)
    int_results = int_fsm.ParseText(int_data)
   
    start_marker = "Interface                     PHY     Protocol Description"
    end_marker = "@@BLOCK--"
    des_data = ReadLogFile.read_data(fileName, start_marker, end_marker)
    des_results = des_fsm.ParseText(des_data)

    print(len(des_results))
    for res in des_results:
        print(res)

    #print(len(int_results), len(des_results))

    #print(int_fsm.header)

    #for int_result in int_results:
    #    print(int_result)

    #print(des_fsm.header)