import os
import time
from time import gmtime, strftime
import general.dptconst
from general.dptconst import log_path
from general.dptconst import threads_path
from general.dptconst import thread_numbers_file

if not os.path.isfile(threads_path):
    open(log_path, 'x').close()

def log_write(text='All seems fine~'):
    """Adds text to log file like this:
    ######## current time ######
    Your text
    ############################
    """

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
        
        if not os.path.isfile(thread_numbers_file):
            open(thread_numbers_file, 'x').close()
    except:
        log_write("Failed creating \"{}\" directory!".format(threads_path))