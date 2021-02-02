from random import randint

import pytest
import requests

from hogwarts01_31.req_page.base import Base


class Contact(Base):
    def addmember(self, userid, name, mobile,department):
        payload = {"userid": userid, "name": name, "department": department, "mobile": mobile}
        # params = {'access_token': self.token}
        r = self.s.post('https://qyapi.weixin.qq.com/cgi-bin/user/create', json=payload)
        print(r.json())
        return r.json()

    def getmember(self, userid):
        # params = {'access_token': self.token, 'userid': userid}
        params = {'userid': userid}
        r = self.s.get('https://qyapi.weixin.qq.com/cgi-bin/user/get', params=params)
        print(r.json())
        return r.json()

    def updatemember(self, userid, name, mobile, **kwargs):
        # params = {'access_token': self.token}
        payload = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        payload.update(kwargs)
        r = self.s.post('https://qyapi.weixin.qq.com/cgi-bin/user/update',  json=payload)
        print(r.json())
        return r.json()

    def deletemember(self,userid):
        # params = {'access_token': self.token, 'userid': userid}
        params = {'userid': userid}
        r = self.s.get('https://qyapi.weixin.qq.com/cgi-bin/user/delete', params=params)
        print(r.json())
        return r.json()
