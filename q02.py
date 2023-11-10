e = {'eName': '', 'eSalary': ''}
a = []
sum = 0
avg = 0.00
z = ' '
s1 = "的薪資為"
print("-" * 30)
print(" " * 8 + "員工薪資輸入")
print(" " * 4 + "若姓名處未輸入則代表結束")
print("-" * 30)
while True:
    e["eName"] = input("請輸入姓名:")
    if e["eName"] == "":
        break
    a.append(e["eName"])
    e["eSalary"] = input("請輸入薪資:")
    a.append(e["eSalary"])
    print()
    continue
print("-" * 30)
for i in range(0, len(a), 2):
    print("員工" + a[i] + "{:^10}".format(s1) + "{:>2}".format(a[i+1]))
    sum = sum + int(a[i+1])
    avg = round(sum / len(a) * 2, 2)
print("-" * 30)
print("合計薪資：" + "{:^10}".format(z) + "{:>8,}".format(sum))
print("平均薪資：" + "{:^10}".format(z) + "  {:>8,}".format(avg))
print("=" * 30)
