# coding:utf-8
from nose.tools import istest, nottest
from config import email, userid, pwd, app_version, nickname
import suite.zww.zww_bt_suite as suite
from tool.driver import Appium


@istest
class ZwwBasicTest(Appium):

    @istest
    def zww_basic_test(self):
        suite.ZwwLoginCase().zww_login_case(email, pwd)
        suite.ZwwAdminCase().zww_admin_case(nickname, userid)
        suite.ZwwAddressCase().zww_address_case()
        suite.ZwwContactCustomerCase().zww_contact_customer_case()
        suite.ZwwHasCapturedCase().zww_has_captured_case()
        suite.ZwwCapturedRecordCase().zww_captured_record_case()
        suite.ZwwSettingsCase().zww_settings_case(app_version)
        suite.ZwwIndexPageCase().zww_index_page_case()

        self.driver.quit()
