# Python program to illustrate the concept
# of threading
# importing the threading module
import threading

x = 0
  
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
  
def thread_task(lock):
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()

def print_cube(num):
	# function to print cube of given num
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))

def main_task():
    global x
    # setting global variable x as 0
    x = 0
  
    # creating a lock
    lock = threading.Lock()
  
    # creating threads
    t3 = threading.Thread(target=thread_task, args=(lock,))
    t4 = threading.Thread(target=thread_task, args=(lock,))
  
    # start threads
    t3.start()
    t4.start()
  
    # wait until threads finish their job
    t3.join()
    t4.join()

if __name__ =="__main__":
	# creating thread


    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

	# starting thread 1
    t1.start()
	# starting thread 2
    t2.start()

	# wait until thread 1 is completely executed
    t1.join()
	# wait until thread 2 is completely executed
    t2.join()

    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))

	# both threads completely executed
    print("Done!")
