import unittest
from tool.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("../scripts/")
# 获取报告存储文件流
with open("../report/66rpg自动化测试报告.html", "wb")as f:
    # 实例化HTMLTestRunner 并调用run
    HTMLTestRunner(stream=f).run(suite)
