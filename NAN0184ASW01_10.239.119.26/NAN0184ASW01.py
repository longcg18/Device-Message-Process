import textfsm as tf
import openpyxl

import os, sys
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
import ReadLogFile

if (__name__ == '__main__'):
    fileName = "NAN0184ASW01_10.239.119.26_S3100-28FC.txt"

    deviceInfos = fileName.split('_')
    deviceName = deviceInfos[0]
    deviceIP = deviceInfos[1]
    deviceModel = deviceInfos[2]

    with open(deviceName + ".template") as tpl:
        fsm = tf.TextFSM(tpl)

    start_marker = "NAN0184ASW01>show interface brief"
    end_marker = "Total entries: 28 ."
    data = ReadLogFile.read_data(fileName, start_marker, end_marker)

    results = fsm.ParseText(data)

    print(fsm.header)
    #for result in results:
    #    print(result)

    for record in results:
        port = record[0]
        description_start = record[1] if len(record) > 1 else ""
        description_rest = record[2] if len(record) > 2 else ""
        link = record[-5]
        shutdown = record[-4]
        speed = record[-3]
        pri = record[-2]
        pvid = record[-1]
        mode = record[-6]
        tag_vlan = record[-7]
        ut_vlan = record[-8]

        description = (description_start + " " + description_rest).strip()

        print("Port:", port)
        print("Description:", description)
        print("Link:", link)
        print("Shutdown:", shutdown)
        print("Speed:", speed)
        print("Pri:", pri)
        print("PVID:", pvid)
        print("Mode:", mode)
        print("TagVlan:", tag_vlan)
        print("UtVlan:", ut_vlan)
        print()