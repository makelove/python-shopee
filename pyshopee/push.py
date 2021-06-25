# -*- encoding: utf-8 -*-
'''
@File    :   push.py
@Time    :   2021/06/25 14:30:24
@Author  :   GH
@Desc    :   
'''

from .base import BaseModule


class Push(BaseModule):
    def GetPushConfig(self, **kwargs):
        """
        https://open.shopee.com/documents?module=71&type=1&id=460&version=1
        Use this API to get the configuration information of push service.
        :param kwargs:
        :return:
        """
        return self.client.execute("push/get_config", "POST", kwargs)
    pass

    def SetPushConfig(self, **kwargs):
        """
        https://open.shopee.com/documents?module=71&type=1&id=461&version=1
        Use this API to set the configuration information of push service.
        :param kwargs:
        :return:
        """
        return self.client.execute("push/set_config", "POST", kwargs)
    pass
