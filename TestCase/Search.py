from Main import Setup
import time,unittest,os

class QDJ_Search_Test(Setup.Base,unittest.TestCase):
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def test_search(self):
        # 此处要调用初始化操作,获取driver
        sDriver = self.driver
        # 点击返回首页
        sDriver.find_element_by_id('com.jdcf.qh:id/iv_back').click()
        time.sleep(1)
        # 点击搜索按钮
        if sDriver.find_element_by_id('com.jdcf.qh:id/home_search').text == '搜索合约代码/合约名称/资讯':
            sDriver.find_element_by_id('com.jdcf.qh:id/home_search').click()
            time.sleep(1)
            sDriver.save_screenshot('E:/workspace/qidangjiaTest/Screenshort/'+'Search_'+QDJ_Search_Test.now_time+'.png')
        else:
            print('搜索文案错误')
            sDriver.save_screenshot('E:/workspace/qidangjiaTest/Screenshort/'+'Search_'+QDJ_Search_Test.now_time+'.png')


        # 进入搜索页面
        if sDriver.find_element_by_id('com.jdcf.qh:id/search_et_input').text == '搜索合约代码/合约名称/资讯':
            sDriver.find_element_by_id('com.jdcf.qh:id/search_et_input').send_keys('1805')
            time.sleep(5)
            sDriver.save_screenshot('E:/workspace/qidangjiaTest/Screenshort/'+'Search_'+QDJ_Search_Test.now_time+'.png')
            # 点击第一个合约，进入行情页
            sDriver.find_element_by_id('com.jdcf.qh:id/search_container').click()
            time.sleep(3)
            sDriver.save_screenshot(os.chdir(os.path.join(os.getcwd(), '../Screenshort'))+'Search_'+QDJ_Search_Test.now_time+'.png')



        # 结束回话
        # self.driver.quit()




# if __name__ == '__main__':
#     unittest.main(verbosity=2)

