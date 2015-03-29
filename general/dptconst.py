import os

log_path = os.path.join(os.getcwd(), ("log.txt"))
threads_path = os.path.join(os.getcwd(), ("threads"))
thread_numbers_file = os.path.join(threads_path, ("threads.dpt"))

def close():
    pass

def first_time():
    "Checks if it's firstime starting up"
    #TO-DO: check in dpt.config (add file if it doesnt exist)
    return True