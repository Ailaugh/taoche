import re, os ,pymongo
# 创建客户端
client = pymongo.MongoClient('localhost')
# 创建数据库
db = client['taobao']
# 创建表
table = db['xiaomi']
root = 'D:\Desktop\淘宝\小米'
file_list = os.listdir(root)
v = 0
for file in file_list:
    content = open('D:\Desktop\淘宝\小米\{}'.format(file), 'r', encoding='utf-8')
    a=content.read()
    title_list = re.compile('"title": "(.*?)",').findall(a)
    img_list=re.compile('"img": "(.*?)",').findall(a)
    sold_list=re.compile('"sold": "(.*?)",').findall(a)
    price_list=re.compile('"price": "(.*?)",').findall(a)
    url_list=re.compile('"url": "(.*?)",').findall(a)
    for a,b,c,d,e in zip(title_list,img_list,sold_list,price_list,url_list):
        print('='*99)
        print('标题:',a)
        print('价格:',d)
        print('销量:',c)
        print('图片:',b)
        print('url:',e)
        y={'title':a,'img':b,'sold':c,'price':d,'url':e}
        table.insert(y)
