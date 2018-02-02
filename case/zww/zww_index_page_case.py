from nose.tools import assert_equal
from tool.deco import exe_deco
from tool.driver import Appium

'''
	首页协议文字内容测试
'''


class ZwwIndexPageCase(Appium):

    @exe_deco
    def zww_index_page_case(self):
        # 获取首页协议信息文字内容并进行断言
        text = self.get_text_by_id("com.netease.ldzww:id/tv_user_use_protocol")
        assert_equal(text, "用户使用协议与隐私条款", msg="登录页协议文字内容错误")
