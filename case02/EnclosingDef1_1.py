# 嵌套函式 1

def mssage(text):
    text = text + " by 巨匠電腦"
    print("mssage 方法執行")
    def print_message():
        print("print_message 方法執行")
        print(text)

    return print_message


if __name__ == '__main__':
    m1 = mssage("Hello")
    print(m1)
    m1()