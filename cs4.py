# 导入 requests 包
try:
    import requests
    from bs4 import BeautifulSoup
    while True:
        text=input('翻译哪个单词？\n')
        if len(text)>150:
            raise RuntimeError('你逗我呢 :(')
        # 发送请求
        try:
            x = requests.get('https://dict.youdao.com/result?word={}&lang=en'.format(text))
            x.encoding="utf-8"
            soup=BeautifulSoup(x.text,'html.parser')
            a=soup.find(class_='trans')
            if len(a.text)>100:
                tmp=a.text.split("；", 1)[0]
                a="单词"+text+"的意思是：\n"+tmp
            else:
                a="单词 "+text+" 的意思是：\n"+a.text
            print(a)
            print("="*30)
        except AttributeError:
            raise Exception('你输入的不是一个单词哦！')
except ModuleNotFoundError:
    raise Exception('请确保您有下载对应的模块！')
