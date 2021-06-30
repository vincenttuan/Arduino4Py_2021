import cv2

carPath = './xml/tw.xml'
carCascade = cv2.CascadeClassifier(carPath)

img = cv2.imread('./image/car1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = carCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(60, 60),
    flags=cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Car number', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

