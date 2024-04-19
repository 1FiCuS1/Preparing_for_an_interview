class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

    @staticmethod
    def check_brackets(brackets_string):
        stack = Stack()
        brackets_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for bracket in brackets_string:
            if bracket in brackets_map.values():
                stack.push(bracket)
            elif bracket in brackets_map.keys():
                if stack.is_empty() or brackets_map[bracket] != stack.pop():
                    return "Несбалансированные скобки"

        return "Сбалансированные скобки" if stack.is_empty() else "Несбалансированные скобки"


print(Stack.check_brackets("(((([{}]))))"))  # Сбалансированно
print(Stack.check_brackets("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(Stack.check_brackets("{{[()]}}"))  # Сбалансированно
print(Stack.check_brackets("{}"))  # Несбалансированно
print(Stack.check_brackets("{{[(])]}}"))  # Несбалансированно
print(Stack.check_brackets("[[{())}]"))  # Несбалансированно