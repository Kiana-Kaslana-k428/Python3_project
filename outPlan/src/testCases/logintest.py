# -*- coding: utf-8 -*-
# 作者: admin
# 时间: 2018/9/18 11:25
# 文件: logintest.py
from outPlan.src.model.login import Login
import unittest
import os
from outPlan.src.common.get_value import GetValue

class TestLogin(unittest.TestCase):
     global lg,data
     lg=None
     data=None

     def setUp(self):
         global lg,data

         aList = os.path.dirname(os.path.abspath('../..'))
         data_path = aList + '\\' + 'outPlan' + '\\' + 'data' + '\\parameter.txt'

         data=GetValue(data_path)

         lg = Login(data.getvalue('url'))

     def test_login(self):
         global lg,data
         res = lg.login(data.getvalue('account'),data.getvalue('password'))

         try:
            self.assertEqual(res['data']['username'], 'tongcheng@ynt.ai')
            self.assertEqual(res['data']['accountType'], 1)

         except Exception as e:
            print(e)

     def tearDown(self):
         pass





