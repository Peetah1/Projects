import tkinter as tk
from tkinter import filedialog
class Color_Button(tk.Button):
    def __init__(self, window, bg, command):
        self.bg = bg  
        super().__init__(master=window, bg=bg, command=command, activebackground=bg)





load_list=[]

def menu_open():
    global a
    if a == 0:
        load_button.place(x=10, y=50, height=40, width=80)
        save_button.place(x=10, y=90, height=40, width=80)
        a = 1
    else:
        load_button.place_forget()
        save_button.place_forget()
        a = 0

prev_x=None
prev_y=None

prev_x=0
prev_y=0
drawing_width=2
a=0       
current_color = None




def on_button_press(event):
    
    global running, prev_x, prev_y
    running = True
    prev_x=event.x
    prev_y=event.y
    
def on_move(event):
    
    global running, prev_x, prev_y
    running = True
    draw2(event)


def change_color(color):
    global current_color
    
    current_color=color
    drawing.config(bg=current_color)
    
    

def draw2(event):
    global running, prev_x, prev_y, current_color
    
    if running :
         
         canvas.create_line(prev_x, prev_y, event.x, event.y, width=drawing_width, fill=current_color)
         prev_x=event.x
         prev_y=event.y
         load_list.append(prev_x)
         load_list.append('\n')
         load_list.append(prev_y)
         load_list.append('\n')
         load_list.append(current_color)
         load_list.append('\n')
         load_list.append(drawing_width)
         load_list.append('\n')


def on_button_release(event):
    
    global running, prev_x, prev_y
    running = False



def change_size(new_width):
    global drawing_width
    drawing_width=new_width




my_string=''


def save_info():
    global load_list, my_string
    file=filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file", ".txt")])
    if file is None:
        return
    
    filetext=open(file.name, 'wt')
    for i in load_list:
        my_string=str(i)
        filetext.write(my_string)
       
    filetext.close()
    
index=0
start_sizex=0
start_sizey=0


def load_info():
    global index, drawing_width, prev_x, prev_y, current_color, start_sizex, start_sizey, counter
    filename = filedialog.askopenfilename(
        filetypes=[('text files', '.txt')])
    filetext=open(filename, 'r')
    '''print(filetext.read())'''
    file_string=filetext.read()
    file_list=file_string.split()
    '''print(file_list)'''

    start_sizex=file_list[0]
    start_sizey=file_list[1]
    
    
    for i in file_list:
        print(i)
       
        if index%4==0:
               prev_x=int(i)
        elif index%4==1:
               prev_y=int(i)
        elif index%4==2:
               current_color=i
        elif index%4==3:
                drawing_width=int(i) 
                canvas.create_line(start_sizex, start_sizey, prev_x, prev_y, width=drawing_width, fill=current_color )
                start_sizex=prev_x
                start_sizey=prev_y
        index+=1

    filetext.close()

#window
window=tk.Tk()
window.geometry('1000x800')
window.title('drawing_game')
window.config(bg='#CACAE1')


#buttons
file_button=tk.Button(window, text='file', font='arial 20', command=menu_open) 
file_button.place(x=10, y=10, height=40, width=80)

load_button=tk.Button(window, text='load', font='arial 20', command=load_info )
save_button=tk.Button(window, text='save', font='arial 20', command=save_info )

red_button=Color_Button(window, bg='red', command=lambda: change_color('red'))
red_button.place(x=0, y=700, width= 100, height=100)

blue_button=Color_Button(window, bg='blue', command=lambda: change_color('blue'))
blue_button.place(x=100, y=700, width= 100, height=100)

yellow_button=Color_Button(window, bg='yellow', command=lambda: change_color('yellow'))
yellow_button.place(x=0, y=600, width= 100, height=100)

green_button=Color_Button(window, bg='green', command=lambda: change_color('green'))
green_button.place(x=100, y=600, width= 100, height=100)

purple_button=Color_Button(window, bg='purple', command=lambda: change_color('purple'))
purple_button.place(x=0, y=500, width= 100, height=100)

pink_button=Color_Button(window, bg='pink', command=lambda: change_color('pink'))
pink_button.place(x=100, y=500, width= 100, height=100)

orange_button=Color_Button(window, bg='orange', command=lambda: change_color('orange'))
orange_button.place(x=0, y=400, width= 100, height=100)

brown_button=Color_Button(window, bg='brown', command=lambda: change_color('brown'))
brown_button.place(x=100, y=400, width= 100, height=100)

black_button=Color_Button(window, bg='black', command=lambda: change_color('black'))
black_button.place(x=0, y=300, width= 100, height=100)

white_button=Color_Button(window, bg='white', command=lambda: change_color('white'))
white_button.place(x=100, y=300, width= 100, height=100)


thickness1_button=tk.Button(window, bg='white', text='1x', activebackground='white', font='arial 20', command=lambda: change_size('2') )
thickness1_button.place(x=250, y=100, height=100, width=100)

thickness2_button=tk.Button(window, bg='white', text='2x', activebackground='white', font='arial 20', command=lambda: change_size('4') )
thickness2_button.place(x=350, y=100, height=100, width=100)

thickness3_button=tk.Button(window, bg='white', text='3x', activebackground='white', font='arial 20', command=lambda: change_size('6') )
thickness3_button.place(x=450, y=100, height=100, width=100)

#white frame and label
canvas=tk.Canvas(window, bg='white')
canvas.place(x=250, y=200, height=600, width=750)
drawing=tk.Label(canvas)


#drawing
canvas.bind('<ButtonPress-1>', on_button_press)
canvas.bind('<B1-Motion>', on_move)
canvas.bind('<ButtonRelease>', on_button_release )












window.mainloop()