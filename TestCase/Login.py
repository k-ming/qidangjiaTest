from Main import Setup
import time,unittest,os



# 引入配置文件
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


        # 结束回话
        # self.driver.quit()


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
