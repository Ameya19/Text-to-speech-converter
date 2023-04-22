import playsound as ps
import gtts
from tkinter import *
from tkinter import filedialog,ttk
import os.path

root = Tk()
root.title("Text To Speech Converter")
root.iconbitmap("D:\\Python\\text-to-speech.ico")
root.geometry("600x640")
root.resizable(width=0, height=0)

#Clear screen function
def Clear():
    my_text.delete(1.0,END)


#Converts from text to speech
def Convert():
    try:
        pb.start()
        print(my_text.get(1.0,END))
        if(my_text.get(1.0,END).strip() != "") :
            audio = gtts.gTTS(text=my_text.get(1.0, END), lang="en", slow=False, tld="us")
            entire_location_path = ""
            if(location_textbox.get(1.0,END).strip() != "") :
                path_status = os.path.exists(location_textbox.get(1.0,END).strip())
                if path_status == True :
                    if(mp3_textbox.get(1.0,END).strip() != "") :
                        path = location_textbox.get(1.0,END)
                        filename = mp3_textbox.get(1.0,END)
                        entire_location_path = path.strip() + "/" + filename.strip() + ".mp3"

                        audio.save(entire_location_path)
                        my_label.config(text="The audio file is converted successfully at location " + entire_location_path + ".")
                    else:
                        path = location_textbox.get(1.0,END)
                        filename = mp3_textbox.get(1.0,END)
                        entire_location_path = path.strip() + "/texttospeech.mp3"

                        audio.save(entire_location_path)
                        my_label.config(text="The audio file is converted successfully at location " + entire_location_path + ".")
                else:
                    my_label.config(text="Please enter valid path.")
            else :
                my_label.config(text="Please enter the path.")
        else:
            my_label.config(text="Please enter some text in the textbox.")
    except Exception as e:
        print("Exception: {}",e)
    finally:
        pb.stop()

#Directory path selector
def Directory_path():
    filename = filedialog.askdirectory()
    location_textbox.insert(END,filename)


my_text = Text(root, width=60, height=20, font="Helvetica,14")
my_text.pack(pady=20)

location_label = Label(root,text="Location to store file:")
location_label.pack(padx=23,anchor="w")

location_textbox = Text(root,width=50, height=1)
location_textbox.pack(padx=25,anchor="w")

mp3_label = Label(root,text="FileName:")
mp3_label.pack(padx=23,anchor="w")

mp3_textbox = Text(root,width=50, height=1)
mp3_textbox.pack(padx=25,anchor="w")

progress_bar_frame = Frame(root)
progress_bar_frame.pack()

# progressbar
pb = ttk.Progressbar(
    progress_bar_frame,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

my_label = Label(root, text="")
my_label.pack(pady=10)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="Clear", command=Clear)
clear_button.grid(row=0,column=0)

convert_button = Button(button_frame,text="Convert", command=Convert)
convert_button.grid(row=0, column=1, padx=20)

browse_button = Button(button_frame, text="Browse", command=Directory_path)
browse_button.grid(row=0, column=2)

root.mainloop()