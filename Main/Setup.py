from selenium import webdriver
from Utils import readConfig
import time,os

# 初始化信息,读取配置文件

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
        # 关闭按钮
        # self.driver.find_element_by_id('com.jdcf.qh:id/iv_close').click()
        # return  self.driver
    # --------------------------------------------------------------------------------------------------------------------
    # 退出webdriver
    # def tearDown(self):

    # 判断页面上的元素是否存在
    # def isElementExist(self,element):
    #     flag = True
    #     try:
    #         self.driver.find_element_by_id(element)
    #         return flag
    #     except:
    #         flag = False
    #         return flag



# if __name__ == '__main__':
#     myBase = Base()
#     myBase.setup()
#     myBase.tearDown()