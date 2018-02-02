from nose.tools import assert_equal, assert_in
from tool.deco import exe_deco
from tool.driver import Appium

'''
	客服用例
'''


class ZwwContactCustomerCase(Appium):

    @exe_deco
    def zww_contact_customer_case(self):
        # 点击联系客服按钮
        self.click_by_id("com.netease.ldzww:id/item_contact_customer")
        # 输入文字内容
        self.input_by_id("com.netease.ldzww:id/editTextMessage", "测试内容！随意回复~")
        # 点击表情按钮
        self.click_by_id("com.netease.ldzww:id/emoji_button")
        # 选择表情
        self.click_by_xpath("//android.widget.GridView[contains(@index,0)]")
        # 点击发送按钮
        self.click_by_id("com.netease.ldzww:id/send_message_button")
        # 获取发送内容并断言
        sig = self.wait_by_xpath("//android.widget.TextView[contains(@text,'测试内容！随意回复~')]")
        assert_equal(sig, "OK", msg="客服发送文案出错")
        # 点击返回按钮
        self.click_by_id("com.netease.ldzww:id/iv_back")
