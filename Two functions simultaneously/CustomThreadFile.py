import threading

# Create NEW Thread objects
class CustomThreadClass:
    def __init__(self, targetFunction):
        self.Thread = threading.Thread(target=targetFunction)
        self.Thread.start()