import configparser
import os
class Read():
    def ReadFile(self):
        os.chdir(os.path.join(os.getcwd(), "../Config"))
        cf = configparser.ConfigParser()
        cf.read('config.ini', 'UTF-8')
        platformName=cf.get('info', 'platformName')
        platformVersion=cf.get('info', 'platformVersion')
        deviceName=cf.get('info', 'deviceName')
        app=cf.get('info', 'app')
        appPackage=cf.get('info', 'appPackage')
        appActivity=cf.get('info', 'appActivity')
        noReset=cf.get('info', 'noReset')
        return platformName, platformVersion, deviceName, app, appPackage, appActivity, noReset

# if __name__=='__main__':
#     R1 = Read()
#     tup = R1.ReadFile()
#     print(tup)
#     print(os.getcwd())


