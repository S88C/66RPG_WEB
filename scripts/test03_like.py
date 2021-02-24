import unittest
from base.get_driver import GetDriver
from parameterized import parameterized
from base.read_txt import read_txt
from page.page_like import PageLike
from page.page_login import PageLogin
from base.get_logger import GetLogger

# 获取日志入口
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt('like'):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1::]


class TestLike(unittest.TestCase):
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
        self.like = PageLike(self.driver)

    # 结束
    def tearDown(self):
        # 关闭driver
        log.info("点赞测试完成，正在进行关闭driver操作")
        GetDriver().quit_driver()

    # 测试点赞方法
    @parameterized.expand(get_data)
    def test_like(self, gamename, authorname):
        try:
            # 调用点赞业务方法
            log.info("调用点赞业务方法")
            self.like.page_lick(gamename, authorname)
            state = self.like.page_get_like_state()
            self.assertEqual(state, "已点赞")
        except Exception as e:
            # 日志
            log.error(e)
            raise
