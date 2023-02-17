import sys
import logging
from time import sleep
from keyboard import *


def liter_limit(liter:float, a: float, b: float):
    try:
        liter = float(liter)
        if a < liter <= b:
            return 1

        elif liter < 0:
            return 2

        elif liter == 0:
            return 3
        else:
            return 0
    except:
        return 4


class Teapot:
    def __init__(self, liter: int = None, time_boiling=10):
        self.liter = liter
        self.time_boiling = time_boiling / 2  # Время закипания

    def run(self):
        logging.basicConfig(level=logging.DEBUG, filename="log.log", format='%(asctime)s %(levelname)s:%(message)s')
        print()
        print("Сколько литров воды вы хотите налить в чайник")
        print("Если захотите остановить чайник удерживайте 'A' eng")
        self.liter = input("( 0 - 1.0 ) :")

        action = liter_limit(self.liter, 0, 1.0)

        if action == 1:

            print("Чайник вкл")
            logging.debug('Start Teapot')
            t = 0
            while True:
                try:
                    if is_pressed("a"):
                        sys.exit()

                    print(f"{int(t)}°")
                    if t == 100.0:
                        break
                    t += self.time_boiling * float(self.liter)

                    sleep((1.0 - (1.0 - float(self.liter))))
                except:
                    logging.error('Stop Teapot')
                    print("Чайник остановлен")
                    quit()

            logging.debug('End Teapot')
            print("Чайник вскипел")
            logging.debug('Off Teapot')
            print("Чайник выкл")
        elif action == 2:
            logging.error('Error code  2')
            print("В чайнике не может быть отрицательное значение литров")
            print("Попробуйте ещё раз")
            return self.run()
        elif action == 3:
            logging.error('Error code  3')
            print("Упс, чайник пустой")
            print("Попробуйте ещё раз")
            return self.run()
        elif action == 4:
            logging.error('Error code  4')
            print("Нужны литры, а не символы")
            print("Попробуйте ещё раз")

            return self.run()
        else:
            logging.error('Error code  0')
            print("Чайник не вмещает в себя больше одного литра")
            print("Попробуйте ещё раз")
            return self.run()


teapot1 = Teapot()


teapot1.run()
