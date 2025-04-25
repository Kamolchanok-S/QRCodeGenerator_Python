from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image

def displayImage(file_name):
    img = ImageTk.PhotoImage(Image.open(file_name))
    img_label = Label(image=img)
    img_label.image = img
    canvas.create_window(200,330,window=img_label)
    

def generateQRCode():
    # Get input data
    link_name = name_txt.get()
    link_url = link_txt.get()
    # print(link_name + " " + link_url)
    file_name = link_name + ".png"
    
    # start generate QR code
    qr_link = pyqrcode.create(link_url)
    # save qr as png file
    qr_link.png(file=file_name, scale=4)
    displayImage(file_name)
    

#Main root
root = Tk()
root.title("QR Code Generator")
root.configure(bg="#17d6c4")
root.geometry("460x460")

#Sub-main display
canvas = Canvas(root, width=400, height=500, bg="#00ffe7")
canvas.pack(pady=30) 

# App name display
app_label = Label(root, text="QR Code Generator", font=('Arial', 20, 'bold'),bg="#22baac",padx=10, pady=10)
canvas.create_window(200,50, window=app_label)

# QR code name
name_label = Label(root, text="Name", bg="#4ebeb4")
canvas.create_window(200,100,window=name_label)

# QR code textbox
name_txt = Entry(root, width=50)
canvas.create_window(200,130,window=name_txt)

# link QR code
link_label = Label(root, text="URL", bg="#4ebeb4")
canvas.create_window(200,160,window=link_label)

# link QR code textbox
link_txt = Entry(root, width=50)
canvas.create_window(200,190,window=link_txt)

# button generate
btn = Button(text="Create QR Code", command=generateQRCode)
canvas.create_window(200,240,window=btn)

root.mainloop()