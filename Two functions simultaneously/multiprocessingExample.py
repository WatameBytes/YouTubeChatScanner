import multiprocessing

def function1():
    print("Inside The Function 1")

def function2():
    print("Inside The Function 2")

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=function1)
    process2 = multiprocessing.Process(target=function2)

    process1.start()
    process2.start()