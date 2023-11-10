from pkg.modu import print_json, process_data, read_json, write_json

x = 0
MENU_FILE = 'menu.json'       # 輸入檔案名稱
OUTPUT_FILE = 'output.json'   # 輸出檔案名稱
menu_data = read_json(MENU_FILE)
print_json(menu_data)
new_dish = {
        "name": "海鮮燉飯",
        "price": 239,
        "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    }
menu_data['categories'][1]['items'].append(new_dish)

discount = float(input("請輸入折扣率(0.0 ~ 0.9)："))
process_data(menu_data, discount)
print_json(menu_data)
write_json(menu_data, OUTPUT_FILE)
