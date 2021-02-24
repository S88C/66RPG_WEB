import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
from base.read_txt import read_txt
from page.page_login import PageLogin
from base.get_logger import GetLogger

# 获取日志入口
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt('login'):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1::]


class TestLogin(unittest.TestCase):
    driver = None
    login = None

    # 初始化
    @classmethod
    def setUpClass(cls):
        log.info("正在初始化获取driver对象")
        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 获取PageLogin实例对象
        cls.login = PageLogin(cls.driver)
        log.info("获取PageLogin页面对象：{}".format(cls.login))

    # 结束
    @classmethod
    def tearDownClass(cls):
        log.info("登录测试完成，正在进行关闭driver操作")
        # 关闭浏览器
        GetDriver().quit_driver()

    # 测试登录方法
    @parameterized.expand(get_data)
    def test_login(self, username, pwd, success, expect):
        # 调用登录业务方法
        log.info("调用登录业务方法")
        # print("登录数据：", username, pwd, success)
        self.login.page_qqlogin(username, pwd)
        # 假设 success = "true" 为正向用例
        if success == "hello":
            try:
                # 先保存登录后的信息，给断言实用

                log.info("正在点击用户头像")
                self.login.page_click_user_btn()
                # 切换到个人中心页面
                self.login.page_now_user(expect)
                result = self.login.page_get_nickname().replace(" ", "")
                log.info("获取登录后的昵称信息:{}".format(result))
                # 断言 登录成功
                log.info("断言是否登录成功")
                self.assertEqual(expect, result)
                log.info("登录成功！")
                log.info("点击退出业务操作")
                # 点击退出
                self.login.page_click_logout()
                log.info("正在点击提示框")
                # 点击提示框
                self.login.base_click_popup_ok()
                log.info("点击确定成功")
            except Exception as e:
                log.error(e)
                # 截图
                self.login.base_get_image()
                # 抛异常
                raise
            finally:
                # 点击登录连接
                self.login.page_click_login_qsn()
                # 点击登录链接
                log.info("点击登录连接操作")
                self.login.page_click_login_link()
        # 逆向用例
        else:
            try:
                print("逆向断言")
                log.info("逆向用例，正在断言异常提示信息：{}".format(self.login.page_get_error_info()))
                self.assertEqual(expect, self.login.page_get_error_info())
                log.info("异常提示信息，断言成功！")
                log.info("点击异常提示框，确定按钮")
                # 点击逆向登录提示框按钮
                self.login.page_click_error_btn()

            except Exception as e:
                log.error(e)
