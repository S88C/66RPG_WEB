import unittest
from parameterized import parameterized
from base.get_driver import GetDriver
from base.read_txt import read_txt
from page.page_search import PageSearch
from base.get_logger import GetLogger

# 获取日志入口
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt('search'):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1::]


class TestSearch(unittest.TestCase):
    driver = None
    search = None

    # 初始化
    @classmethod
    def setUpClass(cls):
        log.info("正在初始化获取driver对象")
        # 获取driver
        cls.driver = GetDriver().get_driver()
        # 获取PageLogin实例对象
        cls.search = PageSearch(cls.driver)
        log.info("获取PageSearch页面对象：{}".format(cls.search))
        log.info("点击青少年弹窗操作")
        # 点击青少年弹窗按钮
        cls.search.page_click_search_qsn()

    # 结束
    @classmethod
    def tearDownClass(cls):
        log.info("搜索测试完成，正在进行关闭driver操作")
        # 关闭浏览器
        GetDriver().quit_driver()

    # 测试登录方法
    @parameterized.expand(get_data)
    def test_search(self, search_txt, author_expect):
        try:
            # 调用搜索业务方法
            log.info("正在调用搜索业务方法")
            self.search.page_search(search_txt)
            result = self.search.page_get_game_name()
            author = self.search.page_get_author_name()
            log.info("当前游戏名称为:{},作者名为:{}".format(result, author))
            log.info("当前游戏名为:%s,预期游戏名为:%s" % (result, search_txt))
            # 断言
            self.assertEqual(result, search_txt)
            log.info("断言成功")
            log.info("当前作者名为:%s,预期作者名为:%s" % (author, author_expect))
            self.assertEqual(author, author_expect)
            log.info("断言成功")
            self.search.page_close_window_to_home()
        except Exception as e:
            # 日志
            log.error(e)
            self.search.page_close_window_to_home()
            raise
