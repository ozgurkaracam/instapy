from Browser import Browser
import time
import userDetails
import tkinter as tk
import fileoptest as fo

instapy=Browser(userDetails.username,userDetails.password)
fo.delInstagram(userDetails.username,userDetails.password)
# time.sleep(10)

# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=400, height=300)
# canvas1.pack()
#
# entry1 = tk.Entry(root)
# canvas1.create_window(200, 140, window=entry1)
#
#
# def getSquareRoot():
#     x1 = entry1.get()
#
#     label1 = tk.Label(root, text=float(x1) ** 0.5)
#     canvas1.create_window(200, 230, window=label1)
#
#
# button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
# canvas1.create_window(200, 180, window=button1)
#
# root.mainloop()
