from nose.tools import assert_equal
from tool.deco import exe_deco
from tool.driver import Appium

'''
	设置页面相关测试
'''


class ZwwSettingsCase(Appium):

    @exe_deco
    def zww_settings_case(self, app_version):
        '''
                    设置页面测试
                '''
        # 点击设置按钮
        self.click_by_xpath("//android.widget.TextView[contains(@text,'设置')]")

        '''
            关于我们页面版本信息内容测试
        '''
        # 点击关于我们按钮
        self.click_by_id("com.netease.ldzww:id/layout_about_us")
        # 点击版本按钮并获取版本信息进行断言
        text = self.get_text_by_id("com.netease.ldzww:id/tv_version_name")
        assert_equal(text, app_version, msg="版本信息错误")
        # 点击版本页面返回按钮
        self.click_by_id("com.netease.ldzww:id/basicres_iv_back")

        '''
            退出登录测试
        '''
        # 点击退出按钮
        self.click_by_id("com.netease.ldzww:id/btn_login_out")
        # 点击弹窗上的确认按钮
        self.switch_to_alert()
        self.click_by_id("com.netease.ldzww:id/basicres_negativeButton")
