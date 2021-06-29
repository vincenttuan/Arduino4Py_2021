import cv2

# 設定 Webcam 位置
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

while True:
    # 捕捉 frame-by-frame
    # ret : 2唔到的 frame 若是正確的會回傳 true
    # frame : 捕捉到的區域資料
    ret, frame = cap.read()
    print(ret, frame)

# 釋放資源
cap.release()