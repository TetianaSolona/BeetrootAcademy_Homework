# task 1

class Stack:
    def __init__(self):
        self.item = ['h', 'e', 'l', 'l', 'o']

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def get_from_stack(self, search):
        new = []
        while self.item:
            new.append(self.item.pop())
        while new:
            val = new.pop()
            if search == val:
                return True
        return False

    def reverse(self):
        string = ''
        for i in range(len(self.item)):
            string += self.item.pop()
        return string


# Balance brackets
dic: dict = {'(': ')',
             '{': '}',
             '[': ']'}


def balanced(expression: str):
    stack: list = []
    flag: bool = True
    for i in expression:
        if i in dic.keys():
            stack.append(i)
        else:
            if not stack:
                flag = False
                break
            br = stack.pop()
            for i in br:
                if dic[br] == dic.values():
                    return flag

    if len(stack) != 0:
        flag = False
    return flag


if __name__ == '__main__':
    print(Stack().get_from_stack('e'))
    print(Stack().get_from_stack('m'))
    print(Stack().reverse())
    print(balanced('([])'))
    print(balanced('([]'))
    print(balanced('([]}}'))
