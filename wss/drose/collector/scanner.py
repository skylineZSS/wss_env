import subprocess
import time
#网络扫描类
class Scanner():
	#读取扫描配置表中内容,进行规范化处理
    def deploy(self):
        list={}
        return list

    # 调用masscan，以字典形式返回开放ip及端口
    #1.从文件deploy_masscan.txt读入扫描范围
    #2.调用masscan扫描
    #3.将结果写入文件masscan_result.txt文件
    def portScan(self):
        # 读入扫描对象
        fr = open("../lib/deploy_masscan.txt")
        content = fr.readlines()
        fr.close()

        # filename中存放扫描结果
        tm=time.strftime("%y_%m_%d_%H_%M_%S",time.localtime())
        filename = r'..\lib\result_masscan' + tm + '.txt'
        # print(filename)
        handle = open(filename, 'a')

        # 将读入的每行转化为列表，调用masscan扫描
        for line in content:
            line = line.strip()
            listforline = line.split('\t')
            # 定义扫描指令
            args = ['masscan', '-p', listforline[1], listforline[0]]
            # print(args)
            subprocess.Popen(args, stdout=handle)
        handle.close()
        ip_port = {}
        return ip_port

	#调用nmap进行版本信息(返回原始数据包存入数据库)和操作系统探测
    def nmapScanner(self,ip_port):
        pass

    #调配以上各函数协同工作
    def WebScanner(self):
        pass


