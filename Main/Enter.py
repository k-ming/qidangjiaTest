# encoding = utf-8
'''
Created by ming.zheng on 2018/2/9.
 '''
from Utils import HTMLTestRunner
from Main import Setup,Quit
from TestCase import Login,Search,Study
import unittest


class QDJ_Test_Case (unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print('正在进行初始化...')
        # 此处调用初始化操作
        Setup.Base.setup(self)

    @classmethod
    def tearDownClass(self):
        print('正在退出会话...')
        # 此处调用退出driver操作
        Quit.MyQuit.myQuit(self)

    def testCase1(self):
        # 此处调用登录用例
        print('正在执行第1条用例...')
        Login.QDJ_Login_Test.test_login(self)

    def testCase2(self):
        # 此处调用搜索用例
        print('正在执行第2条用例...')
        Search.QDJ_Search_Test.test_search(self)

    def testCase3(self):
        # 此处调用投资学院用例
        print('正在执行第3条用例...')
        Study.QDJ_Study_Test.test_study(self)