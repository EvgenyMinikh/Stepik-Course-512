"""
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом,
чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение,
состоящее из только что добавленного элемента.
"""

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, args):
        super().append(args)
        super().log(args)


o = LoggableList()
o.append(12)
print(o)