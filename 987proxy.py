import ctypes
import re
import requests
import time
import winsound

from bs4 import BeautifulSoup

strArrive = "987已到川桥路申江路，5站"
urlshengjiang = "http://www.shjt.org.cn:8005/bus/TrafficLineXML.aspx?TypeID=3&lineid=10474&stopid=7D940000&direction=1&name=987%E8%B7%AF"
strWait = "等待发车"
proxies = {
    "http": "http://name:password@174.34.50.33:8080/",
}

while 1:
    res = requests.get(urlshengjiang,proxies = proxies)
    listStopdis = re.findall(r"<stopdis>(.*)</stopdis>",res.text)

    if not listStopdis:
        print(strWait)
        time.sleep(20)
    elif  int(listStopdis[0]) > 1:
        print(listStopdis[0] + " stations left to 川桥路申江路")
        time.sleep(20)
    else:
        print(strArrive)
        winsound.Beep(600,1000)
        ctypes.windll.user32.MessageBoxW(0,strArrive,'987路公交车',0x1000) 
        break


