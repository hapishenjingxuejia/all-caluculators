import easygui
import easygui as gui
import numpy as np

operations = {
    '加法': lambda x, y: x + y,
    '减法': lambda x, y: x - y,
    '乘法': lambda x, y: x * y,
    '除法': lambda x, y: x / y
}


def calculate_basic_operation():
    operation = gui.buttonbox('请选择基本运算类型：', choices=list(operations.keys()))
    num1 = gui.enterbox('请输入第一个数字：')
    num2 = gui.enterbox('请输入第二个数字：')

    try:
        result = operations[operation](float(num1), float(num2))
        gui.msgbox(f'结果为：{result}')
    except ValueError:
        gui.msgbox('输入无效，请重新输入数字！')


def calculate_advanced_operation():
    operation = gui.buttonbox('请选择高级运算类型：', choices=['开方', '乘方'])
    num = gui.enterbox('请输入一个数字：')

    try:
        num = float(num)
        if operation == '开方':
            result = np.sqrt(num)
        else:
            power = gui.enterbox('请输入乘方指数：')
            result = np.power(num, float(power))
        gui.msgbox(f'结果为：{result}')
    except ValueError:
        gui.msgbox('输入无效，请重新输入数字！')


def password_check(attempts_limit):
    attempts = 0
    while attempts < attempts_limit:
        password = gui.passwordbox('请输入密码：')
        if password == '123456':  # 此处设置您要设定的密码
            return True
        else:
            attempts += 1
            gui.msgbox(f'密码错误，请重新输入。剩余尝试次数：{attempts_limit - attempts}')

    gui.msgbox('密码错误次数过多，程序退出。')
    return False


def developer_mode():
    developer_password = 'abcdef'  # 设置开发者模式密码
    attempts_limit = 5  # 设置重试次数上限
    if easygui.passwordbox("开发者密码", "开发者模式") == developer_password:
        while True:
            choice = gui.buttonbox('请选择开发者模式操作类型：', choices=['更改密码', '退出'])
            if choice == '更改密码':
                new_password = gui.passwordbox('请输入次数：')
                if new_password:
                    if attempts_limit:
                        attempts_limit = new_password
                        gui.msgbox('密码已更新！')
            else:
                break


while True:
    choice = gui.buttonbox('请选择操作类型：', choices=['普通模式', '开发者模式', '退出'])

    if choice == '普通模式':
        if not password_check(5):
            break

        while True:
            operation_choice = gui.buttonbox('请选择操作类型：', choices=['基本运算', '高级运算', '绝对值运算', '退出'])

            if operation_choice == '基本运算':
                calculate_basic_operation()
            elif operation_choice == '高级运算':
                calculate_advanced_operation()
            elif operation_choice == '绝对值运算':
                num = gui.enterbox('请输入一个数字：')
                try:
                    result = abs(float(num))
                    gui.msgbox(f'结果为：{result}')
                except ValueError:
                    gui.msgbox('输入无效，请重新输入数字！')
            else:
                break

    elif choice == '开发者模式':
        developer_mode()
    else:
        break
