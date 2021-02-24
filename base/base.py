from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from base.get_logger import GetLogger
import sys

# 获取日志入口
log = GetLogger().get_logger()


class Base:
    # 初始化方法
    def __init__(self, driver):
        log.info("正在初始化获取driver对象：{}".format(driver))
        self.driver = driver

    # 获取元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("正在查找：{} 元素, 最多等待：{}秒".format(loc, timeout))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        log.info("正在点击：{} 元素".format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        log.info("正在输入：{} 元素".format(loc))
        # 获取元素
        el = self.base_find_element(loc)
        # 清空
        log.info("正在对：{} 元素清空操作".format(loc))
        el.clear()
        # 输入
        log.info("正在对：{} 元素，输入：{}值".format(loc, value))
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        log.info("正在获取：{} 元素的文本， 值为：".format(loc, self.base_find_element(loc).text))
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        log.info("正在截图操作")
        self.driver.get_screenshot_as_file(
            "../image/{}_{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"), sys.exc_info()[1]))

    # 判断元素是否存在 存在返回：true
    def base_if_is_not_exist(self, loc):
        try:
            log.info("正在判断：{} 元素是否存在".format(loc))
            self.base_find_element(loc, timeout=2)
            log.info("{} 元素是存在！".format(loc))
            return True  # 存在
        except:
            log.info("{} 元素是不存在！".format(loc))
            return False  # 不存在

    # 切换iframe表单方法
    def base_switch_to_frame(self, frame):
        # 根据frame的id 、name、frame元素
        self.driver.switch_to.frame(frame)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 点击首页
    def base_click_index(self):
        loc = By.CSS_SELECTOR, ".logo>img"
        self.base_click(loc)

    # 切换窗口方法--> 调用
    def base_switch_to_window(self, title):
        self.driver.switch_to.window(self.base_get_handle(title))

    # 点击提示框的确定
    def base_click_popup_ok(self):
        self.driver.switch_to.alert.accept()

    # 点击提示框的取消
    def base_click_popup_on(self):
        self.driver.switch_to.alert.dismiss()

    # 滑动滚动条
    def base_slide_scrollbar(self, X=0, Y=500):
        js = "window.scrollTo(%d,%d)" % (X, Y)
        log.info("正在滑动滚动条")
        self.driver.execute_script(js)

    # 拼接游戏界面的title并跳转
    def base_now_game_title(self, gamename, authorname):
        title = gamename + " | " + authorname + " | 橙光作品"
        log.info("即将跳转title%s:" % title)
        self.base_switch_to_window(title)

    # 获取提示框的文本
    def base_get_popup(self):
        return self.driver.switch_to.alert.text
        # alert = self.driver.switch_to.alert
        # 处理弹出框 text、accept、dismiss
        # 获取文本
        # return alert.text
        # return text

    # 获取指定窗口handle
    def base_get_handle(self, title):
        # 遍历 当前所有窗口的handle
        for handle in self.driver.window_handles:
            # 切换到当前遍历handle
            self.driver.switch_to.window(handle)
            # 判断当前窗口title是否等于 参数title
            if self.driver.title == title:
                return handle

    # def base_switch_to_window(self, title):
    #     for handle in self.driver.window_handles:
    #         self.driver.switch_to.window(handle)
    #         if self.driver.title == title:
    #             break

    """
        思路：
            1. 切换方法 要 handle
            2. 查找handle
    """
