from random import randint
import pytest

from hogwarts01_31.req_page.base import Base
from hogwarts01_31.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()

    @pytest.mark.parametrize('corpid,corpsecret,result',
                             [(None, None, 41004), (None, '2345', 41002), ('34567', None, 41004),
                              ('wwb6c5c5597de9480d', 'fEIaT-VmujLm25MYbSzDJGgYnP12M63Hudp64vYq65s', 0)],
                             ids=['参数均为空', 'corpid为空', 'corpsecret为空', 'corpid与corpsecret均正确'])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_access_token(corpid, corpsecret)
        assert r.get('errcode') == result  # 或者assert r['errcode'] == result

    # 创建成员，原则：用后即焚，否则下次运行会失败
    @pytest.mark.parametrize('userid, name, mobile,department, result', [
        ('test001', 'test001', f"195{randint(11111111, 99999999)}", [2], 'created'),
        ('FeiXue', 'test001', '18301928701', [2], 'userid existed'),
        ('test002', 'test002', '15921057777', [2], 'mobile existed'),
        ('test002', 'test002', '18301928701', [9], 'invalid party list')
    ], ids=['正常添加', 'userid已存在', '手机号已存在', '部门不存在'])
    def test_add(self, userid, name, department, mobile, result):
        # 先判断要添加的userid存不存在，若存在，先删除
        f = self.contact.getmember('test001')
        if f.get('errcode') == 0:
            self.contact.deletemember('test001')
        r = self.contact.addmember(userid, name, mobile, department)
        assert result in r.get('errmsg')
        self.contact.deletemember('test001')

    @pytest.mark.parametrize('userid,result', [('FeiXue', 0), ('Fe', 60111)], ids=['查找存在成员', '查找不存在成员'])
    def test_get(self, userid, result):
        r = self.contact.getmember(userid)
        assert r.get('errcode') == result

    # def test_update(self,):
    #     r = self.contact.updatemember('FeiXue', '小丸', '15678902345')
    #     assert self.contact.getmember('FeiXue')["mobile"] == '15678902345'

    # 删除数据，不依赖其他用例创建的数据，否则并行运行会出错
    def test_delete(self):
        self.contact.addmember('ximenchuixue', 'ximenchuixue', '13800000000', [2])
        r = self.contact.deletemember('ximenchuixue')
        assert r["errmsg"] == 'deleted'
