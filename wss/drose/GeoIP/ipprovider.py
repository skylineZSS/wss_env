import pygeoip
import django.utils.timezone as timezone
from ..models import ipaddress
#获取ip或域名所在的国家
#g=pygeoip.GeoIP('./GeoIP.dat')
#print(g.country_code_by_name('google.com'))
def geoipprovider(ip):
    gi = pygeoip.GeoIP('../wss/drose/GeoIP/GeoLiteCity.dat')
    result=gi.record_by_addr(ip)
    #print(result)
    obj = ipaddress.objects.filter(ip=ip)
    if obj:
        obj.update(continent=result['continent'],country_name=result['country_name'], city=result['city'],latitude=result['latitude'],longitude=result['longitude'],updatetime=timezone.now())
        print('地址数据更新成功')
    else:
        obj = ipaddress(ip=ip,continent=result['continent'],country_name=result['country_name'], city=result['city'],latitude=result['latitude'],longitude=result['longitude'],updatetime=timezone.now())
        obj.save()
        print('地址数据添加成功')
    country_city=result['country_name']+','+result['city']
    print(country_city)





