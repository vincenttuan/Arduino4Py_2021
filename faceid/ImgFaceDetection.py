import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_smile.xml')

# 設定 img 位置
#img = cv2.imread('./image/test.jpg')
#img = cv2.imread('./image/tzuyu.jpg')
#img = cv2.imread('./image/what.jpg')
img = cv2.imread('./image/people.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
        gray,              # 待檢測圖片，一般來說設定成灰度圖像可以加快檢測速度
        scaleFactor=1.1,   # 檢測粒度。若粒度增加會加速檢測速度，但會影響準確率
        minNeighbors=10,   # 每個目標至少要檢測到幾次以上，才被認定是真數據
        minSize=(30, 30),  # 數據搜尋的最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE
)
print("face:", len(faces), faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray  = gray[y:y+h, x:x+w]
    roi_color = img[y:y + h, x:x + w]
    smile = smile_cascade.detectMultiScale(
        roi_gray,  # 待檢測圖片，一般來說設定成灰度圖像可以加快檢測速度
        scaleFactor=1.1,  # 檢測粒度。若粒度增加會加速檢測速度，但會影響準確率
        minNeighbors=2,  # 每個目標至少要檢測到幾次以上，才被認定是真數據
        minSize=(30, 30),  # 數據搜尋的最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("smile:", len(smile), smile)
    for(sx, sy, sw, sh) in smile:
        # 繪文字 putText(來源, 文字, 左下座標, 字型, 字型大小, 文字顏色, 文字線條寬度)
        cv2.putText(roi_color, 'Smile', (sx, sy - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

cv2.imshow('Face', img)
c = cv2.waitKey(0)  # 搭配 cv2.imshow
