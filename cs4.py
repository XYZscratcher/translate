# 导入 requests 包
import re
import requests
from bs4 import BeautifulSoup
text=input('翻译哪个单词？\n')
# 发送请求
x = requests.get('https://dict.youdao.com/result?word={}&lang=en'.format(text))
x.encoding="utf-8"
soup=BeautifulSoup(x.text,'html.parser')
a=soup.find(class_='trans')
a="单词 "+text+" 的意思是：\n"+a.text
print(a)
