# coding:utf-8
import os
from os.path import abspath,join,dirname

from config import desired_caps_zww,command_executor
from tool.driver import click_by_id,input_by_id,click_by_xpath,get_text_by_id

from appium import webdriver

from nose.tools import istest,nottest,assert_equal,assert_in
from nose_ittr import IttrMultiplier, ittr
from nose import with_setup

from selenium.webdriver.support.wait import WebDriverWait


root_path = dirname(dirname(__file__))
data_path = join(root_path,'data')
_image = lambda img_name:abspath(
	join(data_path,img_name)
)


@istest
class ZwwLoginTest():

	def __init__(self):
		self.driver = webdriver.Remote(command_executor,desired_caps_zww)
		self.email = "用户名"
		self.userid = "用户id（个人中心页面可见）"
		self.pwd = "用户密码"
		self.app_version = "版本V1.0.3"

	@istest
	def zww_basic_test(self):
		driver = self.driver

		'''
			1. 登录测试
		'''
		#点击邮箱登录按钮
		email_btn_id = "com.netease.ldzww:id/btn_email_login"
		driver = click_by_id(driver,email_btn_id)
		#输入用户名
		email_id = "com.netease.ldzww:id/edt_email"
		email = self.email
		driver = input_by_id(driver,email_id,email)
		#输入密码
		pwd_id = "com.netease.ldzww:id/edt_pwd"
		pwd = self.pwd
		driver = input_by_id(driver,pwd_id,pwd)
		#点击登录按钮
		login_btn_id = "com.netease.ldzww:id/btn_login"
		driver = click_by_id(driver,login_btn_id)

		'''
			2. 个人中心跳转测试
		'''
		#点击个人中心按钮
		mine_id = "com.netease.ldzww:id/iv_enter_mine"
		driver = click_by_id(driver,mine_id)

		'''
			3. 用户userid测试
		'''
		#获取userid并进行断言
		userid_id = "com.netease.ldzww:id/tv_user_id"
		driver,text = get_text_by_id(driver,userid_id)
		assert_equal(text,self.userid,msg="用户userid错误")

		'''
			4.1 我的地址页面新增测试
		'''
		myaddr_id = "com.netease.ldzww:id/item_mine_address"
		driver = click_by_id(driver,myaddr_id)
		driver.wait_activity(".usercenter.activity.AddressListActivity", 30, 1)
		#print(driver.page_source)
		#点击新增地址
		addaddr_id = "com.netease.ldzww:id/layout_add_address"
		driver = click_by_id(driver,addaddr_id)
		#输入收货人信息
		name_id = "com.netease.ldzww:id/et_address_name"
		driver = input_by_id(driver,name_id,"张三")
		#输入联系电话
		phone_id = "com.netease.ldzww:id/et_address_mobile"
		driver = input_by_id(driver,phone_id,"18686666666")
		#选择所在地区
		addr_id = "com.netease.ldzww:id/tv_address_area"
		driver = click_by_id(driver,addr_id)
		#点击确定按钮保存地址
		driver.switch_to_alert()
		save_id = "com.netease.ldzww:id/bt_save"
		driver = click_by_id(driver,save_id)
		#输入详细信息
		detail_id = "com.netease.ldzww:id/et_address_detail"
		driver = input_by_id(driver,detail_id,"张三的家")
		#点击保存按钮
		save_id = "com.netease.ldzww:id/btn_save"
		driver = click_by_id(driver,save_id)

		'''
			4.2 我的地址页面编辑保存测试
		'''
		#点击编辑按钮
		edit_id = "com.netease.ldzww:id/img_edit"
		driver = click_by_id(driver,edit_id)
		#编辑姓名
		input_by_id(driver,name_id,"张四")
		#点击保存按钮
		click_by_id(driver,save_id)

		'''
			4.3 我的地址页面删除测试
		'''
		#点击删除按钮（只有一个地址记录所以页面上删除按钮也只有一个）
		del_id = "com.netease.ldzww:id/img_delete"
		driver = click_by_id(driver,del_id)
		#点击弹窗上的确认按钮
		driver.switch_to_alert()
		sure_id = "com.netease.ldzww:id/basicres_negativeButton"
		driver = click_by_id(driver,sure_id)

		'''
			4.4 我的地址页面空页面内容测试
		'''
		#空页面截图
		driver.get_screenshot_as_file(_image("actual_myaddr_empty.png"))
		#检查空页面提示
		tip_id = "com.netease.ldzww:id/tv_no_item_tip"
		text = get_text_by_id(driver,tip_id)
		#打印出来text是个元组，需要取索引第一位才是text内容
		#对空页面提示内容进行断言
		assert_in(text[1],"还没有添加地址哦～",msg="空地址页面提示错误")
		#点击返回按钮
		back_id = "com.netease.ldzww:id/basicres_iv_back"
		driver = click_by_id(driver,back_id)

		'''
			5. 我的娃娃页面测试
		'''
		#点击我的娃娃按钮
		mywawa_id = "com.netease.ldzww:id/item_mine_has_captured"
		driver = click_by_id(driver,mywawa_id)
		#点击立即抓娃娃按钮（页面无记录）
		main_id = "com.netease.ldzww:id/btn_main"
		driver = click_by_id(driver,main_id)
		#点击个人中心按钮
		driver = click_by_id(driver,mine_id)
		#点击我的娃娃按钮
		driver = click_by_id(driver,mywawa_id)
		#点击我的娃娃页面返回按钮
		back_id = "com.netease.ldzww:id/iv_back"
		driver = click_by_id(driver,back_id)

		'''
			6.1 设置页面测试
		'''
		#点击设置按钮
		setting_xpath = "//android.widget.TextView[contains(@text,'设置')]"
		driver = click_by_xpath(driver,setting_xpath)

		'''
			6.2 关于我们页面版本信息内容测试
		'''
		#点击关于我们按钮
		about_id = "com.netease.ldzww:id/layout_about_us"
		driver = click_by_id(driver,about_id)
		#点击版本按钮并获取版本信息进行断言
		version_id = "com.netease.ldzww:id/tv_version_name"
		driver,text = get_text_by_id(driver,version_id)
		assert_equal(text,self.app_version,msg="版本信息错误")
		#点击版本页面返回按钮
		back_id = "com.netease.ldzww:id/basicres_iv_back"
		driver = click_by_id(driver,back_id)

		'''
			6.3 退出登录测试
		'''
		#点击退出按钮
		logout_id = "com.netease.ldzww:id/btn_login_out"
		driver = click_by_id(driver,logout_id)
		#点击弹窗上的确认按钮
		driver.switch_to_alert()
		sure_id = "com.netease.ldzww:id/basicres_negativeButton"
		driver = click_by_id(driver,sure_id)

		'''
			6.4 首页协议文字内容测试
		'''
		#获取首页协议信息文字内容并进行断言
		protocol_id = "com.netease.ldzww:id/tv_user_use_protocol"
		driver,text = get_text_by_id(driver,protocol_id)
		self.driver = driver
		assert_equal(text,"用户使用协议与隐私条款",msg="登录页协议文字内容错误")

	def __del__(self):
		self.driver.quit()