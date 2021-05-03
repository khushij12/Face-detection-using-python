import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
import random
from PIL import Image, ImageTk



face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")




def img_browse():

    def img_detect(filename):
       
        img = cv2.imread(filename)
        cv2.imshow("People", img)
        cv2.waitKey(0)
        gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces1 = face_cascade.detectMultiScale(gray1, scaleFactor=1.05, minNeighbors=5)
        for x, y, w, h in faces1:
            img1 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.imshow("Capture", img1)
        cv2.waitKey(0)
        win3.destroy()
    
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        # Change label contents
        l1.configure(text="File Opened: "+filename,bg=bg_color,fg=fg_color)
        b2=tk.Button(win3,text='Okay',anchor='s',bg='#C7EA46',command=lambda: img_detect(filename),fg=fg_color,bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',activebackground='#acc93e',activeforeground=fg_color)
        b2.place(x=556//2-35,y=270)
        changeOnHover(b2, "#acc93e", "#C7EA46")
        
    win3=tk.Toplevel()    #open browsing window
    win3.geometry('556x400')
    win3.title('Choose Image')
    win3.configure(background=bg_color)
    l=tk.Label(win3,text="Choose your file",font=("Candara",12,"bold"),padx='10',pady='10',fg=fg_color,bg='#ff0080')
    l.pack(fill='both')
    
    l1=tk.Label(win3,font=("Candara",12,"bold"),padx='10',pady='30',fg=fg_color,bg=bg_color)
    l1.pack(fill='both')
    b1=tk.Button(win3,text='Browse Image',anchor='center',command=browseFiles,bg='#30D5C8',fg=fg_color,bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',activebackground='#239990',activeforeground=fg_color)
    b1.place(x=556//2-(80),y=200)
    changeOnHover(b1, "#239990", "#30D5C8")
    win3.mainloop()

    
def video_detect():
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    a = 1
    while True:
        a = a + 1
        check, frame = video.read()
        gray2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray2, scaleFactor=1.05, minNeighbors=5)
        for x, y, w, h in faces:
            img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imshow("Capture", img2)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()

def overlay():
    def colorvid(name):
        if name==0:
            video=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        else:
            video =  cv2.VideoCapture(name)

        
        # color = int(input("1.Blue\n2.Red\n3.Green\n4.Yellow"))
        def fun(color):
            
            if color == 1:
                lower_range = np.array([110, 50, 50])
                upper_range = np.array([130, 255, 255])
            elif color == 2:
                lower_range = np.array([169, 100, 100])
                upper_range = np.array([189, 255, 255])
            elif color == 3:
                lower_range = np.array([40, 40,40])
                upper_range = np.array([70, 255,255])
            elif color ==4:
                lower_range = np.array([22, 93, 0])
                upper_range = np.array([45, 255, 255])
            a = 1
            while True:
                a = a + 1
               
                check, frame = video.read()

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, lower_range, upper_range)

                cv2.imshow('image', frame)
                cv2.imshow('mask', mask)

                cv2.resizeWindow('image', 650, 1000)
                cv2.resizeWindow('mask', 650, 1000)

                key = cv2.waitKey(1)
                if key == ord('q'):
                    win1.destroy()
                    win2.destroy()
                    break

            video.release()
            cv2.destroyAllWindows()

        win2=tk.Tk()
        win2.geometry('400x300')
        win2.title('choose the color')
        win2.configure(background=bg_color)
        
        l=tk.Label(win2,text="Choose a color",font=("Candara",12,"bold"),padx='10',pady='10',fg=fg_color,bg='#ff0080')
        l.pack(fill='both')

        b1=tk.Button(win2,bg='#2117e6',bd='5',activebackground='#140bba',width='10',command=lambda:fun(1),anchor='center')
        b1.place(x=150,y=100)
        b2=tk.Button(win2,bg='#f51c18',bd='5',activebackground='#cc120e',width='10',command=lambda:fun(2),anchor='center')
        b2.place(x=150,y=140)
        b3=tk.Button(win2,bg='#6ee30e',bd='5',activebackground='#55a811',width='10',command=lambda:fun(3),anchor='center')
        b3.place(x=150,y=180)
        b4=tk.Button(win2,bg='#f2f211',bd='5',activebackground='#d6d609',width='10',command=lambda:fun(4),anchor='center')
        b4.place(x=150,y=220)

        changeOnHover(b1, "#140bba", "#2117e6")
        changeOnHover(b2, "#cc120e", "#f51c18")
        changeOnHover(b3, "#55a811", "#6ee30e")
        changeOnHover(b4, "#d6d609", "#f2f211")
        win2.mainloop()

    
    win1=tk.Tk()
    win1.title('Choose any option')
    win1.geometry('450x300')
    win1.configure(background=bg_color)
    l=tk.Label(win1,text="   Choose the option",anchor="n",font=("Candara",12,"bold"),padx='10',pady='10',fg=fg_color,bg='#ff0080')
    l.pack(fill='x')
    def fun1():
        name=0
        colorvid(name)

    def fun2():
        name='neon.mp4'
        colorvid(name)

    def fun3():
        name='wave.mp4'
        colorvid(name)
    frame=tk.Frame(win1,bg=bg_color,width='450')
    frame.place(x=150,y=100)
    
    b1=tk.Button(frame,text="Live Video",anchor='center',command=fun1,bd = '5',fg=fg_color,bg='#FF0080',activebackground='#bd005f',activeforeground=fg_color,font=("Berlin Sans FB",12,"bold"))
    b1.pack()
    b2=tk.Button(frame,text="Recorded video 1",anchor='center',command=fun2,bd = '5',fg=fg_color,bg='#30D5C8',activebackground='#239990',activeforeground=fg_color,font=("Berlin Sans FB",12,"bold"))
    b2.pack()
    b3=tk.Button(frame,text="Recorded video 2",anchor='center',command=fun3,bd = '5',fg=fg_color,bg='#C7EA46',activebackground='#acc93e',activeforeground=fg_color,font=("Berlin Sans FB",12,"bold"))
    b3.pack()

    changeOnHover(b1, "#bd005f", "#FF0080")
    changeOnHover(b2, "#239990", "#30D5C8")
    changeOnHover(b3, "#acc93e", "#C7EA46")
    
        
    win1.mainloop()



def game():
    cat_cascade = cv2.CascadeClassifier("visionary.net_cat_cascade_web_LBP.xml")
    images = ['game1.jpg', 'game2.jpg', 'game3.jpg', 'game4.jpg', 'game5.jpg']

    def play():
        win4.destroy()
        img = cv2.imread(random.choice(images))
        cv2.imshow("cat", img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        
        

        gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        catface1 = cat_cascade.detectMultiScale(gray1, scaleFactor=1.04, minNeighbors=5)
        catnum = 0

        for x, y, w, h in catface1:
            img1 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 3)
            catnum += 1
        
        
        def Take_input():

            INPUT = inputtxt.get("1.0", "end-1c")
            cv2.imshow("Capture", img1)
            cv2.waitKey(3000)
            cv2.destroyAllWindows()
            
            if(int(INPUT) == catnum):
                vid = cv2.VideoCapture('won1.mp4')
                while (vid.isOpened()):

                    ret, frame = vid.read()
                    if ret == True:

                        cv2.imshow('Frame', frame)

                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break

                    else:
                        break
                vid.release()
                cv2.destroyAllWindows()
            else:
                
                vid = cv2.VideoCapture('lose.mp4')
                while (vid.isOpened()):

                    ret, frame = vid.read()
                    if ret == True:

                        cv2.imshow('Frame', frame)

                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break

                    else:
                        break
                vid.release()
                
        win5=tk.Tk()
        win5.geometry('500x300')
        win5.title('Guess it')
        win5.configure(bg=bg_color)
        
        head=tk.Frame(win5,width='10',height='20',bg='#c8a2c8')
        head.place(x=0,y=0)

        l=tk.Label(win5,text="\t\t\t            Guess it:\t\t\t\t",font=("Candara",12,"bold"),padx='10',pady='10',fg=fg_color,bg='#c8a2c8')
        l.pack(fill='both')
        inputtxt = tk.Text(win5, height = 1,width = 2,bg = "light yellow")
        inputtxt.place(x=235,y=100)
        b=tk.Button(win5,text='SUBMIT',activebackground='#d48900',activeforeground=fg_color,bg='#FFA500',fg='white',bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',width='10',command=Take_input)
        b.place(x=180,y=180)
        changeOnHover(b, "#d48900", "#ffa500")
        win5.mainloop()
        
  
            
    
    win4=tk.Tk()
    win4.title('Welcome to Cat Guessing Game')
    win4.geometry('525x300')
    win4.configure(bg='#262424')

    l=tk.Label(win4,text="\t\t  Welcome to Cat Guessing Game\t\t",font=("Candara",12,"bold"),padx='10',pady='10',fg=fg_color,bg='#c8a2c8')
    l.pack(fill='both')

    l1=tk.Label(win4,text="\nWhat you have to do\nWhen you will hit the Play button you will get one image\nFrom that image you have to count number of cats\nMind well you will only get 2 seconds",font=("Candara",12,"bold"),fg='white',bg='#262424')
    l1.place(x=30,y=50)

    b=tk.Button(win4,text='PLAY!!',activebackground='#bd005f',activeforeground=fg_color,bg='#FF0080',fg='white',bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',width='10',command=play)
    b.place(x=190,y=200)
    changeOnHover(b, "#bd005f", "#FF0080")
    win4.mainloop()

    
    
	
def changeOnHover(button, colorOnHover, colorOnLeave):

	# adjusting backgroung of the widget
	# background on entering widget
	button.bind("<Enter>", func=lambda e: button.config(
		background=colorOnHover))

	# background color on leving widget
	button.bind("<Leave>", func=lambda e: button.config(
		background=colorOnLeave))

	
root=tk.Tk()


root.title('Face detection and overlay')
#root.maxsize(1000,1000)
#root.minsize(1000,500)
root.title("Face detection and Overlay features")
bg_color='#262424'
fg_color='white'
fg_color1='#4eb4ab'
root.configure(background=bg_color)




bgImage = tk.PhotoImage(file="10.png")
width = bgImage.width()
height = bgImage.height()

root.geometry('{}x600'.format(width))

frame=tk.Frame(root,width=width,height=height)
frame.grid(row=0)

canvas = tk.Canvas(frame, width = width, height = height, bg = "black")
canvas.create_image((width / 2, height / 2), image = bgImage)
canvas.place(x = 0, y = 0)



l1=tk.Label(root,text="To detect face from image: ",anchor='w',font=("Candara",12,"bold"),fg=fg_color)
l1.configure(background=bg_color)
l1.place(x = 180, y = 200)

#creating button for image
B=tk.Button(root,text="IMAGE",bg='#C7EA46',fg='white',bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',width='10',activebackground='#acc93e',activeforeground=fg_color,command=img_browse)
#fg-fontcolor
B.place(x = 500, y = 190)


l2=tk.Label(root,text="To detect face from FACE-CAM: ",font=("Candara",12,"bold"),fg=fg_color)
l2.configure(background=bg_color)
l2.place(x = 180, y = 300)


B1=tk.Button(root,text="VIDEO",bg='#30D5C8',fg='white',bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',width='10',activebackground='#239990',activeforeground=fg_color,command=video_detect)
B1.place(x = 500, y = 290)



l3=tk.Label(root,text="To see overlay in video:",font=("Candara",12,"bold"),fg=fg_color)
l3.place(x = 180, y = 400)

l3.configure(background=bg_color)
B2=tk.Button(root,text="OVERLAY",bg='#FFA500',fg='white',bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',width='10',activebackground='#d48900',activeforeground=fg_color,command=overlay)
B2.place(x = 500, y = 390)



l4=tk.Label(root,text="Play the game and cheer!",font=("Candara",12,"bold"),fg=fg_color)
l4.place(x=180,y=500)
l4.configure(bg=bg_color)
B3=tk.Button(root,text="HIT IT!!",bg='#c8a2c8',fg=fg_color,bd = '5',font=("Berlin Sans FB",12,"bold"),height='1',width='10',activebackground='#a686a6',activeforeground=fg_color,command=game)
B3.place(x=500,y=490)
changeOnHover(B, "#acc93e", "#C7EA46")
changeOnHover(B1, "#239990", "#30D5C8")
changeOnHover(B2, "#d48900", "#FFA500")
changeOnHover(B3, "#a686a6", "#c8a2c8")

root.mainloop()




























