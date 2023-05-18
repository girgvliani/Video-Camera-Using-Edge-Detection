import threading
import time


def hello():
    print("hello")


t = threading.Timer(4, hello)
t.start()
t.is_alive()  # return true
time.sleep(5)  # sleep for 5 sec
t.is_alive()  # return false
