from tool.deco import exe_deco
from tool.driver import Appium

'''
	抓娃娃记录页面测试
'''


class ZwwCapturedRecordCase(Appium):

    @exe_deco
    def zww_captured_record_case(self):
        # 点击抓娃娃记录按钮
        self.click_by_id("com.netease.ldzww:id/item_captured_record")
        # 点击立即抓娃娃按钮
        self.click_by_id("com.netease.ldzww:id/btn_main")
        # 点击个人中心按钮
        self.click_by_id("com.netease.ldzww:id/iv_enter_mine")
