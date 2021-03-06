# this file is to use locking mechanism that allows you to synchronize threads
import threading
import time


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting '+ self.name)
        # get lock to synchronized threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # free lock to release next thread
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(f'{threadName}  {time.ctime(time.time())}')
        counter -= 1


threadLock = threading.Lock()
threads = []

# create new threads
thread1 = myThread(1, 'Thread-1', 5)
thread2 = myThread(2, 'Thread-2', 5)
thread3 = myThread(3, 'Thread-3', 5)

# start new threads
thread1.start()
thread2.start()
thread3.start()

# add threads to thread list
threads.append(thread2)
threads.append(thread1)
threads.append(thread3)

# wait for all threads to complete
for t in threads:
    t.join()
print('Exiting Main Thread')