from Node import *
from csvManager import *

PATH = "csvTest.csv"
PORT = "23"
USERNAME = "Bintou"

if __name__ == '__main__':
    data = getData(PATH, "Display_name", "ip_address")[0]
    output = OutputFile()
    for row in data:
        ip_address = row[IP_ADDRESS]
        display_name = row[DISPLAY_NAME]
        n = Node()
        n.change_params(display_name, ip_address, PORT, USERNAME)
        output.add_node(n.node)
    output.dump_file()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
