import sys
import re
import json

from netmiko import ConnectHandler

class NetDevice():
    def __init__(self):
        self.logger = ulnet_logging.service_logger()
    
    def connect(self, device_type, ipaddress, username, password):
        self.logger.info("Connecting")
        a = {'device_type': device_type, 'ip': ipaddress, 'username': username, 'password': password}
        try:
            net_connect = ConnectHandler(**a)
        
        except netmiko.NetMikoTimeoutException as error:
            logger.error("Timed out trying to connect to {0}".format(a['ip']))
            return "Not Reachable"
        except netmiko.NetMikoAuthenticationException as error:
            logger.error("Connected, but failed to authenticate to {0}".format(a['ip']))
            return "Not Reachable"
        except Exception as e:
            logger.exception(e)
            return "Not Reachable"
        
        if device_type == "arista_eos":
            return Eos(net_connect)
        elif device_type == "juniper":
            return Junos(net_connect)
        elif device_type == "cisco_ios":
            return CiscoIos(net_connect)
        else:
            assert 0, "Unsupported device type: " + device_type

class Eos(NetDevice):
    def __init__(self, conn):
        self.net_connect = conn
        super().__init__()
    
    
    def get_arp(self):
        
        cmd = "show arp | json"
        self.logger.debug("Sending command {}".format(cmd))
        
        result = self.net_connect.send_command(cmd)
        return result
    
    def bgp_neighbor_state(self):
        cmd = 'show ip bgp sum vrf all | json'
        self.logger.debug("Sending command {}".format(cmd))
        
        op = self.net_connect.send_command(cmd)
        result = json.loads(op)
        return result
    
    def interface_status(self,intf):
        cmd = 'show interfaces {} | json'
        self.logger.debug("Sending command {}".format(cmd))
        
        op = self.net_connect.send_command(cmd.format(intf))
        result = json.loads(op)
        return result

class Junos(NetDevice):
    def __init__(self, conn):
        self.net_connect = conn
        super().__init__()
    
    
    def get_arp(self):
        
        cmd = "show arp | display json"
        self.logger.debug("Sending command {}".format(cmd))
        result = self.net_connect.send_command(cmd)
        return result


class CiscoIos(NetDevice):
    def __init__(self, conn):
        self.net_connect = conn
        super().__init__()
    
    
    def get_arp(self):
        cmd = "show arp | display json"
        self.logger.debug("Sending command {}".format(cmd))
        result = self.net_connect.send_command(cmd)
        return result
    
    def ping_func(self,ip):
        cmd = "ping {}"
        self.logger.debug("Sending command {}".format(cmd))
        
        op = self.net_connect.send_command(cmd.format(ip))
        regex1 = re.compile("Success\srate\sis\s(\w+)\spercent\s\W(\w)/(\w)")
        match1 = regex1.search(op)
        percent = match1.group(1)
        trans_packet = match1.group(3)
        recv_packet = match1.group(2)
        dict1 = {'percentage':percent,'transmitted':trans_packet,'received':recv_packet}
        return dict1



