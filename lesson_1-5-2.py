"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.
Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных элементов по мере их накопления.
Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
"""

class Buffer:
    def __init__(self):
        self.buffer = []

    def add(self, *a):
        self.buffer += list(a)

        if len(self.buffer) >= 5:
            for elem in self.get_current_part():
                print(elem)

    def get_current_part(self):
        if len(self.buffer) < 5:
            return self.buffer

        summ_list = []
        while (len(self.buffer)) >= 5:
            summ = 0
            for i in range(5):
                summ += self.buffer.pop(0)

            summ_list.append(summ)

        return summ_list


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())