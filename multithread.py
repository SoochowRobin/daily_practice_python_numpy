# this file is to implement multithreaded programming
# this file use _thread(old module)
import _thread
import time


# define a function for the thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f'{threadName} : {time.ctime(time.time())}')

# create two threads as follows
try:
    # here, first parameter is function, second parameter is a tuple with parameters
    _thread.start_new_thread(print_time, ('Thread_1', 2,))
    _thread.start_new_thread(print_time, ('Thread_2', 4,))
except:
    print('Error: unable to start thread')


while True:
    pass

