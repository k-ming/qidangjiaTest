# encoding = utf-8
'''
Created by ming.zheng on 2018/2/9.
 '''

from Main import Setup
import time,unittest,os

class QDJ_Study_Test(Setup.Base,unittest.TestCase):
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    def test_study(self):
        sDriver = self.driver
        # 返回到首页
        sDriver.find_element_by_class_name('android.widget.ImageButton').click()
        time.sleep(1)
        # 进入投资学院
        sDriver.find_element_by_xpath('//android.widget.ScrollView[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView').click()
        # sDriver.find_element_by_id('com.jdcf.qh:id/quote_school').click()
        time.sleep(3)
        sDriver.save_screenshot(os.chdir(os.path.join(os.getcwd(), '../Screenshort'))++'Study_'+QDJ_Study_Test.now_time+'.png')
        self.assertEqual('视频课堂',sDriver.find_element_by_id('com.jdcf.qh:id/tv_first').text,msg='视频课堂文案错误')
        self.assertEqual('期货科普',sDriver.find_element_by_xpath('//android.webkit.WebView//android.webkit.WebView/android.widget.ListView/android.view.View[0]/android.view.View[1]'),msg='期货科普文案错误')


        time.sleep(10)
        # self.assertEqual('期货科普',sDriver.find_element_by_link_text('期货科普').text,msg='期货科普文案错误')
        # self.assertEqual('投资心得',sDriver.find_element_by_link_text('投资心得').text,msg='投资心得文案错误')
        # self.assertEqual('产品指南',sDriver.find_element_by_link_text('投资心得').text,msg='产品指南文案错误')