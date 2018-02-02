from nose.tools import assert_equal
from tool.deco import exe_deco
from tool.driver import Appium

'''
	个人中心测试
'''


class ZwwAdminCase(Appium):

    @exe_deco
    def zww_admin_case(self, nickname, userid):
        # 关闭弹窗
        self.click_by_id("com.netease.ldzww:id/iv_fresher_dialog_close")
        # 点击个人中心按钮
        self.click_by_id("com.netease.ldzww:id/iv_enter_mine")
        # 点击头像
        self.click_by_id("com.netease.ldzww:id/iv_user_head")
        # 获取userid并进行断言
        text = self.get_text_by_id("com.netease.ldzww:id/tv_user_id")
        assert_equal(text, userid, msg="用户userid错误")
        # 获取nickname并进行断言
        text = self.get_text_by_id("com.netease.ldzww:id/tv_nick_name")
        assert_equal(text, nickname, msg="用户nickname错误")
        # 点击返回按钮
        self.click_by_id("com.netease.ldzww:id/basicres_iv_back")
