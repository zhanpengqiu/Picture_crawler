import urllib.request
import time,re
import chardet
from bs4 import BeautifulSoup
import urllib.parse

 
x=1

def get_url(url):
    global x
    print(url)
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

    print(img_list)
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
                #'Accept-Encoding': 'gzip',
                 'Cookie': 'UM_distinctid=173a2c5bc624df-00a390221de6cf-3b634404-144000-173a2c5bc635fa; JSESSIONID=B8E37C7957CFA1DC3AF0281BC6551315; CNZZDATA1278247911=1495991305-1596163734-https%253A%252F%252Flink.zhihu.com%252F%7C1597151715; Hm_lvt_659a08f50365d3fc99460022e4ad38c8=1597049682,1597050542,1597073756,1597151710; Hm_lpvt_659a08f50365d3fc99460022e4ad38c8=1597151976'
}
        
        newlist=urllib.request.Request(newlist,headers=headers)

        
        result=urllib.request.urlopen(newlist).read()


        
            
        with open('身份证信息//妹子2//'+title,'wb') as f:
            f.write(result)#保存图片


def getlist(url):
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

    lis =soup.find('div',{'class': 'swiper-container'}).findAll('img')

    pages = lis[-1].attrs['data-src' or 'src'].split('h')[-1].split('.')[0]
    print(pages)
    return int(pages)

def findall_url(url):#第一个页面的所有图册
    global x
    url_imgs=[]
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)
    
    response=urllib.request.urlopen(req)
    content=response.read()
    result=chardet.detect(content)['encoding']#获取编码信息
    if result=='GB2312':
        result='GBK'
    print(result)
    content=content.decode(result)
    soup=BeautifulSoup(content,'html.parser')

    li_list = soup.find('div', {'class': 'all_lanmu'}).find('ul',{'class':'twoline'}).findAll('li')
    for i in li_list:
        url_img = i.find('a').attrs['href']
        url_imgs.append('https://www.showmeizi.com'+url_img)
    return url_imgs
    

url='https://www.showmeizi.com/'
img_list=findall_url(url)
print(img_list)
for i in img_list:
    pages=getlist(i)
    i=i.split('.')[0]+'.'+i.split('.')[1]+'.'+i.split('.')[2]
    print(i)
    
    for j in range(1,pages+1):
        if j==1:
            eachurl=i+'.html'
        else:
            eachurl=i+'_%d.html'%(j)
        print(eachurl)
        get_url(eachurl)
        j+=1
        
