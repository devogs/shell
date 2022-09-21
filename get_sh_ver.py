import csv
import xml.etree.ElementTree as ET

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# Import from mRemoteNG
def SetHostname(xml):
    tree = ET.parse(xml)
    root = tree.getroot()

    Name_dict = []
    for child in root:
        for elem in child:
            for sub in elem:
                Name_dict.append(sub.attrib['Hostname'])

    return Name_dict

def GetCommands(params):
    with ConnectHandler(**params) as c:
        try:
            c.enable()
            sh_ver = c.send_command('show version', use_textfsm=True)
        except Exception as e:
            print(e)

        return sh_ver

def CreateList(output):
    result = [
    output[0]['hostname'],
    output[0]['version'],
    output[0]['serial']
    ]

    return result

def AddToFile(csv_data):

    header = ['hostname', 'version', 'serial']
    with open('get_sh_ver.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(csv_data)

def Main():

    # password = getpass()
    # enable = getpass()

    devices_list = SetHostname('mremote_file.xml')

    for device in devices_list:

        params = {
            'device_type': 'cisco_ios',
            'ip': device,
            'username': 'admin',
            'password': 'admin1234',
            'secret': 'en1234',
            'port': '22'
        }
        
        command_output = GetCommands(params)
        list_result = CreateList(command_output)
        AddToFile(list_result)
        break

if __name__ == "__main__":
    Main()