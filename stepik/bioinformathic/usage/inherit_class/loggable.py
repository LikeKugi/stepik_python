# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом,
# чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение,
# состоящее из только что добавленного элемента.

import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, __object) -> None:
        x = super(LoggableList, self).append(__object)
        self.log(__object)



a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)