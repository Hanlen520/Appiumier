# coding:utf-8
from os.path import abspath, join, dirname
import logging
import time
import os

ROOT_PATH = dirname(__file__)
DATA_PATH = join(ROOT_PATH, 'data')
APK_PATH = join(ROOT_PATH, 'apk')
LOG_PATH = join(ROOT_PATH, 'log')

_IMAGE = lambda data_path, img_name: abspath(
    join(data_path, img_name)
)

_APK = lambda apk_path, dir_name, apk_name: abspath(
    join(apk_path, dir_name, apk_name)
)


class AppiumierLogConfig:
    LOG_LEVEL = logging.NOTSET
    LOG_FILE_PATH = join(LOG_PATH, str(time.time()) + 'appiumier.log')
    LOG_MAX_SIZE = 10 * 1024 * 1024
    LOG_BACKUP_COUNT = 5
    FILE_LOG_LEVEL = logging.INFO
    STREAM_LOG_LEVEL = logging.INFO


command_executor = 'http://localhost:4723/wd/hub'

'''
	每次安装新包都需要重新配置：
	apk_name
	app_version
'''
apk_name = 'ldzww_1.1.0-base.apk'
email = os.environ.get('TEST_USERNAME')
userid = "87625139116"
pwd = os.environ.get('TEST_PASSWORD')
app_version = "版本V1.1.1"
nickname = "runcheck4"

'''
指定了appPackage和AppActivity可以不指定appPackage安装路径
'app':_APK(apk_path=APK_PATH,dir_name='zww',apk_name=apk_name),

启动app后若发生activity的切换则需要设置AppWaitActivity
'''
desired_caps_zww = {
    'deviceName': 'ZTE BV0720',
    'platformVersion': '6.0',
    'platformName': 'Android',
    'appPackage': 'com.netease.ldzww',
    'appActivity': 'com.netease.ldzww.main.activity.SplashActivity',
    'appWaitActivity': 'com.netease.ldzww.login.activity.LoginEntryActivity',
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
