import masscan
import time

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# #读入扫描对象
# fr=open("../lib/deploy_masscan.txt")
# content=fr.readlines()
# fr.close()
#
# #filename中存放扫描结果
# tm=time.strftime("%y_%m_%d_%H_%M_%S",time.localtime())
# filename=r'..\lib\result_masscan'+tm+'.txt'
# #print(filename)
# handle=open(filename,'a')
#
# #将读入的每行转化为列表，调用masscan扫描
# for line in content:
#     line=line.strip()
#     listforline=line.split('\t')
#     #定义扫描指令
#     args=['masscan','-p',listforline[1],listforline[0]]
#     #print(args)
#     subprocess.Popen(args,stdout=handle)
# handle.close()

def openport_scan(ip, port):
    start = time.time()
    mas = masscan.PortScanner()
    mas.scan(ip, ports=port, arguments='--max-rate 10000')
    #存储扫描结果
    results = mas.scan_result
    open_ips = list(results['scan'].keys())
    proto = 'tcp'
    ip_port = {}
    for open_ip in open_ips:
        open_ports = list(results['scan'][open_ip][proto].keys())
        ip_port[open_ip] = ','.join([str(open_port) for open_port in open_ports])
    print(time.time() - start)
    print(ip_port)
    return ip_port