import threading

l = threading.Lock()

print("Before 1st acquire!!!")
l.acquire()
print("Before 2nd acquire!!!")
l.acquire()

# This might be obvious, but this will never run
# Yup, we are stuck and program trying to acquire lock second time while the 1st lock is not released
print("Acquired Lock Twice!!")

# This is a very basic example of Deadlock
