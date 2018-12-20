import subprocess
import time
import os

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
    # fr=open("lib/deploy_masscan.txt")
    # content=fr.readlines()
    # fr.close()

    #filename中存放扫描结果
    tm=time.strftime("%y_%m_%d_%H_%M_%S",time.localtime())
    filename=r'../wss/drose/collector/lib/result_masscan'+tm+'.txt'
    print(filename)
    handle=open(filename,'a')

    time_start = time.time()
    #将读入的每行转化为列表，调用masscan扫描
    # for line in content:
    # listforline=line.strip().split()
    #child = subprocess.Popen('masscan -p%s %s' % (listforline[1], listforline[0]), stdout=handle)
    print('masscan -p%s %s --rate=10000'%(port, ip))
    child=subprocess.Popen('masscan -p%s %s --max-rate 10000'%(port, ip),stdout=handle)
    child.wait()
    print(time.time()-time_start)
    handle.close()

    fip=open(filename)
    result_content=fip.readlines()
    ip_port={}
    for line in result_content:
        split_line=line.strip().split()
        ip=split_line[-1]
        port=split_line[-3].split('/')[0]
        if ip not in ip_port.keys():
            ip_port[ip]=port
        else:
            ip_port[ip]=ip_port[ip]+','+port
    print(len(list(ip_port.keys())))
    return ip_port