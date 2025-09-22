money=5000000
name=None

name=input("请输入您的姓名：")
#定义查询函数
def query(show_header):#show-header为传入变量，如果后面调用此函数输入false就不打印查询余额，如果输入ture就打印
    if show_header:
        print("------------查询余额------------")
    print(f"{name}，您好，您的余额剩余：{money}元")
#定义存款函数
def saving():
    global money#修改全局变量
    try:
        num=int(input("请输入存款金额："))
        if num<=0:
            print("存款金额必须大于0！")
        else:
            money+=num
            print("------------存款-------------")
            print(f"{name}，您好，您存款{num}元成功。")
            query(False)
    except ValueError:
        print("请输入有效的数字！")

#定义取款函数
def get_money():
    global money
    try:
        num=int(input("请输入取款金额："))
        if num<=0:
            print("取款金额必须大于0！")

        elif num>money:
            print("余额不足！")

        else:
             money-=num
             print("-------------取款-------------")
             print(f"{name}，您好，您取款{num}元成功。")
             query(False)
    except ValueError:
        print("请输入有效的数字！")

def show_menu():
    print("-------------主菜单-----------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t\t[输入1]\t")
    print("存款\t\t[输入2]\t")
    print("取款\t\t[输入3]\t")
    print("退出\t\t[输入4]\t")

def main():
    while True:
        show_menu()
        choice=input("请输入您的选择：")
        if choice=="1":
            query(True)
        elif choice=="2":
            saving()#不需要传入参数，函数内部获取输入
        elif choice=="3":
            get_money()
        elif choice=="4":
            print("感谢使用，再见。")
            break
        else:
            print("输入无效，请重新选择！")

if __name__ == '__main__':
    main()

