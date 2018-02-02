from tool.deco import exe_deco
from tool.driver import Appium

'''
	登录测试
'''


class ZwwLoginCase(Appium):

    @exe_deco
    def zww_login_case(self, email, pwd):
        # 点击邮箱登录按钮
        self.click_by_id("com.netease.ldzww:id/btn_email_login")
        # 输入用户名
        self.input_by_id("com.netease.ldzww:id/edt_email", email)
        # 输入密码
        self.input_by_id("com.netease.ldzww:id/edt_pwd", pwd)
        # 点击登录按钮
        self.click_by_id("com.netease.ldzww:id/btn_login")
