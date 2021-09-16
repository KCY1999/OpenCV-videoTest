import cv2
import threading
import tkinter as tk
from PIL import ImageTk, Image
import time
import load

class cam():
    def __init__(self):
        self.flag = 0
        self.frame = []
        self.window = tk.Tk()
        self.window.title("Python")
        self.window.geometry("600x480")
        self.label1 = tk.Label(self.window, text="", fg="#0000ff")
        self.label1.pack()
        self.btn1 = tk.Button(self.window, text="play", fg="red", command=self.play)
        self.btn1.pack()
        self.btn2 = tk.Button(self.window, text="pause", fg="blue", command=self.ppause)
        self.btn2.pack()
        self.btn3 = tk.Button(self.window, text="stop", fg="black", command=self.sstop)
        self.btn3.pack()

        self.window.mainloop()

    def camtest(self):
        self.flag = 0
        self.pause = False
        self.cam1 = cv2.VideoCapture("video.mp4")
        self.stop = False
        #self.cam1 = cv2.VideoCapture(0)

        while(True):
            if cv2.waitKey(1) & 0xFF == ord('q') or self.stop == True:
                break
            #self.status,self.frame=self.cam1.read()
            if self.pause==False:
                self.status, self.frame = self.cam1.read()
            if self.status==False:
                break
            if self.status:
                time.sleep(0.05)
                timee = self.cam1.get(cv2.CAP_PROP_POS_MSEC)
                print(timee)

            oimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            img2 = Image.fromarray(oimg)
            image2 = ImageTk.PhotoImage(image=img2)

            if self.label1 is None:
                self.label1 = tk.Label(image=image2)
                self.label1.image = image2
                self.label1.pack()
            else:
                self.label1.configure(image=image2)
                self.label1.image = image2

            #cv2.imshow("im",self.frame)

        self.cam1.release()

        cv2.destroyAllWindows()

    def play(self):
        self.flag = 1
        self.btn1.configure(state='disabled')
        threading.Thread(target=self.camtest, daemon=True).start()

    def getFrame(self):
        return self.frame

    def ppause(self):
        if self.pause==False:
            self.flag = 0
            self.pause = True
            return

        if self.pause == True:
            self.flag = 1
            self.pause = False
            return
    def sstop(self):
        self.flag = 1
        self.stop=True
        self.btn1.configure(state='active')

c=cam()