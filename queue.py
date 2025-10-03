# Implementation in Python

class Queue:
    def __init__(self):
        self.queue = []   # using a list to store queue elements


    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to queue")

    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        removed_item = self.queue.pop(0)  # removes first element
        print(f"{removed_item} dequeued from queue")
        return removed_item

  
    def peek(self):
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
            return None
        return self.queue[0]

  
    def is_empty(self):
        return len(self.queue) == 0

    
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", " <- ".join(map(str, self.queue)))


# 🧪 Example Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Front element is:", q.peek())

q.dequeue()
q.display()

q.dequeue()
q.dequeue()
q.dequeue()  # extra dequeue to show empty handling
