#Import the required Libraries
from tkinter import *
from turtle import update
from PIL import Image,ImageTk
# from matplotlib import image

root = Tk()
root.geometry("2000x1070")

f1=Frame(root,bg="black",borderwidth=4,relief=SUNKEN)
f1.pack(side=TOP,fill="x")

def home():
    update

def data_Upload():
    root.destroy()
    import dataUpload

def footage_Upload():
    root.destroy()
    import footageUpload    

def Live_CCTV():
    root.destroy()
    import Face_recogination

def login():
    root.destroy()
    import login 

def about_us():
    pass


# b2=Label(root,text="Facio", font=("Roboto 24 bold"), bg="black", fg="white").pack(side=TOP, anchor="nw",expand=True,padx=(10,0))

b2=Button(f1,fg="white",bg="black",text="Facio",font=("Roboto 24 bold underline"),command=home)
b2.pack(side=LEFT,expand=True, anchor="nw")

b1=Button(f1,fg="white",bg="black",text="Home",font=("Roboto 17 bold underline"))
b1.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b5=Button(f1,fg="white",bg="black",text="Data Upload",font=("Roboto 17 bold"),command=data_Upload)
b5.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))
# b1.grid(padx=(500,0),pady=(0,0))

b3=Button(f1,fg="white",bg="black",text="Footage Upload",font=("Roboto 17 bold"),command=footage_Upload)
b3.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b4=Button(f1,fg="white",bg="black",text="Live CCTV",font=("Roboto 17 bold"),command=Live_CCTV)
b4.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b6=Button(f1,fg="white",bg="black",text="About Us",font=("Roboto 17 bold"),command=about_us)
b6.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b5=Button(f1,fg="white",bg="black",text="Login",font=("Roboto 17 bold"),command=login)
b5.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

# b7=Button(f1,fg="white",bg="black",text="Sign In",font=("Roboto 17 bold"),command=Sign_)
# b7.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

frame = Frame(
    root,
    bg='#A8B9BF'
    )
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT,fill=Y)
canvas= Canvas(root, width= 1700, height= 1500)
# scrollbar.config(command=canvas.yview)
canvas.pack()

img= (Image.open("photo1.png"))
resized_image= img.resize((1200,950), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
bg=canvas.create_image(260,10, anchor=NW, image=new_image)

# img1=ImageTk.PhotoImage(Image.open("learnmore.png"))

def cmd(event):
    root.destroy()
    import dataUpload
img1=(Image.open("photo2.png"))  

resized_image1= img1.resize((150,40), Image.ANTIALIAS)
new_image1= ImageTk.PhotoImage(resized_image1)
bg1=canvas.create_image(360,557, anchor=NW, image=new_image1)

# Button=canvas.create_image(370,450,image=img1)
canvas.tag_bind(bg1,"<Button-1>",cmd) 

def cmd(event):
    root.destroy()
    import footageUpload 
img1=(Image.open("photo2.png"))  

resized_image2= img1.resize((150,40), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
bg2=canvas.create_image(880,800, anchor=NW, image=new_image2)

# Button=canvas.create_image(370,450,image=img1)
canvas.tag_bind(bg2,"<Button-1>",cmd) 

root.mainloop()