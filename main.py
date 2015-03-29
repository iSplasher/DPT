from uni import run_window, start
from dir import initial
import general.dptconst
from general.dptconst import first_time

if first_time():
    try:
        initial()
    except:
        print("Cannot startup")

if __name__ == "__main__":

    start()
    run_window()
