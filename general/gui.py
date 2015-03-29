from tkinter import *
from tkinter import ttk
from general.dptconst import threads_path, thread_numbers_file
from time import sleep

#class Window(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self, master)
#        self.grid()


root = Tk()
root.title("Daily Programming Thread")
window = ttk.Panedwindow(root, orient=HORIZONTAL)
left = ttk.Labelframe(window, text='Latest Threads', width=130, height=400)
right = ttk.Labelframe(window, text='Posts', width=700, height=400)
window.add(left)
window.add(right)
window.grid(sticky=(N,S,E,W))


#Threads
def get_threads_numbers():
    numbers = []
    with open(thread_numbers_file, "r", encoding='utf-8') as file:
        for line in file:
            numbers[0] = str(line)
    return numbers

while True:
    all_threads = get_threads_numbers()
    
    #need to use another thread to not make whole GUI sleep
    #get_thread_wait()

thread_numbers = StringVar(value=all_threads)
thread_list = Listbox(left, listvariable=thread_numbers, height=30)
thread_list.grid(column=0, row=0, sticky=(N,S))

#Posts
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



#for x in range(50):
#    x = "1254637" + str(x)
#    thread_list.insert('end', x)

