from nose.tools import assert_in
from tool.deco import exe_deco
from tool.driver import Appium

'''
	我的地址页面测试
'''


class ZwwAddressCase(Appium):

    @exe_deco
    def zww_address_case(self):
        '''
            新增地址测试
        '''
        # 个人中心页面点击用户头像
        self.click_by_id("com.netease.ldzww:id/iv_user_head")
        # 点击我的地址按钮
        self.click_by_id("com.netease.ldzww:id/rl_mine_address")
        self.wait_activity(".usercenter.activity.AddressListActivity")
        # 点击新增地址
        self.click_by_id("com.netease.ldzww:id/layout_add_address")
        # 输入收货人信息
        self.input_by_id("com.netease.ldzww:id/et_address_name", "张三")
        # 输入联系电话
        self.input_by_id("com.netease.ldzww:id/et_address_mobile", "18686666666")
        # 选择所在地区
        self.click_by_id("com.netease.ldzww:id/tv_address_area")
        # 点击确定按钮保存地址
        self.switch_to_alert()
        self.click_by_id("com.netease.ldzww:id/bt_save")
        # 输入详细信息
        self.input_by_id("com.netease.ldzww:id/et_address_detail", "张三的家")
        # 点击保存按钮
        self.click_by_id("com.netease.ldzww:id/btn_save")

        '''
            编辑保存测试
        '''
        # 点击编辑按钮
        self.click_by_id("com.netease.ldzww:id/img_edit")
        # 编辑姓名
        self.input_by_id("com.netease.ldzww:id/et_address_name", "张四")
        # 点击保存按钮
        self.click_by_id("com.netease.ldzww:id/btn_save")

        '''
            删除地址测试
        '''
        # 点击删除按钮（只有一个地址记录所以页面上删除按钮也只有一个）
        self.click_by_id("com.netease.ldzww:id/img_delete")
        # 点击弹窗上的确认按钮
        self.switch_to_alert()
        self.click_by_id("com.netease.ldzww:id/basicres_negativeButton")

        '''
            空页面内容测试
        '''
        # 检查空页面提示
        text = self.get_text_by_id("com.netease.ldzww:id/tv_no_item_tip")
        # 打印出来text是个元组，需要取索引第一位才是text内容
        # 对空页面提示内容进行断言
        assert_in(text[1], "还没有添加地址哦～", msg="空地址页面提示错误")
        # 点击返回按钮
        self.click_by_id("com.netease.ldzww:id/basicres_iv_back")
        # 点击返回按钮
        self.click_by_id("com.netease.ldzww:id/basicres_iv_back")
