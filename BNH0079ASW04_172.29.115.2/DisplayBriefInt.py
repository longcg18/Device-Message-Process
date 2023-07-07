import textfsm as tf

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

    relevant_data = read_data("BNH0079ASW04 _172.29.115.2_S3900.txt")
    interface_result = interface_template.ParseText(relevant_data)
    print("Device: 172.29.155.2 \nType: Switch Cisco 3900\n>>>Display brief interface command:")
    for res in interface_result:
        print(res[0])
        print("\tInterface Name:", interface_name(res[0]))
        print("\tLink State:", res[1])
        print("\tSwitch Port Mode:", res[2])
        print("\tDescription:", res[3])
