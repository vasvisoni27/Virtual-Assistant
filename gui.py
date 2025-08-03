from tkinter import*
from PIL import Image , ImageTk
import action 
import spech_to_text 


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot is not None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
          

def ask():

    ask_val= spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val is not None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("550x675")
root.title("AI Desktop Assistant")
root.resizable(False,False)
root.config(bg="#A17BA2")


# Main Frame
Main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
Main_frame.config(bg="#D2ADD3")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 75 ,  pady =  10)

# Text Lable 
Text_lable = Label(Main_frame, text = "NOVAMIND" , font=("Georgia" ,  20 , "bold", "underline" ) , bg = "#D2ADD3")
#Text_lable1 = Label(Main_frame, text = "NovaMind" , font=("Georgia" ,  14 , "bold", "italic" ) , bg = "#D2ADD3")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)
#Text_lable1.grid(row=0 ,  column=1, padx=20 , pady= 10)


# Image 
#Display_Image = ImageTk.PhotoImage(Image.open("image/Untitled.png"))
resized_photo_image = ImageTk.PhotoImage(Image.open("image/Untitled.png").resize((200, 200)))
Image_Lable = Label(Main_frame, image= resized_photo_image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)


# Add a text widget

text=Text(root , font= ('Consolas') , bg = "#D2ADD3")
text.grid(row = 1 ,  column=1 , pady=20)
text.xview_scroll
text.yview_scroll
text.place(x= 100, y= 375, width= 375, height= 100) 



# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=100 , y = 500 , width= 375, height= 30)



# Add a text button1
button1 =  Button(root,  text="ASK" ,font=("Georgia" ,  8 , "bold", "italic" ), bg="#D2ADD3" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 575)

# Add a text button2
button2 =  Button(root,  text="SEND" ,font=("Georgia" ,  8 , "italic", "bold" ), bg="#D2ADD3" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 230, y= 575)

# Add a text button3
button3 = Button(root, text="DELETE",font=("Georgia" ,  8 , "bold", "italic" ), bg="#D2ADD3" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x=400, y= 575)
root.mainloop()