import os
import time
from time import gmtime, strftime
import dptconst
from dptconst import log_path

threads_path = os.path.join(os.getcwd(), ("threads"))

if not os.path.isfile(threads_path):
    open(log_path, 'a').close()

def log_write(text='All seems fine~'):
    dec_start = "########   "
    dec_end = "   ########"
    time = strftime("%H:%M:%S, %a, %d %b %Y +0000", gmtime())
    decoration = dec_start + time + dec_end + '\n'
    end = '\n'
    for x in range(len(dec_start + time + dec_end)):
        end += '#'
    end += '\n'

    with open(log_path, 'a', encoding='utf-8') as log:
        log.write(decoration)
        log.write(text)
        log.write(end)

def initial():
    try:
        if not os.path.isdir(threads_path):
            os.makedirs(threads_path)
            log_write("Created \"{}\" successfully.".format(threads_path))
    except:
        log_write("Failed creating \"{}\" directory!".format(threads_path))