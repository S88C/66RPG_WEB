def read_txt(filename):
    file = "../data/" + filename + ".txt"
    with open(file, "r", encoding="utf-8")as f:
        # 读取所有行
        return f.readlines()


"""
    预期：列表嵌套元素 列表嵌套列表
    问题：
        1. 去除换行符 strip():去除字符串前后空格、换行符
        2. 拆分字符串 split(",")：根据指定字符拆分字符串，以列表的形式返回
    读取：
        f.read() # 读取所有数据
        f.readline() # 读取单行
        f.readlines() # 读取所有行 一行为一组测试数据，所以使用！
"""
if __name__ == '__main__':
    print(read_txt('search'))
    print("--" * 30)

    arrs = []
    for data in read_txt('search'):
        arrs.append(tuple(data.strip().split(",")))
    print(arrs[1::])
