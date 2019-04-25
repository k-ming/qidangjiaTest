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
	``` 名称  
	;Android 配置信息  
	```   
	``` 组名  
	[info]
	```  
	``` 平台名称  
	platformName=Android  
	```   
	``` Android版本  
	platformVersion=28  
	```  
	``` 设备名称  
	deviceName=小米手机
	```  
	``` apk路径  
	app=F:\yunshen\selenium+py\QDJ_Auto_Test\App\app-QDJ-1.0.0.apk
	```  
	``` apk包名  
	appPackage=com.dx168.efsmobile.application
	```  
	``` MainActivity名称  
	appActivity=SplashActivity
	```  
	``` 如果设备上已安装apk则不重新安装，可以设置成false则每次启动需要重新安装  
	noReset=true
	```
	#### 读取配置文件类 readConfig.py
	```  导入os,configparser 类
	import configparser
	import os
	```  
	class Read():
		def ReadFile(self):
			``` 切换到配置文件路径下  
			os.chdir(os.path.join(os.getcwd(), "../Config"))
			``` 
			``` 实例化读取配置文件类  
			cf = configparser.ConfigParser() 
			cf.read('config.ini', 'UTF-8')
			```  
			``` 读取配置文件参数  
			platformName=cf.get('info', 'platformName')
			platformVersion=cf.get('info', 'platformVersion')
			deviceName=cf.get('info', 'deviceName')
			app=cf.get('info', 'app')
			appPackage=cf.get('info', 'appPackage')
			appActivity=cf.get('info', 'appActivity')
			noReset=cf.get('info', 'noReset')
			```  
			``` 返回读取的参数  
			return platformName, platformVersion, deviceName, app, appPackage, appActivity, noReset
			```  
	
