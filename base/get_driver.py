import page
from selenium import webdriver


class GetDriver:
    # 获取driver 单例
    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # cls.driver = webdriver.Firefox()
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        # 为了程序的健壮性， 需要先判断不为空的时候在执行
        if cls.driver:
            cls.driver.quit()
            # 必须 置空
            cls.driver = None
