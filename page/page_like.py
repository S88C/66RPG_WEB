import page
from base.base import Base
from base.get_logger import GetLogger
from .page_search import PageSearch
import time

# 获取日志入口
log = GetLogger().get_logger()


class PageLike(Base):
    # 关闭青少年弹框
    def page_click_like_qsn(self):
        log.info("正在关闭青少年弹窗")
        self.base_click(page.home_qsn)

    # 点击游戏封面
    def page_click_game_img(self):
        log.info("正在点击游戏封面")
        self.base_click(page.search_game_img)

    # 获取游戏点赞状态
    def page_get_like_state(self):
        log.info("正在获取点赞状态")
        return self.base_get_text(page.like_txt)

    # 点击点赞按钮
    def page_click_like_btn(self):
        log.info("正在点击点赞按钮")
        self.base_click(page.like_btn)

    # 获取弹窗的文本
    # def page_get_popup_text(self):
    #   t = self.base_get_popup()
    #   return t

    # 点击弹窗的确定
    def page_click_popup_ok(self):
        log.info("正在点击弹窗的确定")
        self.base_click_popup_ok()

    # 拼接游戏界面的title并跳转
    def page_now_game_title(self, gamename, authorname):
        title = gamename + " | " + authorname + " | 橙光作品"
        log.info("即将跳转title%s:" % title)
        self.base_switch_to_window(title)

    # 关闭当前页面，返回首页
    def page_close_window_to_home(self):
        self.driver.close()
        self.base_switch_to_window(page.search_home_title)

    # 判断点赞状态并执行相应操作
    def page_if_like(self, state):
        if state == "赞一个":
            log.info("当前未点赞，正在进行点赞操作")
            self.page_click_like_btn()
        else:
            log.info("当前已点赞，正在进行点弹窗操作")
            self.page_click_like_btn()
            log.info("点击点赞按钮成功")
            time.sleep(2)
            txt = self.base_get_popup()
            log.info("已获取弹框内容:%s" % txt)
            self.page_click_popup_ok()
            if txt == "您已对此作品点过赞，请不要重复点赞！":
                pass
            else:
                raise

    # 组合点赞业务方法
    def page_lick(self, gamename, authorname):
        # 通过搜索方法来搜索作品
        PageSearch(self.driver).page_search(gamename)
        # 点击作品封面
        self.page_click_game_img()
        # 跳转游戏界面
        self.page_now_game_title(gamename, authorname)
        # 滑动滚动条
        self.base_slide_scrollbar()
        # 获取点赞文本
        state = self.page_get_like_state()
        log.info("当前点赞文本为:%s" % state)
        # 判断点赞状态并执行相应操作
        self.page_if_like(state)
