import sys
import re
import json

from netmiko import ConnectHandler

class NetDevice(object):

    def connect(type, ipaddress, username, password):
        A ={'device_type':type,'ip':ipaddress,'username':username,'password':password}
        net_connect=ConnectHandler(**A)

        if type == "arista_eos":
            return eos(net_connect)
        elif type == "juniper":
            return junos(net_connect)
        else:
            assert 0, "Invalid Device Type: " + type

    connect = staticmethod(connect)

class eos(NetDevice):

    def __init__(self, conn):
        self.net_connect = conn

    def parse_command(self, buff):
        x = re.sub('\{None\}', '', buff)
        j = json.loads(x)
        return j

    def get_arp(self):
        logger.debug()
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        #print (name)

        intf_desc = self.net_connect.send_command("show arp | json")
        json_buf = self.parse_command(intf_desc)
        return json_buf

    def bgp_neighbor(self):
        print("Arista Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show ip bgp summary | json")
        json_buf = self.parse_command(intf_desc)
        return json_buf

class junos(NetDevice):
    def __init__(self, conn):
        self.net_connect = conn

    def parse_command(self, buff):
        x = re.sub('\{master\}', '', buff)
        j = json.loads(x)
        return j

    def get_arp(self):
        print("Juniper Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show arp | display json")
        json_buf = self.parse_command(intf_desc)
        return json_buf

    def check_sys_uptime(self):
        print("Juniper Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show system uptime | display json")
        json_buf = self.parse_command(intf_desc)
        return json_buf

    def check_chassis_fpc(self):
        print("Juniper Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show chassis fpc | display json")
        json_buf = self.parse_command(intf_desc)
        return json_buf

    def check_sys_alarms(self):
        print("Juniper Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show system alarms | display json")
        json_buf = self.parse_command(intf_desc)
        return json_buf

    #Function for checking the shutdown event in the device
    def check_log_msg(self):
        print("Juniper Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show log messages | match system_abnormal_shudown")
        json_buf = self.parse_command(intf_desc)
        return json_buf

    #Function to check all the bgp neighbors for a device
    def bgp_neighbor(self):
        print("Juniper Device")
        a =  self.net_connect.find_prompt()
        name = (a[7:a.find('>')])
        print (name)

        intf_desc = self.net_connect.send_command("show bgp neighbor | display json")
        json_buf = self.parse_command(intf_desc)
        return json_buf


