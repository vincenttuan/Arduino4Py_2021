import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')

# 設定 img 位置
img = cv2.imread('./image/test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
        gray,             # 待檢測圖片，一般來說設定成灰度圖像可以加快檢測速度
        scaleFactor=1.1,  # 檢測粒度。若粒度增加會加速檢測速度，但會影響準確率
        minNeighbors=10,   # 每個目標至少要檢測到幾次以上，才被認定是真數據
        minSize=(30, 30), # 數據搜尋的最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE
)

print(len(faces), faces)

