import json


def read_json(filename):
    filepath = "../data/"+filename
    with open(filepath,"r",encoding="utf-8")as f:
        return json.load(f)
if __name__ == '__main__':
    print(read_json("calc.json"))
    print("--" * 30)
    """
        需求：[(),()] 
        实际格式：{'calc_001': {'a': 1, 'b': 2, 'expect': 3}, 'calc_002': {'a': 9, 'b': 0, 'expect': 9}, 'calc_003': {'a': 12392332, 'b': 23403, 'expect': 12415735}}
        解决：
            1. 新建空列表
            2. 遍历 values()获取所有的值
                3. 列表.append(())
    """
    arrs = []
    for data in read_json("calc.json").values():
        arrs.append((data.get("a"),
                     data.get("b"),
                     data.get("expect")))
    print(arrs)