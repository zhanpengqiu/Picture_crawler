import urllib.request
import time,re
import chardet
from bs4 import BeautifulSoup
import urllib.parse
import os
import random

x=1

def open_url(url):
    global x
    url_imgs=[]

    UserAgent_List = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
    
    headers={'User-Agent':random.choice(UserAgent_List),}
    req=urllib.request.Request(url,headers=headers)
    
    response=urllib.request.urlopen(req)
    content=response.read()
    result=chardet.detect(content)['encoding']#获取编码信息
    if result=='GB2312':
        result='GBK'
    content=content.decode(result)
    soup=BeautifulSoup(content,'html.parser')

    li_list = soup.find('div', {'class': 'all_lanmu'}).find('ul',{'class':'twoline'}).findAll('li')
    for i in li_list:
        url_img = i.find('a').attrs['href']
        url_imgs.append('https://www.showmeizi.com'+url_img)
    return url_imgs

def get_url(url):
    global x

    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)

    
    response=urllib.request.urlopen(req)
    content=response.read()
    result=chardet.detect(content)['encoding']#获取编码信息
    if result=='GB2312':
        result='GBK'
    content=content.decode(result)
    
    soup=BeautifulSoup(content,'html.parser')
    img_list = soup.find('div',{'class': 'swiper-container'}).findAll('img')
    
    title_first=img_list[0].attrs['data-src'].split('/')[1].split('!')[0]#文件开头
    print(title_first)
    os.mkdir('身份证信息//秀妹子图片1//'+title_first)
    
    for img in img_list:
 
        img_url = 'https://www.showmeizi.com'+img.attrs['data-src']

        title = img_url.split('/')[-1]
        x+=1
        
        img_url1=urllib.parse.quote(img_url,encoding='utf-8')#开始解码
        jiexi=urllib.parse.urlparse(img_url)
        newlist=re.sub(r"%3A",":",img_url1)#新网址，解码后的网址

        
        new_url=urllib.parse.unquote(img_url1)

        headers={'User-Agent': '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip',
                 'Cookie': 'UM_distinctid=173a2c5bc624df-00a390221de6cf-3b634404-144000-173a2c5bc635fa; JSESSIONID=B8E37C7957CFA1DC3AF0281BC6551315; CNZZDATA1278247911=1495991305-1596163734-https%253A%252F%252Flink.zhihu.com%252F%7C1597151715; Hm_lvt_659a08f50365d3fc99460022e4ad38c8=1597049682,1597050542,1597073756,1597151710; Hm_lpvt_659a08f50365d3fc99460022e4ad38c8=1597151976'}
        
        newlist=urllib.request.Request(newlist,headers=headers)
 
        result=urllib.request.urlopen(newlist).read()


        with open('身份证信息//秀妹子图片1//'+title_first+'//'+title,'wb') as f:
            f.write(result)#保存图片


for i in range(1,100):
    url='https://www.showmeizi.com/?currentPage='+str(i)
    print(i)
    if i%5==0:
        j=int(input('输入1继续'))
        if j==1:
            print('您选择继续')
        else:
            break


    img_list=open_url(url)
    
    for img in img_list:
        get_url(img)
        time.sleep(1)


