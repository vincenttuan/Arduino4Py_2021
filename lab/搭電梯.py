from time import sleep

current_floor = 1

print('幸福大廈共有1~7層樓')

print('進電梯')
while True:
    target_floor = input('您現在在 %d 樓。請問要去哪一樓(輸入 0 可以出電梯)?\n>> ' % current_floor)

    try:
        target_floor = int(target_floor)
    except ValueError:
        print('格式錯誤，請輸入數字\n')
        continue

    if target_floor == 0:
        break

    if target_floor == current_floor:
        continue

    if target_floor < 1 or target_floor > 7:
        print('請輸入介於 1-7 的整數')
        continue

    if target_floor < current_floor:
        print('電梯下樓')
        while target_floor < current_floor:
            print(current_floor)
            current_floor = current_floor - 1
            sleep(1)
        print(current_floor)
    else:
        print('電梯上樓')
        while target_floor > current_floor:
            print(current_floor)
            current_floor = current_floor + 1
            sleep(1)
        print(current_floor)

print('出電梯')


