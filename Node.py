import xml.etree.ElementTree as ET
from lxml import etree

IP_ADDRESS = "ip_address"
DISPLAY_NAME = "Display_name"


class Node:
    def __init__(self):
        self.node = ET.Element("Node")
        self.node.set("Type", '1')
        ET.SubElement(self.node, "SavedSession")
        self.node.find("SavedSession").text = "Default Settings"
        ET.SubElement(self.node, "DisplayName")
        self.node.find("DisplayName").text = " "
        ET.SubElement(self.node, "ServerName")
        self.node.find("ServerName").text = " "
        ET.SubElement(self.node, "PuttyConType")
        self.node.find("PuttyConType").text = "2"
        ET.SubElement(self.node, "Port")
        self.node.find("Port").text = " "
        ET.SubElement(self.node, "UserName")
        self.node.find("UserName").text = " "
        ET.SubElement(self.node, "Password")
        self.node.find("Password").text = " "
        ET.SubElement(self.node, "PasswordDelay")
        self.node.find("PasswordDelay").text = " "
        ET.SubElement(self.node, "CLParams")
        self.node.find("CLParams").text = " "
        ET.SubElement(self.node, "ScriptDelay")
        self.node.find("ScriptDelay").text = " "

    def afficher(self):
        print(ET.dump(self.node))

    def set_clparams(self):
        ip_address = self.node.find("ServerName").text
        port = self.node.find("Port").text
        user_name = self.node.find("UserName").text
        protocol = ""
        if port == "22":
            protocol = "ssh"
        elif port == "23":
            protocol = "telnet"
        else:
            print("ERREUR: Mauvais port spécifié")
            exit(0)
        result = f"{ip_address} -{protocol} -P {port} -l {user_name}"
        return result

    def change_params(self, display_name, ip_address, port, username):
        self.node.find("DisplayName").text = display_name
        self.node.find("ServerName").text = ip_address
        self.node.find("Port").text = port
        self.node.find("UserName").text = username
        self.node.find("CLParams").text = self.set_clparams()


class OutputFile:
    def __init__(self):
        self.servers = ET.Element("Servers")
        self.putty = ET.Element("Putty")
        self.servers.append(self.putty)

    def add_node(self, node):
        self.putty.append(node)

    def dump_file(self):
        ET.ElementTree(self.servers).write("Session.xml", encoding="UTF-8", xml_declaration=True,
                                           default_namespace=None, method="xml")
        tree = etree.parse("Session.xml")
        output = etree.tostring(tree.getroot(), pretty_print=True, xml_declaration=True, encoding="UTF-8")
        with open("Session.xml", "wb") as f:
            f.write(output)
