from enum import Enum
from abc import ABCMeta, abstractmethod

"""
    Facade pattern : classes , instructions -> single function을 통해 실행
    # 복잡한 interface를 노출시키지 않고 단일 함수로 실행가능하게 함
    # ABCMeta 
"""
State = Enum("State", "new running sleeping restart zombie")
class User:
    pass

class Process:
    pass

class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass

class FileServer(Server):
    def __init__(self):
        self.name = "FileServer"
        self.state = State.new

    def boot(self):
        self.state = State.running

    def kill(self, restart=True):
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        print(f"trying to create the file {name} {user} with permissions {permissions}")

class ProcessServer(Server):
    def __init__(self):
        self.name = "ProcessServer"
        self.state = State.new

    def boot(self):
        self.state = State.running

    def kill(self, restart=True):
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name):
        print(f"trying to create the file {name} {user}")

class WindowServer:
    pass

class NetworkServer:
    pass

class OperatingSystem:
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        self.ps.create_file(user, name)

def main():
    os = OperatingSystem()
    os.start()
    os.create_file("foo", "hello", "-rw-r-r")
    os.create_process("bar", "ls /tmp")

if __name__ == "__main__":
    main()

