import page
from base.base import Base
from base.get_logger import GetLogger
from base.SlideVerificationCode import SlideVerificationCode
import time

# 获取日志入口
log = GetLogger().get_logger()


class PageLogin(Base):
    # 关闭青少年弹框
    def page_click_login_qsn(self):
        log.info("点击青少年弹窗操作")
        self.base_click(page.home_qsn)

    # 点击登录链接
    def page_click_login_link(self):
        log.info("点击登录操作")
        self.base_click(page.login_link)

    # 跳转登录页面
    def page_click_now_login(self):
        log.info("即将跳转至登录页面")
        self.base_switch_to_window(page.login_on_delivery_title)

    # 输入用户名
    def page_input_username(self, username):
        log.info("正在输入用户名")
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        log.info("正在输入密码")
        self.base_input(page.login_pwd, pwd)

    # 点击协议复选框
    def page_click_login_checkbox(self):
        log.info("正在点击复选框")
        self.base_click(page.login_checkbox)

    # 输入验证码
    # def page_input_verify_code(self, verify_code):
    #    self.base_input(page.login_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_btn(self):
        log.info("正在点击登录按钮")
        self.base_click(page.login_btn)

    # 滑动QQ验证码
    def page_slid_verify_code(self):
        # 判断是否需要滑动验证码
        if_verify_code = self.base_if_is_not_exist(page.home_qsn)
        if not if_verify_code:
            # 切换到验证码的iframe
            log.info("正在处理验证码")
            time.sleep(3)
            verify_code = self.base_find_element(page.login_qq_verify_code)
            self.base_switch_to_frame(verify_code)
            log.info("切换验证码iframe成功")
            # 4.2选择拖动滑块的节点
            time.sleep(3)
            slide_element = self.driver.find_element_by_id('tcaptcha_drag_thumb')

            #  模拟拖到滑块进行识别
            sc = SlideVerificationCode(save_image=True, driver=self.driver)

            # 获取滑块图片的节点id="slideBlock"
            slideBlock_ele = self.driver.find_element_by_id('slideBlock')
            # 获取背景图片节点id="slideBg"
            slideBg = self.driver.find_element_by_id('slideBg')

            # 4.3计算滑动距离，电脑缩放比例需要为100% 才可确保减去的正确
            distance = sc.get_element_slide_distance(slideBlock_ele, slideBg)
            print("滑动的距离为：", distance)
            log.info("滑动的距离为：", distance)
            # 滑动距离误差校正，按照比例来进行计算，然后减去 第一部分距离
            distance = distance * (280 / 680) - 31

            print("校验后的滑动距离", distance)
            log.info("校验后的滑动距离", distance)
            # 4.4、进行滑动
            sc.slide_verification(self.driver, slide_element, distance=distance)
            log.info("验证码处理完成")
        else:
            log.info("无需滑动验证码")

    # 点击QQ登录
    def page_cilck_qqlogin(self):
        log.info("正在点击QQ登录")
        self.base_click(page.login_qq)

    # 切换ifame
    def page_switch_qqifame(self):
        qqifame = self.base_find_element(page.login_qq_iframe)
        log.info("切换ifame为QQifame")
        self.base_switch_to_frame(qqifame)

    # 点击账号密码登录
    def page_clck_qqnumber(self):
        log.info("点击QQ登录界面的账号密码登录")
        self.base_click(page.login_qq_number)

    # 输入QQ号
    def page_input_qquser(self, user):
        log.info("正在输入QQ号")
        self.base_input(page.login_qq_user, user)

    # 输入QQ密码
    def page_input_qqpwd(self, pwd):
        log.info("正在输入QQ密码")
        self.base_input(page.login_qq_pwd, pwd)

    # 点击授权登录按钮
    def page_click_logingo(self):
        time.sleep(2)
        log.info("正在点击登录按钮")
        self.base_click(page.login_qq_go)
        log.info("点击登录成功")

    # 判断是否需要滑动验证码
    def page_if_verify_code(self):
        if_verify_code = self.base_if_is_not_exist(page.home_qsn)
        return if_verify_code

    # 获取异常提示信息
    def page_get_error_info(self):
        log.info("正在获取异常提示信息")
        return self.base_get_text(page.login_error_info)

    # 点击异常提示信息确定按钮
    def page_click_error_btn(self):
        log.info("正在点击异常提示信息的确认按钮")
        self.base_click(page.login_error_btn_ok)

    # 切换到个人中心网页
    def page_now_user(self, expect):
        title = page.login_user_title + expect
        log.info("正在切换到%s界面" % title)
        self.base_switch_to_window(title)

    # 点击用户头像
    def page_click_user_btn(self):
        log.info("正在点击用户头像")
        self.base_click(page.login_user_btn)

    # 获取登录后昵称
    def page_get_nickname(self):
        log.info("正在获取用户昵称")
        return self.base_get_text(page.login_nickname)

    # 点击退出
    def page_click_logout(self):
        log.info("正在点击退出按钮")
        self.base_click(page.login_logout)

    # 组合登录业务方法_QQ账号登录
    def page_qqlogin(self, username, pwd):
        # 关闭青少年弹窗
        self.page_click_login_qsn()
        # 点击登录链接
        self.page_click_login_link()
        # 跳转至登录页面
        self.page_click_now_login()
        log.info("正在执行登录操作，测试数据为：{}、{}".format(username, pwd))
        # 点击QQ登录
        self.page_cilck_qqlogin()
        # 切换QQifame
        self.page_switch_qqifame()
        # 点击账号密码登录
        self.page_clck_qqnumber()
        # 输入QQ号
        self.page_input_qquser(username)
        # 输入密码
        self.page_input_qqpwd(pwd)
        # 点击授权并登录
        self.page_click_logingo()
        # 滑动验证码
        self.page_slid_verify_code()
        # 关闭青少年弹窗
        self.page_click_login_qsn()
