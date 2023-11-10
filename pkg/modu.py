import json


def triangle_zhonxin():
    """Return the triangle_zhonxin on x and y."""
    x1, y1 = input("請輸入頂點 a 的坐標：").split(',')
    x2, y2 = input("請輸入頂點 b 的坐標：").split(',')
    x3, y3 = input("請輸入頂點 c 的坐標：").split(',')
    a = x1, y1
    b = x2, y2
    c = x3, y3
    type(a)
    type(b)
    type(c)
    x = round(float((int(x1) + int(x2) + int(x3)) / 3))
    y = round(float((int(y1) + int(y2) + int(y3)) / 3))
    print("-" * 30)
    print(f'{"此三角形的重心為："}', end="")
    return (x, y)


def read_json(file_name: str) -> dict:
    with open('menu.json', 'r', encoding='UTF-8') as f:
        """json.load() 讀取 JSON 檔案，轉換為 Python 的 dict"""
        pi_dict = json.load(f)
        return pi_dict


def print_json(data: dict) -> None:
    """將字典轉爲 json 字串後輸出到螢幕"""
    new_menu_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(new_menu_str)


def process_data(data: dict, discount: float) -> None:
    """打折"""
    for category in data['categories']:
        for item in category['items']:
            item['price'] = round(item['price'] * discount)


def write_json(data: dict, file_name: str) -> None:
    """ json.dump() 將 dict 轉成 JSON 格式，寫入 JSON 檔案"""
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
