from queue import Queue
from queue import LifoQueue

q = Queue(maxsize=10)
q.put(20)
q.put(2)
q.put(120)
q.put(200)
q.put(30)
q.put(3)
q.put(220)
q.put(14)
q.put(1)
q.put(180)

print(q.empty())
print(q.full())
print(q.qsize())

q.put(200)

# q.put_nowait(200)

while(q.empty() is False):
    print(q.get())

# print(q.get_nowait())

q1 = LifoQueue()

q1.put(20)
q1.put(2)
q1.put(120)
q1.put(200)
q1.put(30)
while(q1.empty() is False):
    print(q1.get())
