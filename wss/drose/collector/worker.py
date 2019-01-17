#负责调用模块完成业务逻辑
import django
django.setup()
from multiprocessing import Pool
from .demo_portScan import openport_scan
from .demo_nmapScanner import scan2csv
from ..GeoIP.ipprovider import geoipprovider
import time,os

def scanNetwork(IP, Port, Arguements):
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    i = IP.split(',')  # 对多个目标地址进行分割
    for target in i:
        p.apply_async(worker,args=(target,Port,Arguements,))
    print('Waiting for all subprocesses done...')
    # 调用close()之后就不能继续添加新的Process了
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    # 调用join()之前必须先调用close()
    p.join()
    print('All subprocesses done.')

def worker(ip,port ,arguements):
    print('Run task %s (%s)...' % (ip,os.getpid()))
    start = time.time()
    ip_port = openport_scan(ip, port)
    num = 1
    for host in ip_port:
        print('第%d个ip:%s' % (num,host))
        scan2csv(host, ip_port[host], arguements)
        geoipprovider(host)
        num = num + 1
    print('该%s扫描用时：%f' % (ip, time.time() - start))