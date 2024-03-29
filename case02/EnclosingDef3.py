# 嵌套函式 3
# 多重相乘

def multi(n):
    if n == 0:
        return None

    # def multi(x):
    #     return n * x

    multi = lambda x: n * x

    return multi  # 得到第8行的方法參考

if __name__ == '__main__':
    n3 = multi(3)
    n5 = multi(5)
    x = 6
    print(n3(x)) # x = 6
    print(n3(n5(x))) # n3(n5(x)) -> n3(n5(6)) -> n3(30) -> 90