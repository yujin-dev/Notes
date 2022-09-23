class CircularQueue(object):
    def __init__(self, limit=10):
        self.limit = limit
        self.queue = [None for _ in range(limit)]
        self.front = self.rear = -1

    def __str__(self):
        if (self.rear >= self.front):
            return " ".join([str(self.queue[i]) for i in range(self.front, self.rear+1)])
        else: # self.rear < self.front
            q1 = " ".join([str(self.queue[i]) for i in range(self.front, self.limit)])
            q2 = " ".join([str(self.queue[i]) for i in range(0, self.rear+1)])
            return q1 + " " + q2

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear+1) %self.limit == self.front

    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full")
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.limit
            self.queue[self.rear] = data
            print("enqueue", self.queue, self.rear, data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        elif (self.front==self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1)%self.limit
            print("dequeue", self.queue, self.front)
if __name__ == '__main__':
    myCQ = CircularQueue(5)
    myCQ.enqueue(14)
    myCQ.enqueue(22)
    myCQ.enqueue(13)
    myCQ.enqueue(16)
    print('Queue:', myCQ)
    myCQ.dequeue()
    myCQ.dequeue()
    print('Queue:', myCQ)
    myCQ.enqueue(9)
    myCQ.enqueue(20)
    myCQ.enqueue(5)
    myCQ.enqueue(5)
    myCQ.dequeue()
    myCQ.dequeue()
    print('Queue:', myCQ)