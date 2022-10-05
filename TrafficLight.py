"""
1. Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    __color = [None, None, None]
    __count = 0

    def running(self, color):
        TrafficLight.__color[TrafficLight.__count] = color
        color_list = ["красный", "жёлтый", "зелёный"]

        if TrafficLight.__color[0] == color_list[TrafficLight.__count]:
            print(color)
            time.sleep(7)
        elif TrafficLight.__color[1] == color_list[TrafficLight.__count]:
            print(color)
            time.sleep(2)
        elif TrafficLight.__color[2] == color_list[TrafficLight.__count]:
            print(color, '\t\n поехали!!!')
            time.sleep(10)
        else:
            raise BaseException(
                f""" Нарушена последовательность цвета: {TrafficLight.__count + 1} позицией указан {color}, 
                правильная последовательность (красный, жёлтый, зелёный) должен быть: {color_list[TrafficLight.__count]} 
                """)
        TrafficLight.__count += 1


TrafficLight_ = TrafficLight()
TrafficLight_.running('красный')
TrafficLight_.running('жёлтый')
TrafficLight_.running('зелёный')

# или

from itertools import cycle, count
from time import sleep

class TrafficLight:
    color = ['red', 'yellow', 'green']

    def __init__(self):
        if TrafficLight.color[0] != 'red':
            err = 'Color error'
            return err
        elif TrafficLight.color[1] != 'yellow':
            err = 'Color error'
            return err
        elif TrafficLight.color[2] != 'green':
            err = 'Color error'
            return err

    def running(self, col):
        timer = {'red': 7, 'yellow': 2, 'green': 5}
        print(f'{TrafficLight.color[col].upper()}, {timer.get(TrafficLight.color[col])} sec')
        for l in count(-timer.get(TrafficLight.color[col]), 1):
            if l > -1 : break
            print(-l)
            sleep(1)

try:
    tl = TrafficLight()
except:
    print('TrafficLight is broken!')
else:
    for l in cycle([0, 1, 2]):
        tl.running(l)