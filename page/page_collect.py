import page
from base.base import Base
from base.get_logger import GetLogger
from .page_search import PageSearch
import time

# 获取日志入口
log = GetLogger().get_logger()


class PageCollect(Base):
    # 点击游戏封面
    def page_click_game_img(self):
        log.info("正在点击游戏封面")
        self.base_click(page.search_game_img)

    # 获取游戏收藏状态
    def page_get_collect_state(self):
        log.info("正在获取收藏状态")
        return self.base_get_text(page.collect_txt)

    # 点击收藏按钮
    def page_click_collect_btn(self):
        log.info("正在点击收藏按钮")
        self.base_click(page.collect_btn)

    # 点击精选集的复选框
    def page_collect_checkbox(self):
        log.info("正在点击复选框")
        self.base_click(page.collect_checkbox)

    # 点击精选集的确认按钮
    def page_click_collect_submit(self):
        log.info("正在点击确认按钮")
        self.base_click(page.collect_submit)

    # 获取Toast
    def page_get_collect_toast(self):
        return self.base_get_text(page.collect_toast)

    # 组合收藏业务方法
    def page_collect(self, gamename, authorname):
        # 通过搜索方法来搜索作品
        PageSearch(self.driver).page_search(gamename)
        # 点击作品封面
        self.page_click_game_img()
        # 跳转游戏界面
        self.base_now_game_title(gamename, authorname)
        # 滑动滚动条
        self.base_slide_scrollbar()
        # 获取收藏状态
        state = self.page_get_collect_state()
        # 点击收藏按钮
        self.page_click_collect_btn()
        # 点击精选集复选框
        self.page_collect_checkbox()
        # 点击确定按钮
        self.page_click_collect_submit()
        return state

