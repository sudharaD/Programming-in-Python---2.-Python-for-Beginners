my_stack = []

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

push(my_stack, "a")
push(my_stack, "b")
push(my_stack, "c")

print(my_stack)
