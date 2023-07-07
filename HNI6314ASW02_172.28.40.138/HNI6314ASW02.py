import textfsm
import openpyxl

def interface_name(name):
    ats = str(name)
    return ats.replace("gi", "GigabitEthernet")

def read_data(fileName):
    f = open(fileName, "r")
    start_marker = "@@BLOCK--"
    end_marker = "@@BLOCK--"

    file_content = f.read()

    start_index = file_content.find(start_marker) + len(start_marker)
    end_index = file_content.find(end_marker, start_index)

    relevant_data = file_content[start_index:end_index].strip()
    return relevant_data

def export_title(title):
    print()

if (__name__ == '__main__'): 
    fileName = "HNI6314ASW02_172.28.40.138_MyPowerS4220.txt"
    with open("HNI6314ASW02.template") as tpl:
        fsm = textfsm.TextFSM(tpl)

    deviceInfos = fileName.split("_")
    deviceName = deviceInfos[0]
    deviceIP = deviceInfos[1]
    deviceModel = deviceInfos[2]

    title = ['Interface', 'LinkState', 'ActSpeed', 'ActDuplex', 'PVid', 'Description']


    workbook = openpyxl.load_workbook("..\DataCollection.xlsx")
    sheetName = str(deviceName)
    if (sheetName in workbook.sheetnames) == True:
        workbook.remove(workbook[sheetName])
    worksheet = workbook.create_sheet(sheetName)

    for col, val in enumerate(title, start=1):
        worksheet.cell(row=1, column=col).value = val

    #deviceInfos = fileName.split('_')
    results = fsm.ParseText(read_data(fileName))

    row_num = 2

    #print(fsm.header)
    for result in results:
        line = []
        line.append(str(interface_name(result[0])))
        line.append(str(result[1]))
        line.append(str(result[2]))
        line.append(str(result[3]))
        line.append(str(result[4]))
        line.append(str(result[5]))

        for col_num, res in enumerate(line, start=1):
            worksheet.cell(row_num, col_num).value=res
        row_num = row_num + 1

    workbook.save("..\DataCollection.xlsx")
    workbook.close()