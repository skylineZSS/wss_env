import nmap
import pandas as pd
import django.utils.timezone as timezone
from ..models import scanresult
# nm = nmap.PortScanner()
# nm.scan('121.248.55.130', '20,80-500')
# cmd=nm.command_line()
# print(cmd)
# print(nm.csv())

def scan2csv(Host,Ports, Arguments):
    nm = nmap.PortScanner()
    data = nm.scan(hosts= Host,ports=Ports,arguments=Arguments)
    timestr = data['nmap']['scanstats']['timestr']
    timestr = timestr.replace(' ','-')
    timestr = timestr.replace(':','-')
    ip = Host
    name = '../wss/drose/collector/lib/'+str(ip)+timestr+'.csv'
    port_list = []
    try:
        # protocol = list(data['nmap']['scaninfo'].keys())
        # for proto in protocol:      #不同协议

        os = data['scan'][ip]['osmatch'][0]['name']
        print(os)
        proto = 'tcp'
        tcp_port = data['scan'][ip][proto]      #
        ports = list(data['scan'][ip][proto].keys())
        for port in ports:      #不同端口
            port_dict = tcp_port[port]
            if 'script' not in port_dict.keys():
                port_dict['script'] = ''
            port_dict['port'] = port
            port_dict['proto'] = proto
            port_dict['operation'] = os
            port_list.append(port_dict)
            obj = scanresult.objects.filter(ip=ip, port=port)
            if obj:
                obj.update(cpe=port_dict['cpe'], name=port_dict['name'], product=port_dict['product'], proto=port_dict['proto'], state=port_dict['state'], version=port_dict['version'], banners=port_dict['script'], updatetime=timezone.now(), operation= port_dict['operation'])
                print('数据更新成功')
            else:
                obj = scanresult(ip=ip, port=port, cpe=port_dict['cpe'], name=port_dict['name'], product=port_dict['product'], proto=port_dict['proto'], state=port_dict['state'], version=port_dict['version'], banners=port_dict['script'], updatetime=timezone.now(), operation= port_dict['operation'])
                obj.save()
                print('数据添加成功')
        df = pd.DataFrame(port_list)
        df.to_csv(name)
    except:
        print("处理"+ ip + "时发生错误")