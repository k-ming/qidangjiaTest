# qidangjiaTest
其当家app,UI自动化测试框架，特点（只启动app一次，一个session就可以跑完所有用例）
### step1:环境搭建
1、windows下安装appium
2、安装pythonIDE3.6
3、安装pycharm

### step2:目录介绍
![项目结构]
1、qidangjiaTest 项目的根目录
2、app 存放apk文件的目录
3、Config 配置文件目录,config.ini是配置文件
4、Main 程序主入口，Enter.py 启动文件， Setup.py 初始化文件， Quit.py 退出驱动文件
5、Report 测试报告目录
6、Screenshort 截图目录
7、TestCase 测试用例目录 Login.py 测试登陆，Search.py 测试搜索 Study.py 测试学院
8、Utils 工具目录 HTMLTestRunner.py 生成HTML测试报告类，readConfig.py 读取配置文件类

### step3:文件介绍
#### 配置文件config.ini
	//配置信息  
	;Android   
	[info]
	//平台名称  
	platformName=Android  
	//Android版本  
	platformVersion=28  
	//设备名称  
	deviceName=小米手机
	//apk路径  
	app=F:\yunshen\selenium+py\QDJ_Auto_Test\App\app-QDJ-1.0.0.apk
	//apk包名  
	appPackage=com.dx168.efsmobile.application
	//MainActivity名称  
	appActivity=SplashActivity
	//如果设备上已安装apk则不重新安装，可以设置成false则每次启动需要重新安装  
	noReset=true
#### 读取配置文件类 readConfig.py
```python  
//导入os,configparser 类
import configparser
import os      
class Read():  
	def ReadFile(self):  
		//切换到配置文件路径下    
		os.chdir(os.path.join(os.getcwd(), "../Config"))  
		//实例化读取配置文件类    
		cf = configparser.ConfigParser()   
		cf.read('config.ini', 'UTF-8')  
		// 读取配置文件参数    
		platformName=cf.get('info', 'platformName')  
		platformVersion=cf.get('info', 'platformVersion')  
		deviceName=cf.get('info', 'deviceName')  
		app=cf.get('info', 'app')  
		appPackage=cf.get('info', 'appPackage')  
		appActivity=cf.get('info', 'appActivity')  
		noReset=cf.get('info', 'noReset')  
		//返回读取的参数    
		return platformName, platformVersion, deviceName, app, appPackage, appActivity, noReset  
```  
#### 初始化类 Setup.py
```python
from selenium import webdriver
from Utils import readConfig
import time,os

// 初始化信息,读取配置文件,建立session，初始化driver，供后面的测试用例直接调用

class Base():
    def setup(self):
        # 调用配置文件中的设备信息
        myRead = readConfig.Read()
        # 用一个元组来接收配置文件的信息
        tup = myRead.ReadFile()
        # ---------------------------------------------------------------------------------------------------------------
        # 定义设备需要的参数
        desired_caps = {}
        desired_caps['platformName'] = tup[0]
        desired_caps['platformVersion'] = tup[1]
        desired_caps['deviceName']= tup[2]
        desired_caps['app']= tup[3]
        # 如果指定了安装APP的路径，则appPackage，appActivity这两个参数可以不要
        # desired_caps['appPackage']= tup[4]
        # desired_caps['appActivity']= tup[5]
        # 不需要重新安装
        desired_caps['noReset']=tup[6]
        # 建立远程连接
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        time.sleep(8)
        # 执行adb命令来滑动引导页，进入广告页面
        os.system('adb shell input swipe 1060 960 10 960')
        time.sleep(1)
        os.system('adb shell input swipe 1060 960 10 960')
        time.sleep(3)
        # 立即进入其当家
        # self.driver.find_element_by_id('com.jdcf.qh:id/iv_guide_bg').click()
        time.sleep(2)
```  
#### 测试用例 Login.py 测试登陆,此处只用改用例举例  
```python
from Main import Setup
import time,unittest,os


// 引入配置文件,并获取到driver
class QDJ_Login_Test(Setup.Base,unittest.TestCase):
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def test_login(self):
        # 此处要调用初始化操作
        MyDriver = self.driver
        # 获取首页上个人中心图标
        MyDriver.find_element_by_id('com.jdcf.qh:id/customer_head_imge').click()
        # 进入个人中心页面，点击立即登录
        loging = MyDriver.find_element_by_id('com.jdcf.qh:id/tv_nickname')
        # 检验文案是否正确
        if loging.text == u'立即登录':
            # 跳转到登录界面
            loging.click()
            # 测试返回按钮
            back = MyDriver.find_element_by_id('com.jdcf.qh:id/tv_back')
            # 检验文案
            if back.text == u'返回':
                back.click()
                time.sleep(1)
            else:self.assertEqual(u'返回',loging.text,msg='返回文案错误')
            # 再次进入登录界面，点击微信登录
            loging.click()
            time.sleep(1)
            vxlogin = MyDriver.find_element_by_id('com.jdcf.qh:id/ll_vx_login')
            vxlogin.click()
            time.sleep(3)
            # 截取登录成功后的图片
            MyDriver.save_screenshot(os.chdir(os.path.join(os.getcwd(), '../Screenshort'))+'Login_'+QDJ_Login_Test.now_time+'.png')
            time.sleep(1)
        else:self.assertEqual(u'立即登录',loging.text,msg='立即登录文案错误')
        self.assertEqual(u'您好，欢迎来到期当家',MyDriver.find_element_by_id('com.jdcf.qh:id/tv_login_tips').text,msg='登录失败')	
```

#### 执行测试 Enter.py,此处使用的是python自带的unittest单元测试框架，所以没法用HTMLTestRunner.py生成测试报告，后面将继续优化
```python  
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
```
#### 退出driver 
```python
from Main import Setup

# 用来执行退出session
class MyQuit(Setup.Base):
    def myQuit(self):
        self.driver.quit()
```