#  Реализуйте структуру данных, представляющую собой расширенную структуру стек.
#  Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
#  и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.
#
# Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1),
# затем снимается следующий верхний элемент (top2), и затем как результат операции сложения
# на вершину стека кладется элемент, равный top1 + top2.
#
# Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2)
# и целочисленного деления (top1 // top2).
#
# Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.

class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())



def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    print(ex_stack)
    ex_stack.sub()
    assert ex_stack.pop() == 6
    print(ex_stack)
    ex_stack.sum()
    assert ex_stack.pop() == 7
    print(ex_stack)
    ex_stack.mul()
    assert ex_stack.pop() == 2
    print(ex_stack)
    assert len(ex_stack) == 0
    print(ex_stack)

test()