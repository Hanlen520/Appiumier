from tool.deco import exe_deco
from tool.driver import Appium

'''
	我的娃娃页面测试
'''


class ZwwHasCapturedCase(Appium):

    @exe_deco
    def zww_has_captured_case(self):
        # 点击我的娃娃按钮
        self.click_by_id("com.netease.ldzww:id/item_mine_has_captured")
        # 点击立即抓娃娃按钮（页面无记录）
        self.click_by_id("com.netease.ldzww:id/btn_main")
        # 点击个人中心按钮
        self.click_by_id("com.netease.ldzww:id/iv_enter_mine")
        # 点击我的娃娃按钮
        self.click_by_id("com.netease.ldzww:id/item_mine_has_captured")
        # 点击我的娃娃页面返回按钮
        self.click_by_id("com.netease.ldzww:id/iv_back")
