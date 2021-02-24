import unittest
from base.get_driver import GetDriver
from parameterized import parameterized
from base.read_txt import read_txt
from page.page_collect import PageCollect
from page.page_login import PageLogin
from base.get_logger import GetLogger

# 获取日志入口
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt('like'):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1::]


class TestCollect(unittest.TestCase):
    driver = None
    like = None

    # 初始化
    def setUp(self):
        # 获取driver
        log.info("正在初始化获取driver对象")
        self.driver = GetDriver().get_driver()
        # 实例化PageLogin并调用登录成功依赖方法
        log.info("实例化PageLogin")
        PageLogin(self.driver).page_qqlogin(username='487764530', pwd='Sunchao001128')
        # 获取PageLike对象
        log.info("获取PageLike对象")
        self.collect = PageCollect(self.driver)

    # 结束
    def tearDown(self):
        # 关闭driver
        log.info("收藏完成，正在进行关闭driver操作")
        GetDriver().quit_driver()

    # 测试点赞方法
    @parameterized.expand(get_data)
    def test_collect(self, gamename, authorname):
        try:
            # 调用收藏业务方法
            log.info("调用收藏业务方法")
            state = self.collect.page_collect(gamename, authorname)
            log.info("当前收藏状态为:%s" % state)
            print(state)
            result = self.collect.page_get_collect_toast()
            log.info("当前收藏状态为:%s" % state)
            log.info("正在进行断言")
            self.assertNotEqual(state, result)
            log.info("断言成功%s != %s" % (state, result))
        except Exception as e:
            # 日志
            log.error(e)
            raise
