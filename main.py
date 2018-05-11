# coding:utf-8
import requests
import platform
# import sys

# reload(sys)

# sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    '''
    html = requests.get('http://www.baidu.com')
    print(html.status_code)
    html.encoding = html.apparent_encoding
    # print dir(html)
    # text=html.text
    # text=text.decode("utf-8").encode("gbk")
    print(html.text)
    print("haha,success")

    '''
    print(platform.python_version())
    ss = '中国'
    print(ss)
    s11 = ss.decode('utf-8')
    print(s11)
    s22 = s11.encode('gbk')
    print(s22)
