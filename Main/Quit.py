from Main import Setup

# 用来执行退出session
class MyQuit(Setup.Base):
    def myQuit(self):
        self.driver.quit()

