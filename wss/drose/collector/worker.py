#负责调用模块完成业务逻辑
from .demo_portScan import openport_scan
from .demo_nmapScanner import scan2csv

# Hosts = 'scanme.nmap.org'
# Arguments = '-Pn -sS --script=banner '

def scanNetwork(IP, Port, Arguements):

    ip_port = openport_scan(IP, Port)
    num = 1
    for host in ip_port:
        print('第%s个ip'%num)
        scan2csv(host,ip_port[host],Arguements)
        num = num + 1


class Worker():
    pass