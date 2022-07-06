import threading
import time


def function_1():
  time.sleep(1)
  print("Inside The Function 1")

def function_2():
  print("Inside The Function 2")

# Create a new thread
Thread1 = threading.Thread(target=function_1)

# Create another new thread
Thread2 = threading.Thread(target=function_2)

# Start the thread
Thread1.start()

# Start the thread
Thread2.start()

# Wait for the threads to finish
Thread1.join()
Thread2.join()

print("Done!")