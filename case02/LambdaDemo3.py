# lambda lab:
# 請利用 lambda 做出能夠判斷 odd 奇數, even 偶數的函式
# result(4) 得到 "even"
# result(3) 得到 "odd"
# 印出結果的函式也一律使用 lambda

result      = lambda n : "Even" if n % 2 == 0 else "Odd"
printResult = lambda x : print(x)

n = 3
printResult(result(n))
