from selenium.webdriver.common.by import By

"""以下为测试服务器地址"""
url = "https://66rpg.com"
"""以下为登录页面配置信息"""
# 青少年模式按钮
home_qsn = By.CSS_SELECTOR, ".qsnClose"
# 登录连接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 登录界面标题
login_on_delivery_title = "用户登录|橙光"
# 输入用户名
login_username = By.CSS_SELECTOR, "#username"
# 输入密码
login_pwd = By.CSS_SELECTOR, "#password"
# 服务协议复选框
login_checkbox = By.NAME, "agreement"
# 输入验证码
login_verify_code = By.CSS_SELECTOR, "#verify_code"
# 点击登录按钮
login_btn = By.XPATH, "/html/body/div[@class='wrapper']/div[@class='content clr']/div[@class='content_right fl']/div[" \
                      "@class='login_ct_wrapper']/div[@class='login_btn_box']/input[@class='login_btn fl'] "
# 滑动验证码_拖动滑块的节点
qq_slid = By.CSS_SELECTOR, "#tcaptcha_drag_thumb"
# 滑动验证码_滑块图片
qq_slid_img = By.CSS_SELECTOR, "#slideBlock"
# 滑动验证码_背景图
qq_slid_bg = By.CSS_SELECTOR, "#slideBg"
# 获取异常提示信息
login_error_info = By.CSS_SELECTOR, ".layui-layer-content"
# QQ登录
login_qq = By.XPATH, "/html/body/div[@class='wrapper']/div[@class='content clr']/div[@class='content_right fl']/div[" \
                     "@class='login_ct_wrapper']/div[@class='shortcut_login clr']/a[@class='fl third-party-btn QQ'] "
# 切换QQ登录iframe
login_qq_iframe = By.CSS_SELECTOR, "#ptlogin_iframe"
# 账号密码登录元素
login_qq_number = By.CSS_SELECTOR, "#switcher_plogin"
# QQ账号输入框
login_qq_user = By.XPATH, "//input[@id='u']"
# QQ密码输入框
login_qq_pwd = By.XPATH, "//input[@id='p']"
# 授权并登录按钮
login_qq_go = By.CSS_SELECTOR, "#login_button"
# QQ验证码ifamr
login_qq_verify_code = By.CSS_SELECTOR, "#tcaptcha_iframe"
# 点击异常提示框 确认
login_error_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
# 个人中心按钮
login_user_btn = By.CSS_SELECTOR, ".user_headers"
# 个人中心页面
login_user_title = "橙光-"
# 用户昵称
login_nickname = By.XPATH, "//*[@id='main']/div/div[4]/div[1]/div/dl/dd[1]/span[2]/a"
# 退出
login_logout = By.PARTIAL_LINK_TEXT, "退出"

"""以下为搜索框数据信息"""
# 输入作品名
search_input = By.XPATH, "/html/body/div[2]/div/div[3]/form/input"
# 点击搜索按钮
search_btn = By.XPATH, "/html/body/div[2]/div/div[3]/form/span"
# 第一个作品的封面，点击后进入游戏页面
search_game_img = By.XPATH, "//*[@id='search_result']/li[1]/div/div/div[1]/a/img"
# 游戏名
search_game_name = By.XPATH, "//*[@id='search_result']/li[1]/div/div/div[2]/h5/a[1]"
# 搜索界面title
search_title = '橙光 搜索页 | 找作品'
# 作者名称
search_author_name = By.XPATH, "//*[@id='search_result']/li[1]/div/div/div[2]/h5/a[2]"
# 首页title
search_home_title = "首页 - 橙光"

"""以下方法为点赞功能配置数据"""
# 点赞状态文字
like_txt = By.XPATH, "//*[@id='game']/div[3]/div[1]/div[1]/span"
# 点击按钮
like_btn = By.XPATH, "//*[@id='game']/div[3]/div[1]/div[1]/i"
# 登录ifame
like_loginifame = By.CSS_SELECTOR, "#js-cross-login-iframe"
# 收货人
order_person = By.CSS_SELECTOR, ".consignee>b"
# 提交订单
order_submit = By.CSS_SELECTOR, ".Sub-orders"
# 获取订单结果
order_result = By.CSS_SELECTOR, ".erhuh>h3"

"""以下为收藏功能配置数据"""
# 收藏状态文字
collect_txt = By.XPATH, "//*[@id='game']/div[3]/div[1]/div[3]/span"
# 收藏按钮
collect_btn = By.XPATH, "//*[@id='game']/div[3]/div[1]/div[3]/i"
# 选择默认精选集
collect_checkbox = By.XPATH, "//*[@id='folderScroll']/div[1]/div[3]/div/label[1]/span[1]"
# 精选集确定按钮
collect_submit = By.XPATH, "/html/body/div[14]/div/div[3]/input"
# Toast提示框
collect_toast = By.XPATH, "/html/body/div[10]"

"""以下为评论功能配置数据"""
# 竖屏评论输入框
comment_input = By.XPATH, "//*[@id='game']/div[2]/div[3]/div[2]/input"
# 竖屏发表按钮
comment_sed = By.XPATH, "//*[@id='game']/div[2]/div[3]/div[2]/button"
# Toast提示框
comment_toast = By.XPATH, "/html/body/div[19]/span"
# Toast异常提示框
comment_error_toast = By.XPATH, "/html/body/div[19]/span"
