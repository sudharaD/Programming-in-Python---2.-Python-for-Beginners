# Stacks
my_stack = []

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

push(my_stack, "a")
push(my_stack, "b")
push(my_stack, "c")

print(my_stack)

print(pop(my_stack))

print(my_stack)

print("--------------------------------------------")
# Queues
my_queue = []

def enqueue(queue, value):
    queue.append(value)

def dequeue(queue):
    return queue.pop(0)

enqueue(my_queue, "a")
enqueue(my_queue, "b")
enqueue(my_queue, "c")

print(my_queue)

print(dequeue(my_queue))

print(my_queue)