# coding: utf-8
import requests
import re
class Weibo(object):
    '''
    新浪微博类
    '''
    headers = { # 这个请求头一定要有，否则会失败
        "Host": "m.weibo.cn",
        "Connection": "keep-alive",
        "Origin": "http://m.weibo.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Referer": "",
        "Accept-Language": "zh-CN,zh;q=0.8",
        }
    def __init__(self, username, password):
        '''
        借助移动端进行登录
        '''
        #user,password用户名密码,使用自己注册的sina用户名密码
        self.username = username
        self.password = password
        self.session = requests.Session()
        self._login()
    def _login(self):
        #登录地址
        url_login = r"http://passport.weibo.cn/sso/login" # 是的，这就是移动端的登录地址
        headers = self.headers.copy()
        headers['Host'] = "passport.weibo.cn"
        headers['Origin'] = "http://passport.weibo.cn"
        headers['Referer'] = "http://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F"
        payload = {
            "username" : self.username,
            "password" : self.password,
            "savestate" : "1",
            "ec" : "0",
            "pagerefer" : "http%3A%2F%2Fpassport.weibo.cn%2Fsignin%2Fwelcome%3Fentry%3Dmweibo%26r%3Dhttp%253A%252F%252Fm.weibo.cn%252F%26wm%3D3349%26vt%3D4",
            "entry" : "mweibo", #我猜，这里是mobile weibo的意思，表明登录是来自移动端
            "wentry" : "",
            "loginfrom" : "",
            "client_id" : "",
            "code" : "",
            "qq" : "",
            "hff" : "",
            "hfp" : "",
        }
        resp = self.session.post(
                url_login,
                data=payload,
                headers=headers
            ).json()
        self.uid = resp['data']['uid'] #保存用户id
        for url in resp['data']['crossdomainlist'].values(): # 响应中返回的domainlist每个要请求一下，否则登录不完整
            #print(url)
            if not url.startswith("http:") and not url.startswith("https:"): url = "http:" + url
            if url.startswith("https:"): url = "http:"+url[6:]
            #print(url) 
            self.session.get(url)#,verify = 'mycert.pem')
        self.session.get("https://m.weibo.cn/") # 最后这里如果能够正常看到响应结果，说明登录成功
    def add_new(self, content):
        '''
        create a new weibo发布新微博方法
        '''
        addurl = "https://m.weibo.cn/mblogDeal/addAMblog"
        st = re.findall(r'"st":"(\w+)"', self.session.get(r"https://m.weibo.cn/mblog").text)
    # 如果发送数据中有一些值为数字字母等混合的长得像随机数的参数，
    # 建议可以在页面源代码里找找，然后用正则表达式提取出来。就像这里的st
        data = {'content':content, 'st':st[0],}
        headers = self.headers.copy()
        headers['Referer'] = "https://m.weibo.cn/mblog"
        respon = self.session.post(addurl, data, headers=headers).json()
        return respon.get("msg", "Unknow Error") # 这里的msg是发布结果
    def comment(self, mid, content):
        '''
        post a comment发布新微博方法
        '''
        mid = str(mid)
        addurl = "https://m.weibo.cn/api/comments/create"
        st = re.findall(r"st: '(\w+)'", self.session.get(r"https://m.weibo.cn/status/"+mid).text)
        data = {'content':content, 'st':st[0],'id':mid,'mid':mid,}
        headers = self.headers.copy()
        headers['Referer'] = "https://m.weibo.cn/compose/comment?id="+mid
        respon = self.session.post(addurl, data, headers=headers).json()
        print(respon)
    def annoy(self,uid,content):
        cnt = 5
        uid = str(uid)
        url = 'https://m.weibo.cn/api/container/getIndex?uid='+uid+'&containerid=107603'+uid
        resp = self.session.get(url).json()
        for card in resp.get('cards'):
            if cnt == 0:
                break
            x = card.get('itemid')
            t = card.get('card_type')
            if t == 9:
                print(x)
                self.comment(x.split('_-_')[1],content)
                cnt -= 1
