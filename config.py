# coding:utf-8
from os.path import abspath,join,dirname

PATH = lambda dir_name,apk_name:abspath(
	join(abspath(dirname(__file__)),'apk',dir_name,apk_name)
)

command_executor = 'http://localhost:4723/wd/hub'

desired_caps_zww = {
	'deviceName':'Vivo x9s',
	'version':'7.1.1',
	'platformName':'Android',
	'app':PATH(dir_name='zww',apk_name='ldzww_1.0.3_wynt4.apk'),
	'app-package':'com.netease.ldzww',
	'app-activity':'com.netease.ldzww.login.activity.LoginEntryActivity',
	'unicodeKeyboard':True,
	'resetKeyboard':True
}