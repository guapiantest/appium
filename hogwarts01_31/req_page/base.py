import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = requests.Session()
        self.corpid = 'wwb6c5c5597de9480d'
        self.corpsecret = 'fEIaT-VmujLm25MYbSzDJGgYnP12M63Hudp64vYq65s'
        # self.token = self.get_access_token(self.corpid, self.corpsecret).get('access_token')  # token 登录
        self.s.params['access_token'] = self.get_access_token(self.corpid, self.corpsecret).get(
            'access_token')  # session登录

    def get_access_token(self, corpid, corpsecret):
        params = {'corpid': corpid, 'corpsecret': corpsecret}
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        print(r.json())
        return r.json()
