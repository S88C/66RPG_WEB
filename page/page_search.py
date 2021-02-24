import page
from base.base import Base
from base.get_logger import GetLogger
import time

# 获取日志入口
log = GetLogger().get_logger()


class PageSearch(Base):
    # 关闭青少年弹框
    def page_click_search_qsn(self):
        log.info("正在关闭青少年弹窗")
        self.base_click(page.home_qsn)

    # 输入搜索内容
    def page_input_search_content(self, gamename):
        log.info("正在输入搜索内容:%s" % gamename)
        self.base_input(page.search_input, gamename)

    # 点击搜索按钮
    def page_click_search_btn(self):
        log.info("正在点击搜索按钮")
        self.base_click(page.search_btn)

    # 切换到搜索界面
    def page_now_search(self):
        log.info("正在切换到搜索界面")
        self.base_switch_to_window(page.search_title)

    # 获取作者昵称
    def page_get_author_name(self):
        log.info("正在获取作者昵称")
        return self.base_get_text(page.search_author_name)

    # 获取作品名
    def page_get_game_name(self):
        log.info("正在获取作品名称")
        return self.base_get_text(page.search_game_name)

    # 返回首页
    def page_now_home(self):
        log.info("正在返回首页")
        self.base_switch_to_window(page.search_home_title)

    # 关闭当前页面，返回首页
    def page_close_window_to_home(self):
        log.info("正在关闭窗口")
        self.driver.close()
        log.info("正在前往首页")
        self.page_now_home()

    # 组合业务方法
    def page_search(self, gamename):
        log.info("正在执行搜索操作，测试游戏名称为：{}".format(gamename))
        self.page_input_search_content(gamename)
        self.page_click_search_btn()
        self.page_now_search()
        log.info("跳转到搜索成功")
