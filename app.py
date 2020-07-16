from abc import ABC, abstractclassmethod

# Stream is an abstract class since it is derived from abstract base class called 'ABC'
class Stream(ABC):

    # To ensure all derived calss of 'Stream' class has a method named 'read()'
    # we decorate the read() method with '@abstractclassmethod' decorator
    @abstractclassmethod
    def read(self):
        #we put 'pass' so that we don't need to write anything more for the method
        pass


class MemoryStream(Stream):
    def __init__(self):
        self.title = "This is a memory stream"

# We cannot derive MemoryStream from Stream class unless we implement the read() as we did below:
    def read(self):
        return self.title

memoryStream = MemoryStream()
print(memoryStream.read())