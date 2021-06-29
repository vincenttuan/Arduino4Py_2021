import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')

# 設定 Webcam 位置
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)  # 800, 640
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)  # 600, 480

while True:
    # 捕捉 frame-by-frame
    # ret : 2唔到的 frame 若是正確的會回傳 true
    # frame : 捕捉到的區域資料
    ret, frame = cap.read()
    print(ret, frame)

    # 圖像灰階化
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 畫出每一個臉的範圍
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 在臉部周圍畫矩形框
    for (x, y, w , h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)

    # 顯示在 frame UI 上面
    cv2.imshow('My Video', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

# 釋放資源
cap.release()
cv2.destroyAllWindows()
