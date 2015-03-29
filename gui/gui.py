from tkinter import *
from tkinter import ttk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()


root = Tk()
root.title("Daily Programming Thread")
window = ttk.Panedwindow(root, orient=HORIZONTAL)
left = ttk.Labelframe(window, text='Latest Threads', width=130, height=400)
right = ttk.Labelframe(window, text='Posts', width=700, height=400)
window.add(left)
window.add(right)
window.grid(sticky=(N,S,E,W))

thread_list = Listbox(left, height=30)
thread_list.grid(column=0, row=0, sticky=(N,S))
posts_view = Text(right, width=70, height=37)
posts_view.grid(column=0, row=0, sticky=(N,S,E,W))

#scrollbars
thread_list_scroll = ttk.Scrollbar(left, orient=VERTICAL, command=thread_list.yview)
thread_list['yscrollcommand'] = thread_list_scroll.set
thread_list_scroll.grid(column=1, row=0, sticky=(N,S))
 
posts_view_scroll = ttk.Scrollbar(right, orient=VERTICAL, command=posts_view.yview)
posts_view['yscrollcommand'] = posts_view_scroll.set
posts_view_scroll.grid(column=1, row=0, sticky=(N,S))
#OBS: set state to 'normal' if you want to add text (even from loops)
posts_view['state'] = DISABLED 

#making widgets resizeable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
left.grid_rowconfigure(0, weight=2)
left.grid_columnconfigure(0, weight=2)
left.grid_columnconfigure(1, weight=0)
right.grid_rowconfigure(0, weight=2)
right.grid_columnconfigure(0, weight=15)



for x in range(50):
    x = "1254637" + str(x)
    thread_list.insert('end', x)

