'''
+-----------------+
| ___3___   傳送   |
| 766,20.50,52.00 |
+-----------------+
'''
import tkinter
from tkinter import font

root = tkinter.Tk()
root.geometry("600x400")
root.title = "Arduino GUI"

respText = tkinter.StringVar()
respText.set("0,0.0,0.0")

sendButton0  = tkinter.Button(text='0')
sendButton1  = tkinter.Button(text='1')
sendButton2  = tkinter.Button(text='2')
sendButton3  = tkinter.Button(text='3')
sendButton4  = tkinter.Button(text='4')
sendButton8  = tkinter.Button(text='8')
receiveLabel = tkinter.Label(root, textvariable=respText)

root.rowconfigure((0,1), weight=1) # 列 0, 列 1 同步放大縮小
root.columnconfigure((0,1,2,3,4,5), weight=1) # 欄 0, 欄 1, 欄 2 ...同步放大縮小

sendButton0.grid(row=0,   column=0, columnspan=1, sticky='EWNS')
sendButton1.grid(row=0,   column=1, columnspan=1, sticky='EWNS')
sendButton2.grid(row=0,   column=2, columnspan=1, sticky='EWNS')
sendButton3.grid(row=0,   column=3, columnspan=1, sticky='EWNS')
sendButton4.grid(row=0,   column=4, columnspan=1, sticky='EWNS')
sendButton8.grid(row=0,   column=5, columnspan=1, sticky='EWNS')
receiveLabel.grid(row=1,  column=0, columnspan=6, sticky='EWNS')

root.mainloop()


