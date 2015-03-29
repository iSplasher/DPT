from general import gui
from general.network import network
import parser
from dir import log_write
import dptconst as dpt

def run_window():
    gui.root.mainloop()

def check_if_exist(file, string):
    """Checks if string already exist within file
    parameters: file, string
    Returns False if string already exist
    """
    with open(file, 'r', encoding='utf-8') as x:
        for line in x:
            if string == line:
                return False
        return True


def add_post(post):
    "Adds a post in current thread"
    pass

def add_thread(thread_number):
    "Adds thread to listbox if it doesn't already exist"
    if check_if_exist(thread_number):
        with open(dpt.thread_numbers_file, 'a', encoding='utf-8') as thread_number_file:
            thread_number_file.write("{}\n".format(thread_number))
    else:
        log_write("Thread already exist!")

def start():
    "Will look for any new threads and posts and add them"
    while True:
        t_number, posts = network.get_posts()
        add_thread(t_number)
