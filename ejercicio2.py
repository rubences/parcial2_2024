class PriorityQueue:
    def __init__(self):
        self.high = []
        self.medium = []
        self.low = []

    def enqueue(self, item, priority):
        if priority == 'high':
            self.high.append(item)
        elif priority == 'medium':
            self.medium.append(item)
        elif priority == 'low':
            self.low.append(item)
        else:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")

    def dequeue(self):
        if self.high:
            return self.high.pop(0)
        elif self.medium:
            return self.medium.pop(0)
        elif self.low:
            return self.low.pop(0)
        else:
            raise IndexError("Dequeue from an empty priority queue")

    def is_empty(self):
        return not (self.high or self.medium or self.low)

class ScrollStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
priority_queue = PriorityQueue()
scroll_stack = ScrollStack()

# Adding requests to the priority queue
priority_queue.enqueue("Help from Rohan", 'high')
priority_queue.enqueue("Help from Gondor", 'medium')
priority_queue.enqueue("Help from Shire", 'low')

# Processing the most urgent request
if not priority_queue.is_empty():
    urgent_request = priority_queue.dequeue()
    scroll_stack.push(urgent_request)

# Retrieving the most urgent scroll
if not scroll_stack.is_empty():
    most_urgent_scroll = scroll_stack.pop()
    print(f"Processing: {most_urgent_scroll}")