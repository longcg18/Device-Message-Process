import textfsm as tf
import openpyxl

def interface_name(any):
    ats = str(any)
    ats = ats.replace("Eth", "Ethernet").replace("GE", "GigabitEthernet")
    ats = ats.replace("TENGE", "tenGigabitEthernet").replace("Loop", "Loopback")
    return ats

def read_data(fileName):
    f = open(fileName, "r")
    start_marker = "Interface   Link"
    end_marker = "@BLOCK--"

    file_content = f.read()

    start_index = file_content.find(start_marker) + len(start_marker)
    end_index = file_content.find(end_marker, start_index)

    relevant_data = file_content[start_index:end_index].strip()
    return relevant_data

if (__name__ == '__main__'):

    with open("DisplayBriefInt.template") as f:
        interface_template = tf.TextFSM(f)

    fileName = "BNH0079ASW04 _172.29.115.2_S3900.txt"
    deviceInfos = fileName.split("_")
    deviceName = deviceInfos[0]
    deviceIP = deviceInfos[1]
    deviceModel = deviceInfos[2]

    relevant_data = read_data("BNH0079ASW04 _172.29.115.2_S3900.txt")
    results = interface_template.ParseText(relevant_data)
    
    workbook = openpyxl.load_workbook("..\DataCollection.xlsx")
    sheetName = str(deviceName)
    if (sheetName in workbook.sheetnames) == True:
        workbook.remove(workbook[sheetName]) 
    worksheet = workbook.create_sheet(sheetName)    

    title = ['Interface', 'LinkState', 'SwitchPortMode', 'Description']
    for col, val in enumerate(title, start=1):
        worksheet.cell(row=1, column=col).value = val
    row_num=2
    for result in results:
        
        line = []
        line.append(str(interface_name(result[0])))    
        line.append(str(result[1]))        
        line.append(str(result[2]))  
        line.append(str(result[3]))      
        
        for col_num, res in enumerate(line, start=1):
            worksheet.cell(row_num, col_num).value=res
        row_num = row_num + 1
        
    workbook.save("..\DataCollection.xlsx")
    workbook.close()

