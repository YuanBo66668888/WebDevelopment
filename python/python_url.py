# encoding = utf-8
import urllib
import re
import os
import time

urls = ["http://photo.sina.com.cn/", "http://www.nipic.com/photo/index.html"];
dirnames = ["sina", "nipic"];

def getHTML(url):
    page = urllib.urlopen(url);
    html = page.read();
    return html

kind = 0;
for url in urls:
    html = getHTML(url);
    reg_html = r'src="(.+?\.jpg)"';
    imgre = re.compile(reg_html);
    imglist = re.findall(imgre, html);
    index = 0;
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, 'pics/%s_%s%s.jpg' %(dirnames[kind],int(time.time()),index));
        print("Save One...")
        index = index + 1
    kind = kind + 1