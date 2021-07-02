'''
+------+------+-----+
| 25.4 | 45.1 | off |
+------+------+-----+
'''
import tkinter
import random
from tkinter import font
from PIL import Image, ImageTk
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://arduino-iot-202107-default-rtdb.firebaseio.com/'
})

def listenerDoor(event):
    print(event.data)
    # 換圖片
    if event.data == 1:
        doorLabel.config(image=door_open_photo)
        doorLabel.image = door_open_photo
    elif event.data == 0:
        doorLabel.config(image=door_close_photo)
        doorLabel.image = door_close_photo

def listenerDHT11Temp(event):
    print(event.data)
    tempValue.set(event.data)

def listenerDHT11Humi(event):
    print(event.data)
    humiValue.set(event.data)

def listenerFirebase():
    firebase_admin.db.reference("/door").listen(listenerDoor)
    firebase_admin.db.reference("/dht11/temp").listen(listenerDHT11Temp)
    firebase_admin.db.reference("/dht11/humi").listen(listenerDHT11Humi)


def update_temp():
    value = random.uniform(20, 30)
    value = "%.2f" % value
    value = float(value)
    db.reference('/dht11/temp').set(value)


def update_humi():
    value = random.uniform(50, 80)
    value = "%.2f" % value
    value = float(value)
    db.reference('/dht11/humi').set(value)

def update_door():
    # 若現在是開門 1 狀態，就送出關門 0, 反之亦然
    pass

root = tkinter.Tk()
root.geometry("500x150")
root.title("Firebase console")

myfont = font.Font(family='Helvetica', size=36, weight='bold')
myfont2 = font.Font(family='Helvetica', size=24)

door_open_photo  = ImageTk.PhotoImage(Image.open('door_open.png'))
door_close_photo = ImageTk.PhotoImage(Image.open('door_close.png'))

tempValue = tkinter.StringVar()
tempValue.set("00.0 C")

humiValue = tkinter.StringVar()
humiValue.set("00.0 %")

tempLabel = tkinter.Label(root, textvariable=tempValue, font=myfont)
humiLabel = tkinter.Label(root, textvariable=humiValue, font=myfont)
doorLabel = tkinter.Label(root, image=door_close_photo, font=myfont)

updateTempButton = tkinter.Button(text='Temp', command=lambda: update_temp(), font=myfont2)
updateHumiButton = tkinter.Button(text='Humi', command=lambda: update_humi(), font=myfont2)
updateDoorButton = tkinter.Button(text='Door', command=lambda: update_door(), font=myfont2)

root.rowconfigure(0, weight=1)
root.columnconfigure((0, 1, 2), weight=1)

tempLabel.grid(row=0, column=0, sticky='EWNS')
humiLabel.grid(row=0, column=1, sticky='EWNS')
doorLabel.grid(row=0, column=2, sticky='EWNS')
updateTempButton.grid(row=1, column=0, sticky='EWNS')
updateHumiButton.grid(row=1, column=1, sticky='EWNS')
updateDoorButton.grid(row=1, column=1, sticky='EWNS')

t1 = threading.Thread(target=listenerFirebase)
t1.start()

root.mainloop()
