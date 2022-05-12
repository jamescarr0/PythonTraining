from collections import deque

class TicketQueue():
    '''
    Simple deque, no error checking, real python deque exercise
    '''
    def __init__(self) -> None:
        self.deque = deque()
        
    def add_person(self, name):
        self.deque.append(name)
        print(f"{name} has been added to the queue")

    def service_person(self):
        print(f"{self.deque.popleft()} has been serviced and removed from the que")

    def bypass_queue(self, name):
        self.deque.appendleft(name)
        print(f"{name} bypassed queue and placed at the front")

    def print_que(self):
        print(self.deque)

t = TicketQueue()
t.service_person()